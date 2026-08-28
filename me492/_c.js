
        const CACHE_VERSION = '2026-08-28.3';
        const VIEW_STATE_KEY = 'me492_quiz_view_state';
        const ANSWERS_STORAGE_KEY = 'me492_quiz_answers_v2';
        const RETAKE_ANSWERS_STORAGE_KEY = 'me492_quiz_retake_answers_v2';
        const OPTION_ORDER_STORAGE_KEY = 'me492_quiz_option_orders_v2';
        const TABLE_CELLS_STORAGE_KEY = 'me492_quiz_table_cells_v2';

        const SOURCES = [
            {
                id: 'set-1',
                label: 'ME 492 past papers',
                file: 'compiled.json',
                description: '244 questions taken from the past papers: entrepreneurship & free enterprise, creativity & innovation, business planning, venture stages, marketing, intellectual property, legal forms, financing, budgeting, calculations and the "because" section. 107 of these are checked against the 2005 official marking scheme.'
            },
            {
                id: 'set-ai',
                label: 'AI generated, 100 new',
                file: 'ai-generated-100.json',
                description: '100 new questions written from the lecture notes and slides, in the same shape as the real paper: 70 plain, 22 i/ii/iii and 8 "because" items, plus a fresh 12-question calculation block. Not from a past paper, so treat a disagreement here as a prompt to check the slide.'
            },
            {
                id: 'set-site',
                label: 'Extra past-paper items, 48',
                file: 'site-extracted-48.json',
                description: '48 questions found on samplequestions.vercel.app that are not in the first set. 19 cover ground the other sets are thin on, mostly the economists. 29 are calculations from four fresh tables, including two cash budgets that need a borrowing rule the guide did not cover. Three combination answers were corrected against the lecturer\'s notes; each says so in its explanation.'
            }
        ];

        let allQuestionsData = [];
        let userAnswers = getStoredAnswers();
        let retakeAnswers = getStoredRetakeAnswers();
        let currentMode = 'set';
        let currentSourceId = SOURCES[0].id;
        let currentAnswerStore = 'main';
        let currentQuestionsData = [];
        let currentViewKey = 'set-1';
        let currentExamLabel = 'All Questions';
        let correctCount = 0;
        let wrongCount = 0;
        let currentModeQuestions = [];
        let optionOrders = getStoredOptionOrders();
        let tableCells = getStoredTableCells();
        let lastRandomIndex = -1;

        function normalizeOptionText(optionText) {
            return String(optionText || '').replace(/^\s*[A-E][.)]\s*/, '').trim();
        }

        function normalizeStoredAnswers(storedAnswers) {
            const normalized = {};
            Object.entries(storedAnswers || {}).forEach(([key, value]) => {
                normalized[key] = Array.isArray(value)
                    ? value.map(normalizeOptionText)
                    : [normalizeOptionText(value)];
            });
            return normalized;
        }

        function getStoredAnswers() {
            return normalizeStoredAnswers(JSON.parse(localStorage.getItem(ANSWERS_STORAGE_KEY) || '{}'));
        }

        function getStoredRetakeAnswers() {
            return normalizeStoredAnswers(JSON.parse(localStorage.getItem(RETAKE_ANSWERS_STORAGE_KEY) || '{}'));
        }

        function getStoredOptionOrders() {
            try {
                return JSON.parse(localStorage.getItem(OPTION_ORDER_STORAGE_KEY) || '{}');
            } catch (error) {
                return {};
            }
        }

        function saveAnswers(answerStore = 'main') {
            if (answerStore === 'retake') {
                localStorage.setItem(RETAKE_ANSWERS_STORAGE_KEY, JSON.stringify(retakeAnswers));
                return;
            }
            localStorage.setItem(ANSWERS_STORAGE_KEY, JSON.stringify(userAnswers));
        }

        function saveOptionOrders() {
            localStorage.setItem(OPTION_ORDER_STORAGE_KEY, JSON.stringify(optionOrders));
        }

        // The calculation tables print "?" in every cell you have to work out.
        // Those cells become inputs, and what you type is kept here so a run
        // survives a reload, a change of card and a Retake Wrong.
        function getStoredTableCells() {
            try {
                const parsed = JSON.parse(localStorage.getItem(TABLE_CELLS_STORAGE_KEY) || '{}');
                return parsed && typeof parsed === 'object' ? parsed : {};
            } catch (error) {
                return {};
            }
        }

        function saveTableCells() {
            try {
                localStorage.setItem(TABLE_CELLS_STORAGE_KEY, JSON.stringify(tableCells));
            } catch (error) {
                // Storage full or blocked. Keep the working on screen regardless.
            }
        }

        function setTableCell(cellKey, value) {
            const trimmed = String(value == null ? '' : value).trim();
            if (trimmed) tableCells[cellKey] = trimmed;
            else delete tableCells[cellKey];
            saveTableCells();
        }

        // Every input anywhere on the page that holds this cell. A scenario's
        // table appears on several cards at once, and they must agree.
        function syncTableCell(cellKey, value, origin) {
            document.querySelectorAll(`.cell-input[data-cell="${CSS.escape(cellKey)}"]`)
                .forEach(input => { if (input !== origin) input.value = value; });
        }

        // The table is shared, so clearing it clears it on every card that
        // prints it. That is the whole point of filling it once.
        function clearWorking(button) {
            const card = button.closest('.question-card');
            const keys = Array.from(card.querySelectorAll('.cell-input'))
                .map(input => input.dataset.cell);
            if (!keys.length) return;
            keys.forEach(key => { delete tableCells[key]; });
            saveTableCells();
            keys.forEach(key => syncTableCell(key, '', null));
            card.querySelector('.cell-input')?.focus();
        }

        function getQuestionKey(question, sourceId) {
            return `${sourceId}:${question.question_number}`;
        }

        function getAnswerForQuestion(question, sourceId, viewSourceId, answersObj) {
            const candidateKeys = [getQuestionKey(question, sourceId)];
            if (viewSourceId === 'all' || viewSourceId === 'random') {
                candidateKeys.push(getQuestionKey(question, viewSourceId));
            }

            for (const key of candidateKeys) {
                if (Object.prototype.hasOwnProperty.call(answersObj, key)) {
                    return { key, value: answersObj[key] };
                }
            }

            return { key: candidateKeys[0], value: undefined };
        }

        function shuffleArray(values) {
            const shuffled = [...values];
            for (let index = shuffled.length - 1; index > 0; index -= 1) {
                const swapIndex = Math.floor(Math.random() * (index + 1));
                [shuffled[index], shuffled[swapIndex]] = [shuffled[swapIndex], shuffled[index]];
            }
            return shuffled;
        }

        function getOptionOrder(question, sourceId, options) {
            const key = getQuestionKey(question, sourceId);
            const storedOrder = optionOrders[key];

            if (Array.isArray(storedOrder)
                && storedOrder.length === options.length
                && new Set(storedOrder).size === options.length
                && storedOrder.every(index => Number.isInteger(index) && index >= 0 && index < options.length)) {
                return storedOrder;
            }

            const order = shuffleArray(options.map((_, index) => index));
            optionOrders[key] = order;
            saveOptionOrders();
            return order;
        }

        function getHeaderOffset() {
            const header = document.querySelector('.header');
            return (header ? header.offsetHeight : 0) + 14;
        }

        function getViewState() {
            try {
                const raw = localStorage.getItem(VIEW_STATE_KEY);
                return raw ? JSON.parse(raw) : null;
            } catch (error) {
                return null;
            }
        }

        function saveViewState(questionIndex = 0) {
            localStorage.setItem(VIEW_STATE_KEY, JSON.stringify({
                mode: currentMode,
                sourceId: currentSourceId,
                viewKey: currentViewKey,
                questionIndex: Number.isFinite(questionIndex) ? questionIndex : 0
            }));
        }

        function clearViewState() {
            localStorage.removeItem(VIEW_STATE_KEY);
        }

        function scrollToQuestion(questionIndex, behavior = 'smooth', saveState = true) {
            const card = document.getElementById(`q-${questionIndex}`);
            if (!card) return false;

            const rect = card.getBoundingClientRect();
            const currentY = window.scrollY || window.pageYOffset;
            const headerOffset = getHeaderOffset();
            const topTarget = currentY + rect.top - headerOffset;
            const centerTarget = currentY + rect.top - ((window.innerHeight - rect.height) / 2);
            window.scrollTo({ top: Math.max(0, Math.min(centerTarget, topTarget)), behavior });
            if (saveState) saveViewState(questionIndex);
            return true;
        }

        function scrollToContinuation(questionIndex, saveState = true) {
            window.setTimeout(() => {
                if (questionIndex < currentQuestionsData.length) {
                    scrollToQuestion(questionIndex, 'smooth', saveState);
                } else {
                    scrollToBottom(saveState);
                }
            }, 250);
        }

        function scrollToBottom(saveState = true) {
            const footer = document.getElementById('footer');
            if (footer) {
                footer.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
            if (saveState && currentQuestionsData.length > 0) {
                saveViewState(Math.max(0, currentQuestionsData.length - 1));
            }
        }

        function setRetakeControls(isRetakeMode) {
            document.getElementById('retake-btn').style.display = isRetakeMode ? 'none' : 'inline-block';
            document.getElementById('return-btn').style.display = isRetakeMode ? 'inline-block' : 'none';
        }

        function setActiveSourceCard(sourceId) {
            document.querySelectorAll('.source-card').forEach(card => {
                card.classList.toggle('active', card.dataset.sourceId === sourceId);
            });
        }

        function sourceLabel(sourceId) {
            return SOURCES.find(source => source.id === sourceId)?.label || sourceId;
        }

        function getQuestionsForSource(sourceId) {
            return allQuestionsData.filter(question => question.sourceId === sourceId);
        }

        function buildSourcesUI() {
            const grid = document.getElementById('source-grid');
            grid.innerHTML = '';

            // Hide the set selector only when there is nothing to choose between.
            const selector = document.querySelector('.selector');
            if (selector) selector.style.display = SOURCES.length <= 1 ? 'none' : '';

            SOURCES.forEach(source => {
                const card = document.createElement('div');
                card.className = 'source-card';
                card.dataset.sourceId = source.id;
                card.innerHTML = `
                    <h3>${source.label}</h3>
                    <p>${source.description}</p>
                `;
                card.onclick = () => showSource(source.id, true);
                grid.appendChild(card);
            });
        }

        async function loadQuestionBanks() {
            try {
                const baseUrl = new URL('.', window.location.href).toString();
                const responses = await Promise.all(
                    SOURCES.map(source => fetch(`${baseUrl}${source.file}?v=${CACHE_VERSION}`, { cache: 'no-store' }).then(response => response.json()))
                );

                allQuestionsData = responses.flatMap((questions, sourceIndex) => {
                    const source = SOURCES[sourceIndex];
                    return questions.map(question => ({
                        ...question,
                        sourceId: source.id,
                        sourceLabel: source.label
                    }));
                });

                buildSourcesUI();
                document.getElementById('loading').style.display = 'none';

                const savedState = getViewState();
                if (savedState && savedState.mode && savedState.sourceId) {
                    restoreSavedView(savedState);
                } else {
                    showSource(currentSourceId, false);
                }
            } catch (error) {
                console.error(error);
                document.getElementById('loading').innerHTML = `<p style="color:var(--danger)">Error loading question banks: ${error.message}</p>`;
            }
        }

        function restoreSavedView(savedState) {
            if (!savedState || !savedState.mode || !savedState.sourceId) {
                return false;
            }

            currentMode = savedState.mode;
            currentSourceId = savedState.sourceId;
            currentAnswerStore = savedState.mode === 'retake' ? 'retake' : 'main';

            if (savedState.mode === 'retake') {
                const savedQuestions = getQuestionsForSource(savedState.sourceId);
                const wrongQuestions = savedQuestions.filter(question => isQuestionWrong(question));
                setRetakeControls(true);
                currentQuestionsData = wrongQuestions;
                renderQuestions(wrongQuestions, {
                    answerStore: 'retake',
                    mode: 'retake',
                    sourceId: savedState.sourceId,
                    shouldRestore: true,
                    shouldAutoscroll: false
                });
                if (Number.isInteger(savedState.questionIndex)) {
                    window.requestAnimationFrame(() => scrollToQuestion(savedState.questionIndex, 'auto', false));
                }
                setActiveSourceCard(savedState.sourceId);
                return true;
            }

            showSource(savedState.sourceId, false, savedState.questionIndex || 0);
            return true;
        }

        function showSource(sourceId, pushState = true, questionIndex = 0) {
            currentSourceId = sourceId;
            currentMode = 'set';
            currentViewKey = sourceId;
            currentAnswerStore = 'main';
            setRetakeControls(false);
            setActiveSourceCard(sourceId);

            const questions = getQuestionsForSource(sourceId);
            renderQuestions(questions, {
                answerStore: 'main',
                mode: 'set',
                sourceId,
                shouldRestore: true,
                shouldAutoscroll: false,
                questionIndex
            });

            if (pushState) saveViewState(questionIndex);
            if (Number.isInteger(questionIndex) && questionIndex >= 0) {
                window.requestAnimationFrame(() => scrollToQuestion(questionIndex, 'auto', false));
            } else {
                window.scrollTo({ top: 0, behavior: 'smooth' });
            }
        }

        function goToNextSource() {
            if (currentMode !== 'set') return;
            const index = SOURCES.findIndex(source => source.id === currentSourceId);
            if (index >= 0 && index < SOURCES.length - 1) {
                showSource(SOURCES[index + 1].id, true, 0);
            }
        }

        function renderQuestions(questions, options = {}) {
            const {
                shouldRestore = false,
                shouldAutoscroll = false,
                answerStore = 'main',
                mode = 'set',
                sourceId = currentSourceId,
                questionIndex = 0
            } = options;

            const feed = document.getElementById('feed');
            feed.innerHTML = '';
            currentQuestionsData = questions;
            currentModeQuestions = questions;
            currentAnswerStore = answerStore;
            document.getElementById('footer').style.display = 'block';

            if (!questions.length) {
                feed.innerHTML = '<div class="panel"><p style="margin:0;color:var(--muted);text-align:center">No questions found.</p></div>';
                calculateStats();
                return;
            }

            questions.forEach((question, idx) => {
                const card = createQuestionCard(question, idx, answerStore, mode, sourceId);
                feed.appendChild(card);
            });

            const currentIndex = SOURCES.findIndex(s => s.id === currentSourceId);
            const isLastSet = currentIndex === SOURCES.length - 1;
            document.getElementById('next-source-btn').style.display = currentMode === 'set' && !isLastSet ? 'inline-block' : 'none';
            calculateStats();

            if (shouldAutoscroll) {
                scrollToContinuation(questionIndex, false);
            }
        }

        function createQuestionCard(question, idx, answerStore, mode, sourceId) {
            const effectiveSourceId = sourceId === 'all' || sourceId === 'random' ? question.sourceId : sourceId;
            const answerKey = getQuestionKey(question, effectiveSourceId);
            const isMultiChoice = Array.isArray(question.correct_answer) && question.correct_answer.length > 1;
            const correctAnswers = (question.correct_answer || []).map(normalizeOptionText);
            const answersObj = answerStore === 'retake' ? retakeAnswers : userAnswers;
            const storedLookup = getAnswerForQuestion(question, effectiveSourceId, sourceId, answersObj);
            const stored = storedLookup.value;
            const card = document.createElement('article');
            card.className = 'question-card';
            card.id = `q-${idx}`;

            const singleSource = SOURCES.length <= 1;
            const tagParts = [`Question ${question.question_number}`];
            if (effectiveSourceId && !singleSource) tagParts.push(sourceLabel(effectiveSourceId));
            if (isMultiChoice) tagParts.push('Choose Multiple');

            card.innerHTML = `
                <div class="question-head">
                    <div class="question-tag">${tagParts.join(' · ')}</div>
                    <div style="color:var(--muted);font-size:0.82rem;">${singleSource ? '' : sourceLabel(question.sourceId)}</div>
                </div>
                <div class="question-text">${renderStem(question.question_text)}</div>
                ${question.question_text.includes('|')
                    ? `<button type="button" class="clear-working"
                         onclick="clearWorking(this)">Clear working</button>`
                    : ''}
            `;

            const optionsWrap = document.createElement('div');
            optionsWrap.className = 'options';
            const options = Array.isArray(question.options) ? question.options : [];
            const optionOrder = getOptionOrder(question, sourceId, options);
            const selectedValues = Array.isArray(stored) ? stored : stored ? [stored] : [];

            optionOrder.forEach(optionIndex => {
                const option = options[optionIndex];
                const normalized = normalizeOptionText(option);
                const button = document.createElement('button');
                button.className = 'option-btn';
                button.dataset.option = normalized;
                button.innerHTML = `<span>${escapeHtml(option)}</span><span class="option-icon"></span>`;
                if (selectedValues.includes(normalized)) button.classList.add('selected');
                button.onclick = () => handleAnswer(question, idx, normalized, button, answerStore, mode, effectiveSourceId, isMultiChoice, correctAnswers);
                optionsWrap.appendChild(button);
            });

            // showAnswer reads these back, so it does not need the question object.
            card.dataset.explanation = question.explanation || '';
            card.dataset.hook = question.hook || '';
            // The guide's section numbering is internal bookkeeping. The card shows
            // the topic name instead, which is what you actually revise from.
            card.dataset.source = question.topic || question.source || '';
            card.dataset.teach = question.teach || '';
            card.dataset.verified = question.verified || '';

            const feedback = document.createElement('div');
            feedback.className = 'answer-feedback';
            feedback.id = `feedback-${idx}`;
            card.appendChild(optionsWrap);
            card.appendChild(feedback);

            if (selectedValues.length) {
                const isCorrect = isMultiChoice
                    ? selectedValues.slice().sort().join('|') === correctAnswers.slice().sort().join('|')
                    : selectedValues[0] === correctAnswers[0];
                showAnswer(idx, isCorrect, correctAnswers, isMultiChoice, false, card);
            }

            return card;
        }

        function handleAnswer(question, idx, selectedOption, button, answerStore, mode, sourceId, isMultiChoice, correctAnswers) {
            const answerKey = getQuestionKey(question, sourceId);
            const answersObj = answerStore === 'retake' ? retakeAnswers : userAnswers;

            if (isMultiChoice) {
                const current = Array.isArray(answersObj[answerKey]) ? [...answersObj[answerKey]] : [];
                const found = current.indexOf(selectedOption);
                if (found >= 0) {
                    current.splice(found, 1);
                    button.classList.remove('selected');
                } else {
                    current.push(selectedOption);
                    button.classList.add('selected');
                }
                answersObj[answerKey] = current;
            } else {
                document.querySelectorAll(`#q-${idx} .option-btn`).forEach(btn => btn.classList.remove('selected'));
                answersObj[answerKey] = [selectedOption];
                button.classList.add('selected');
            }

            saveAnswers(answerStore);

            const selectedAnswers = Array.isArray(answersObj[answerKey]) ? answersObj[answerKey] : [answersObj[answerKey]];
            const isComplete = !isMultiChoice || selectedAnswers.length === correctAnswers.length;
            if (isComplete) {
                const isCorrect = isMultiChoice
                    ? selectedAnswers.slice().sort().join('|') === correctAnswers.slice().sort().join('|')
                    : selectedAnswers[0] === correctAnswers[0];
                showAnswer(idx, isCorrect, correctAnswers, isMultiChoice, isCorrect, document.getElementById(`q-${idx}`));
            }

            calculateStats();
        }

        function showAnswer(idx, isCorrect, correctAnswers, isMultiChoice, autoScroll = false, cardElement = null) {
            const card = cardElement || document.getElementById(`q-${idx}`);
            if (!card) return;
            const feedback = card.querySelector(`#feedback-${idx}`);
            if (!feedback) return;

            const optionBtns = card.querySelectorAll('.option-btn');
            optionBtns.forEach(btn => {
                const value = normalizeOptionText(btn.dataset.option || btn.textContent);
                if (correctAnswers.includes(value)) {
                    btn.classList.add('correct');
                } else if (btn.classList.contains('selected') && !isCorrect) {
                    btn.classList.add('wrong');
                }
                btn.classList.add('locked');
                btn.style.pointerEvents = 'none';
            });

            const explanation = card.dataset.explanation || '';
            const source = card.dataset.source || '';
            // Only the unchecked answers are called out, so the note stays rare.
            const unchecked = (card.dataset.verified || '').startsWith('not checked');
            const sourceLine = unchecked ? `${source} · answer not checked against a printed key` : source;
            const sourceHtml = source ? `<div class="explain-source">${escapeHtml(sourceLine)}</div>` : '';
            const teach = card.dataset.teach || '';
            const teachHtml = teach
                ? `<details class="teach"><summary>The whole topic</summary>`
                  + `<div class="teach-body">${escapeHtml(teach)}</div></details>`
                : '';
            const hook = card.dataset.hook || '';
            const hookHtml = hook
                ? `<div class="hook"><span class="hook-label">Remember</span>${escapeHtml(hook)}</div>`
                : '';
            const explainHtml = (explanation || teach || hook)
                ? `<div class="explain">${escapeHtml(explanation)}${teachHtml}${hookHtml}${sourceHtml}</div>`
                : '';

            feedback.classList.add('show');
            if (isCorrect) {
                feedback.className = 'answer-feedback show feedback-correct';
                feedback.innerHTML = '<strong>✓ Correct!</strong>' + (explainHtml
                    ? `<details class="explain-toggle"><summary>Why</summary>${explainHtml}</details>`
                    : '');
                if (autoScroll) scrollToContinuation(idx + 1);
            } else {
                feedback.className = 'answer-feedback show feedback-wrong';
                const text = isMultiChoice
                    ? `Correct answers: ${correctAnswers.join(', ')}`
                    : `Correct answer: ${correctAnswers[0]}`;
                feedback.innerHTML = `<strong>✗ Wrong</strong><br>${escapeHtml(text)}` + explainHtml;
            }
        }

        // The calculation questions carry the paper's data table. Turn a markdown
        // table into a real one, and leave every other line as escaped text.
        function renderStem(text) {
            const lines = String(text).split('\n');
            const out = [];
            let table = [];
            let prose = [];

            const flushProse = () => {
                const body = prose.join('\n').replace(/^\n+|\n+$/g, '');
                if (body) out.push(`<span>${escapeHtml(body)}</span>`);
                prose = [];
            };
            const flushTable = () => {
                if (table.length) out.push(renderTable(table));
                table = [];
            };

            lines.forEach(line => {
                if (line.trim().startsWith('|')) {
                    if (!table.length) flushProse();
                    table.push(line);
                } else {
                    flushTable();
                    prose.push(line);
                }
            });
            flushTable();
            flushProse();
            return out.join('');
        }

        // Cells are keyed by the table itself, not by the question. Seven
        // questions print the Osagyefo budget, so filling it once fills it on
        // all seven. Same table means same key, everywhere it appears.
        function tableKeyBase(rows) {
            const text = rows.join('\n').replace(/\s+/g, ' ').trim();
            let hash = 2166136261;
            for (let i = 0; i < text.length; i += 1) {
                hash ^= text.charCodeAt(i);
                hash = Math.imul(hash, 16777619);
            }
            return 't' + (hash >>> 0).toString(36);
        }

        function renderTable(rows) {
            const keyBase = tableKeyBase(rows);
            const isRule = cells => cells.every(c => /^:?-{2,}:?$/.test(c));
            const parsed = rows.map(row => row.trim()
                .replace(/^\|/, '').replace(/\|$/, '')
                .split('|').map(c => c.trim()));

            const ruleAt = parsed.findIndex(isRule);
            const head = ruleAt > 0 ? parsed.slice(0, ruleAt) : [];
            const body = parsed.slice(ruleAt >= 0 ? ruleAt + 1 : 0).filter(r => !isRule(r));

            const cell = (tag, value) => {
                const bold = /^\*\*(.*)\*\*$/.exec(value);
                const inner = bold ? `<strong>${escapeHtml(bold[1])}</strong>` : escapeHtml(value);
                return `<${tag}>${inner}</${tag}>`;
            };

            // A "?" is a cell the paper leaves for you to fill. Make it an input
            // and label it with its own row and column, so a screen reader and a
            // stored key both say which figure it is.
            const workingCell = (rowIndex, colIndex, rowLabel, colLabel) => {
                const key = `${keyBase}:${rowIndex}:${colIndex}`;
                const stored = tableCells[key] || '';
                const label = [rowLabel, colLabel].filter(Boolean).join(', ') || 'working value';
                return `<td class="working"><input class="cell-input" type="text" inputmode="decimal"`
                    + ` autocomplete="off" spellcheck="false" placeholder="?"`
                    + ` style="width:${columnWidth(colIndex)}ch"`
                    + ` data-cell="${escapeHtml(key)}" value="${escapeHtml(stored)}"`
                    + ` aria-label="${escapeHtml(label)}"></td>`;
            };

            // Size each column to its own widest figure plus one character, so an
            // input is only as wide as the number it has to hold. Columns that are
            // all question marks borrow the widest figure in the table, because
            // that is the size of answer they are waiting for.
            const widest = [];
            let widestAnywhere = 0;
            body.forEach(row => row.forEach((value, colIndex) => {
                if (colIndex === 0 || value === '?' || value === '') return;
                const len = value.replace(/\*\*/g, '').length;
                widest[colIndex] = Math.max(widest[colIndex] || 0, len);
                widestAnywhere = Math.max(widestAnywhere, len);
            }));
            const columnWidth = colIndex => {
                const len = widest[colIndex] || widestAnywhere || 8;
                return Math.max(len + 1, 5);
            };

            const headings = head.length ? head[head.length - 1] : [];
            const thead = head.length
                ? `<thead>${head.map(r => `<tr>${r.map(c => cell('th', c)).join('')}</tr>`).join('')}</thead>`
                : '';

            const tbody = `<tbody>${body.map((r, rowIndex) => {
                const blank = r.every(c => c === '');
                const rowLabel = String(r[0] || '').replace(/\*\*/g, '');
                const cells = r.map((c, colIndex) => c === '?'
                    ? workingCell(rowIndex, colIndex, rowLabel, headings[colIndex])
                    : cell('td', c)).join('');
                return `<tr${blank ? ' class="spacer"' : ''}>${cells}</tr>`;
            }).join('')}</tbody>`;

            return `<div class="table-wrap"><table>${thead}${tbody}</table></div>`;
        }

        function escapeHtml(text) {
            return String(text || '')
                .replace(/&/g, '&amp;')
                .replace(/</g, '&lt;')
                .replace(/>/g, '&gt;')
                .replace(/"/g, '&quot;')
                .replace(/'/g, '&#39;');
        }

        function calculateStats() {
            let correct = 0;
            let wrong = 0;
            const answersObj = currentAnswerStore === 'retake' ? retakeAnswers : userAnswers;
            const questions = currentQuestionsData.length ? currentQuestionsData : allQuestionsData;

            questions.forEach(question => {
                const answer = getAnswerForQuestion(question, question.sourceId, currentSourceId, answersObj).value;
                if (!answer || !answer.length) return;

                const correctAnswers = (question.correct_answer || []).map(normalizeOptionText);
                const selectedAnswers = Array.isArray(answer) ? answer : [answer];
                const isMultiChoice = correctAnswers.length > 1;
                const isCorrect = isMultiChoice
                    ? selectedAnswers.slice().sort().join('|') === correctAnswers.slice().sort().join('|')
                    : selectedAnswers[0] === correctAnswers[0];
                if (isCorrect) correct++;
                else if (selectedAnswers.filter(Boolean).length) wrong++;
            });

            const total = correct + wrong;
            const progressTotal = currentQuestionsData.length || allQuestionsData.length;
            document.getElementById('stat-correct').textContent = correct;
            document.getElementById('stat-wrong').textContent = wrong;
            document.getElementById('stat-score').textContent = `${total ? Math.round((correct / total) * 100) : 0}%`;
            document.getElementById('stat-progress').textContent = `${total}/${progressTotal}`;
        }

        function isQuestionWrong(question) {
            const answer = getAnswerForQuestion(question, question.sourceId, currentSourceId, userAnswers).value;
            if (!answer || !answer.length) return false;
            const selectedAnswers = Array.isArray(answer) ? answer : [answer];
            const correctAnswers = (question.correct_answer || []).map(normalizeOptionText);
            return selectedAnswers.slice().sort().join('|') !== correctAnswers.slice().sort().join('|');
        }

        function retakeWrongQuestions() {
            const activeQuestions = currentQuestionsData.length ? currentQuestionsData : allQuestionsData;
            const wrongQuestions = activeQuestions.filter(isQuestionWrong);

            if (!wrongQuestions.length) {
                alert('No wrong answers to retake!');
                return;
            }

            currentMode = 'retake';
            currentAnswerStore = 'retake';
            setRetakeControls(true);
            currentQuestionsData = wrongQuestions;
            currentViewKey = `${currentSourceId}-retake`;
            renderQuestions(wrongQuestions, {
                answerStore: 'retake',
                mode: 'retake',
                sourceId: currentSourceId,
                shouldRestore: true,
                shouldAutoscroll: false
            });
            window.scrollTo({ top: 0, behavior: 'smooth' });
        }

        function returnToMainQuestions() {
            currentAnswerStore = 'main';
            setRetakeControls(false);
            const viewState = getViewState();
            if (viewState && viewState.mode && viewState.mode !== 'retake') {
                if (viewState.mode === 'set') {
                    showSource(viewState.sourceId || SOURCES[0].id, false, viewState.questionIndex || 0);
                    return;
                }
            }
            showSource(currentSourceId || SOURCES[0].id, false, 0);
        }

        function resetProgress() {
            const isRetakeMode = currentMode === 'retake' || currentAnswerStore === 'retake';
            const promptText = isRetakeMode
                ? 'Reset retake progress only? Main progress will stay unchanged.'
                : 'Are you sure you want to reset all progress?';

            if (!confirm(promptText)) return;

            if (isRetakeMode) {
                localStorage.removeItem(RETAKE_ANSWERS_STORAGE_KEY);
                retakeAnswers = {};
                renderQuestions(currentQuestionsData, {
                    answerStore: 'retake',
                    mode: 'retake',
                    sourceId: currentSourceId,
                    shouldRestore: false,
                    shouldAutoscroll: false
                });
                window.scrollTo({ top: 0, behavior: 'smooth' });
                return;
            }

            localStorage.removeItem(ANSWERS_STORAGE_KEY);
            localStorage.removeItem(RETAKE_ANSWERS_STORAGE_KEY);
            localStorage.removeItem(TABLE_CELLS_STORAGE_KEY);
            clearViewState();
            userAnswers = {};
            retakeAnswers = {};
            tableCells = {};
            currentMode = 'set';
            currentAnswerStore = 'main';
            showSource(currentSourceId || SOURCES[0].id, false, 0);
        }

        function scrollToTop() {
            window.scrollTo({ top: 0, behavior: 'smooth' });
        }

        function goToNextSource() {
            if (currentMode !== 'set') return;
            const currentIndex = SOURCES.findIndex(source => source.id === currentSourceId);
            if (currentIndex >= 0 && currentIndex < SOURCES.length - 1) {
                showSource(SOURCES[currentIndex + 1].id, true, 0);
            }
        }

        // Jump to a question at random. Unanswered ones come first, so the button
        // stays useful late in a run instead of landing on work already done.
        // Once everything is answered it falls back to the whole set.
        function jumpToRandomQuestion() {
            const total = currentQuestionsData.length;
            if (!total) return;

            const answers = currentAnswerStore === 'retake' ? retakeAnswers : userAnswers;
            const unanswered = [];
            currentQuestionsData.forEach((question, index) => {
                const effectiveSourceId = currentSourceId === 'all' || currentSourceId === 'random'
                    ? question.sourceId
                    : currentSourceId;
                const stored = getAnswerForQuestion(question, effectiveSourceId, currentSourceId, answers);
                if (stored.value === undefined || stored.value === null) unanswered.push(index);
            });

            const pool = unanswered.length ? unanswered : currentQuestionsData.map((_, i) => i);
            let index = pool[Math.floor(Math.random() * pool.length)];
            // Do not land on the card already in front of you when there is a choice.
            if (pool.length > 1 && index === lastRandomIndex) {
                index = pool[(pool.indexOf(index) + 1) % pool.length];
            }
            lastRandomIndex = index;

            const card = document.getElementById(`q-${index}`);
            if (!card) return;
            card.scrollIntoView({ behavior: 'smooth', block: 'center' });
            card.classList.remove('flash');
            void card.offsetWidth;          // restart the animation
            card.classList.add('flash');
            saveViewState(index);
        }

        // One delegated listener covers every table cell, including the cards
        // that are rebuilt when you change source or start a retake.
        document.addEventListener('input', event => {
            const input = event.target.closest('.cell-input');
            if (!input) return;
            setTableCell(input.dataset.cell, input.value);
            syncTableCell(input.dataset.cell, input.value, input);
        });

        // Enter moves down the column instead of submitting anything.
        document.addEventListener('keydown', event => {
            if (event.key !== 'Enter') return;
            const input = event.target.closest('.cell-input');
            if (!input) return;
            event.preventDefault();
            const inputs = Array.from(document.querySelectorAll('.cell-input'));
            const next = inputs[inputs.indexOf(input) + 1];
            if (next) next.focus();
            else input.blur();
        });

        window.addEventListener('load', loadQuestionBanks);
    