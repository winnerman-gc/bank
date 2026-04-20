import json
import os
import re
import zipfile
import xml.etree.ElementTree as ET


W_NS = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"


def normalize_whitespace(text):
    return re.sub(r"\s+", " ", str(text or "")).strip()


def normalize_answer_key(text):
    return normalize_whitespace(text).lower().replace(" ", "")


def extract_docx_paragraphs(docx_path):
    with zipfile.ZipFile(docx_path, "r") as zf:
        xml_data = zf.read("word/document.xml")

    root = ET.fromstring(xml_data)
    paragraphs = []
    for p in root.iter(f"{W_NS}p"):
        runs = []
        for t in p.iter(f"{W_NS}t"):
            runs.append(t.text or "")
        line = normalize_whitespace("".join(runs))
        if line:
            paragraphs.append(line)
    return paragraphs


def parse_questions(paragraphs, source_name):
    question_re = re.compile(r"^(\d+)\.\s+(.+)$")
    option_re = re.compile(r"^([A-D])[\.)]\s+(.+)$", re.IGNORECASE)
    answer_re = re.compile(r"^ANSWER\s*:\s*([A-D])\s*$", re.IGNORECASE)

    questions = []
    current = None
    current_option_idx = None

    def finalize_current():
        nonlocal current, current_option_idx
        if not current:
            return
        if len(current["options"]) >= 2:
            questions.append(current)
        current = None
        current_option_idx = None

    for raw in paragraphs:
        line = normalize_whitespace(raw)
        if not line:
            continue

        qm = question_re.match(line)
        if qm:
            finalize_current()
            q_num = int(qm.group(1))
            q_text = normalize_whitespace(qm.group(2))
            current = {
                "question_number": q_num,
                "question_text": q_text,
                "options": [],
                "correct_answer": "",
                "working": "",
                "original_file": source_name,
            }
            continue

        if current is None:
            continue

        om = option_re.match(line)
        if om:
            current["options"].append(normalize_whitespace(om.group(2)))
            current_option_idx = len(current["options"]) - 1
            continue

        am = answer_re.match(line)
        if am:
            answer_letter = am.group(1).upper()
            idx = ord(answer_letter) - ord("A")
            if 0 <= idx < len(current["options"]):
                current["correct_answer"] = current["options"][idx]
            continue

        if current_option_idx is not None and not current.get("correct_answer"):
            current["options"][current_option_idx] = normalize_whitespace(
                current["options"][current_option_idx] + " " + line
            )
        elif not current.get("correct_answer"):
            current["question_text"] = normalize_whitespace(current["question_text"] + " " + line)

    finalize_current()

    for i, q in enumerate(questions, 1):
        q["question_number"] = i

    return questions


def parse_working_sections(paragraphs):
    question_re = re.compile(r"^Q(\d+)$", re.IGNORECASE)
    working_re = re.compile(r"^Working\s*:\s*$", re.IGNORECASE)
    answer_re = re.compile(r"^✓?\s*Answer\s*:\s*(.+)$", re.IGNORECASE)

    sections = {}
    current_number = None
    collecting = False
    current_lines = []
    current_answer = ""

    def finalize_current():
        nonlocal current_number, collecting, current_lines, current_answer
        if current_number is None:
            return
        sections[current_number] = {
            "working": "\n".join(current_lines).strip(),
            "correct_answer": current_answer.strip(),
        }
        current_number = None
        collecting = False
        current_lines = []
        current_answer = ""

    for raw in paragraphs:
        line = normalize_whitespace(raw)
        if not line:
            continue

        qm = question_re.match(line)
        if qm:
            finalize_current()
            current_number = int(qm.group(1))
            collecting = False
            current_lines = []
            continue

        if current_number is None:
            continue

        if working_re.match(line):
            collecting = True
            continue

        am = answer_re.match(line)
        if am:
            collecting = False
            current_answer = normalize_whitespace(am.group(1))
            current_answer = re.sub(r"^[A-D][\.)]\s*", "", current_answer, flags=re.IGNORECASE)
            continue

        if collecting:
            current_lines.append(line)

    finalize_current()
    return sections


def parse_answer_docx_blocks(paragraphs):
    question_re = re.compile(r"^Q(\d+)$", re.IGNORECASE)
    working_re = re.compile(r"^Working\s*:\s*$", re.IGNORECASE)
    answer_re = re.compile(
        r"^✓?\s*Answer\s*:\s*(?:(?P<letter>[A-D])(?:[\.)])?\s*)?(?P<text>.*)$",
        re.IGNORECASE,
    )

    blocks = {}
    current_number = None
    current_lines = []

    def finalize_current():
        nonlocal current_number, current_lines
        if current_number is None:
            return

        question_text = ""
        working_lines = []
        last_answer_letter = ""
        last_answer_text = ""
        collecting_working = False

        for line in current_lines:
            if not question_text:
                question_text = line
                continue

            if working_re.match(line):
                collecting_working = True
                continue

            answer_match = answer_re.match(line)
            if answer_match:
                collecting_working = False
                last_answer_letter = (answer_match.group("letter") or "").upper()
                last_answer_text = normalize_whitespace(answer_match.group("text"))
                last_answer_text = re.split(r"\b(?:Examiner|Author)\s*:\s*", last_answer_text, maxsplit=1)[0].strip()
                continue

            if collecting_working:
                working_lines.append(line)

        blocks[current_number] = {
            "question_text": question_text,
            "working": "\n".join(working_lines).strip(),
            "answer_letter": last_answer_letter,
            "answer_text": last_answer_text,
        }
        current_number = None
        current_lines = []

    for raw in paragraphs:
        line = normalize_whitespace(raw)
        if not line:
            continue

        qm = question_re.match(line)
        if qm:
            finalize_current()
            current_number = int(qm.group(1))
            current_lines = []
            continue

        if current_number is None:
            continue

        current_lines.append(line)

    finalize_current()
    return blocks


def resolve_answer_text(answer_text, options):
    if not answer_text:
        return ""

    target = normalize_answer_key(answer_text)
    normalized_options = [(option, normalize_answer_key(option)) for option in options]

    for option, key in normalized_options:
        if key == target:
            return option

    for option, key in normalized_options:
        if key and key in target:
            return option

    return answer_text


def compile_questions():
    folder = os.path.dirname(__file__)
    questions_docx = os.path.join(folder, "questions.docx")
    answers_docx = os.path.join(folder, "answersplusexplanation.docx")

    questions = parse_questions(extract_docx_paragraphs(questions_docx), os.path.basename(questions_docx))
    working_sections = parse_working_sections(extract_docx_paragraphs(answers_docx))
    answer_blocks = parse_answer_docx_blocks(extract_docx_paragraphs(answers_docx))

    for question in questions:
        section = answer_blocks.get(question["question_number"], working_sections.get(question["question_number"], {}))
        working = section.get("working", "")
        answer_letter = section.get("answer_letter", "")
        answer_text = section.get("answer_text", "")
        correct_answer = ""
        if answer_letter:
            index = ord(answer_letter.upper()) - ord("A")
            if 0 <= index < len(question["options"]):
                correct_answer = question["options"][index]
        if not correct_answer and answer_text:
            correct_answer = resolve_answer_text(answer_text, question["options"])
        if working:
            question["working"] = working
        if correct_answer:
            question["correct_answer"] = correct_answer

    output_path = os.path.join(folder, "compiled.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(questions, f, indent=2, ensure_ascii=False)

    print(f"Compiled {len(questions)} questions into {output_path}")


if __name__ == "__main__":
    compile_questions()
