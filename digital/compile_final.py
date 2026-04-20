import json
import re
import zipfile
import xml.etree.ElementTree as ET

W_NS = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"

def normalize_whitespace(text):
    return re.sub(r"\s+", " ", str(text or "")).strip()

def extract_paragraphs(docx_path):
    with zipfile.ZipFile(docx_path, "r") as zf:
        xml_data = zf.read("word/document.xml")
    root = ET.fromstring(xml_data)
    paragraphs = []
    for p in root.iter(f"{W_NS}p"):
        runs = []
        for t in p.iter(f"{W_NS}t"):
            if t.text:
                runs.append(t.text)
        line = normalize_whitespace("".join(runs))
        if line:
            paragraphs.append(line)
    return paragraphs

# Parse questions
questions_pars = extract_paragraphs("questions.docx")
questions_dict = {}
current_q = None

question_re = re.compile(r"^(\d+)\.\s+(.+)$")
option_re = re.compile(r"^[a-d]\)\s+(.+)$", re.IGNORECASE)

for line in questions_pars:
    qm = question_re.match(line)
    if qm:
        if current_q and len(current_q["options"]) >= 2:
            questions_dict[current_q["number"]] = current_q
        current_q = {
            "number": int(qm.group(1)),
            "question_text": normalize_whitespace(qm.group(2)),
            "options": []
        }
        continue
    
    if current_q is None:
        continue
    
    om = option_re.match(line)
    if om:
        current_q["options"].append(normalize_whitespace(om.group(1)))
        continue
    
    # Append continuation
    if current_q["options"] and not line.startswith(("Q", "Working", "Answer")):
        current_q["options"][-1] = normalize_whitespace(
            current_q["options"][-1] + " " + line
        )
    elif not current_q["options"]:
        current_q["question_text"] = normalize_whitespace(current_q["question_text"] + " " + line)

if current_q and len(current_q["options"]) >= 2:
    questions_dict[current_q["number"]] = current_q

print(f"Parsed {len(questions_dict)} questions")

# Parse answers - find Q# blocks
answers_pars = extract_paragraphs("answersplusexplanation.docx")
q_answers = {}

# Find each Q# block and extract info
q_block_indices = {}
for i, line in enumerate(answers_pars):
    qm = re.match(r"^Q(\d+)$", line, re.IGNORECASE)
    if qm:
        q_num = int(qm.group(1))
        q_block_indices[q_num] = i

print(f"Found Q markers at: {sorted(q_block_indices.keys())}")

# For each Q block, find the question text within it to verify match, then get answer
answer_re = re.compile(r"^Answer\s*:\s*(.+)$", re.IGNORECASE)

for q_num in sorted(questions_dict.keys()):
    if q_num not in q_block_indices:
        print(f"Warning: No Q{q_num} block found")
        continue
    
    start_idx = q_block_indices[q_num]
    end_idx = q_block_indices.get(q_num + 1, len(answers_pars))
    
    # Look for Answer: within this block
    answer_found = None
    for i in range(start_idx, end_idx):
        am = answer_re.match(answers_pars[i])
        if am:
            answer_found = normalize_whitespace(am.group(1))
            break
    
    if answer_found:
        q_answers[q_num] = answer_found
        print(f"Q{q_num}: {answer_found[:60]}...")
    else:
        print(f"Q{q_num}: NO ANSWER FOUND")

# Match answers to options and build final list
final_questions = []
for q_num in sorted(questions_dict.keys()):
    q = questions_dict[q_num]
    answer_text = q_answers.get(q_num, "")
    
    if not answer_text:
        print(f"Skipping Q{q_num} - no answer")
        continue
    
    # Extract letter if answer is like "a) ..." or "a)"
    letter_match = re.match(r"^([a-d])\)?(?:\s|$)", answer_text, re.IGNORECASE)
    correct_option = ""
    
    if letter_match:
        letter = letter_match.group(1).lower()
        idx = ord(letter) - ord('a')
        if idx < len(q["options"]):
            correct_option = q["options"][idx]
    
    if not correct_option:
        # Try substring matching
        normalized_answer = answer_text.lower()[:40]
        for opt in q["options"]:
            if normalized_answer in opt.lower():
                correct_option = opt
                break
    
    if not correct_option and answer_text:
        correct_option = answer_text
    
    final_questions.append({
        "question_number": q["number"],
        "question_text": q["question_text"],
        "options": q["options"],
        "correct_answer": correct_option,
        "original_file": "questions.docx + answersplusexplanation.docx"
    })

print(f"\n✓ Final: {len(final_questions)} questions")

with open("compiled.json", "w", encoding="utf-8") as f:
    json.dump(final_questions, f, indent=2, ensure_ascii=False)

# Verify first 5
print("\nFirst 5 questions verification:")
for q in final_questions[:5]:
    print(f"\nQ{q['question_number']}: {q['question_text'][:50]}...")
    for i, opt in enumerate(q["options"]):
        mark = "✓" if opt == q["correct_answer"] else " "
        print(f"  {chr(97+i)}) [{mark}] {opt[:45]}...")
