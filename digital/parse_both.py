import zipfile
import xml.etree.ElementTree as ET
import re

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

# Extract questions
questions_pars = extract_paragraphs("questions.docx")
answers_pars = extract_paragraphs("answersplusexplanation.docx")

# Parse questions
print("=== Parsing questions.docx ===")
questions = []
current_q = None
current_option_idx = None

question_re = re.compile(r"^(\d+)\.\s+(.+)$")
option_re = re.compile(r"^[a-d]\)\s+(.+)$", re.IGNORECASE)

for line in questions_pars:
    qm = question_re.match(line)
    if qm:
        if current_q and len(current_q["options"]) >= 2:
            questions.append(current_q)
        current_q = {
            "question_number": int(qm.group(1)),
            "question_text": normalize_whitespace(qm.group(2)),
            "options": [],
            "correct_answer": "",
            "working": ""
        }
        current_option_idx = None
        continue
    
    if current_q is None:
        continue
    
    om = option_re.match(line)
    if om:
        current_q["options"].append(normalize_whitespace(om.group(1)))
        current_option_idx = len(current_q["options"]) - 1
        continue
    
    # Append continuation to question or last option
    if current_option_idx is not None and not current_q.get("correct_answer"):
        current_q["options"][current_option_idx] = normalize_whitespace(
            current_q["options"][current_option_idx] + " " + line
        )
    elif not current_q.get("correct_answer"):
        current_q["question_text"] = normalize_whitespace(current_q["question_text"] + " " + line)

if current_q and len(current_q["options"]) >= 2:
    questions.append(current_q)

print(f"Parsed {len(questions)} questions")
for i, q in enumerate(questions[:5]):
    print(f"\nQ{q['question_number']}: {q['question_text'][:60]}...")
    for j, opt in enumerate(q["options"]):
        print(f"  {chr(97+j)}) {opt[:50]}...")

# Now parse answers
print("\n\n=== Parsing answers ===")
answer_re = re.compile(r"^Answer\s*:\s*(.+)$", re.IGNORECASE)

answers = []
for line in answers_pars:
    am = answer_re.match(line)
    if am:
        answer_text = normalize_whitespace(am.group(1))
        answers.append(answer_text)
        print(f"Answer {len(answers)}: {answer_text[:70]}")

print(f"\nTotal answers found: {len(answers)}")

# Try to match
print(f"\nMatching: {len(questions)} questions with {len(answers)} answers")

if len(questions) == len(answers):
    print("✓ Count matches!")
    for i, (q, a) in enumerate(zip(questions[:3], answers[:3])):
        print(f"\nQ{i+1}: {q['question_text'][:50]}...")
        print(f"Answer: {a[:70]}")
else:
    print(f"✗ Mismatch: {len(questions)} questions vs {len(answers)} answers")
