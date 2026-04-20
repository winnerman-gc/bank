import json
import os
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

# Extract questions from questions.docx
questions_pars = extract_paragraphs("questions.docx")

# Parse questions
questions_dict = {}
current_q = None
current_option_idx = None

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
            "options": [],
            "correct_answer": ""
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
    
    # Append continuation
    if current_option_idx is not None and not current_q.get("correct_answer"):
        current_q["options"][current_option_idx] = normalize_whitespace(
            current_q["options"][current_option_idx] + " " + line
        )
    elif not current_q.get("correct_answer"):
        current_q["question_text"] = normalize_whitespace(current_q["question_text"] + " " + line)

if current_q and len(current_q["options"]) >= 2:
    questions_dict[current_q["number"]] = current_q

print(f"Parsed {len(questions_dict)} questions from questions.docx")

# Extract answers from answersplusexplanation.docx
answers_pars = extract_paragraphs("answersplusexplanation.docx")

# Find answer for each Q# marker
answers_dict = {}
q_marker_re = re.compile(r"^Q(\d+)$", re.IGNORECASE)
answer_re = re.compile(r"^Answer\s*:\s*(.+)$", re.IGNORECASE)

for i, line in enumerate(answers_pars):
    qm = q_marker_re.match(line)
    if qm:
        q_num = int(qm.group(1))
        # Look for "Answer:" within next 100 lines
        for j in range(i+1, min(i+100, len(answers_pars))):
            am = answer_re.match(answers_pars[j])
            if am:
                answer_text = normalize_whitespace(am.group(1))
                answers_dict[q_num] = answer_text
                break

print(f"Found {len(answers_dict)} answers from answersplusexplanation.docx")

# Match questions with answers and build final list
final_questions = []
for q_num in sorted(questions_dict.keys()):
    q = questions_dict[q_num]
    answer_text = answers_dict.get(q_num, "")
    
    if not answer_text:
        print(f"Warning: No answer found for Q{q_num}")
        continue
    
    # Try to map answer text to an option
    # Check if answer starts with a letter (a, b, c, d)
    letter_match = re.match(r"^([a-d])\)", answer_text, re.IGNORECASE)
    if letter_match:
        # Extract just the letter
        letter = letter_match.group(1).lower()
        option_idx = ord(letter) - ord('a')
        if option_idx < len(q["options"]):
            q["correct_answer"] = q["options"][option_idx]
    else:
        # Try to find the answer text in the options
        normalized_answer = normalize_whitespace(answer_text)
        found = False
        for opt in q["options"]:
            if normalize_whitespace(opt.lower()).startswith(normalized_answer.lower()[:30]):
                q["correct_answer"] = opt
                found = True
                break
        if not found:
            # Fallback: use the answer text as-is
            q["correct_answer"] = answer_text
    
    final_questions.append({
        "question_number": q["number"],
        "question_text": q["question_text"],
        "options": q["options"],
        "correct_answer": q["correct_answer"],
        "original_file": "questions.docx + answersplusexplanation.docx"
    })

print(f"Final count: {len(final_questions)} questions with answers")

# Save to compiled.json
with open("compiled.json", "w", encoding="utf-8") as f:
    json.dump(final_questions, f, indent=2, ensure_ascii=False)

print(f"✓ Compiled {len(final_questions)} questions into compiled.json")

# Show first few for verification
print("\nFirst 3 questions:")
for q in final_questions[:3]:
    print(f"\nQ{q['question_number']}: {q['question_text'][:60]}...")
    for i, opt in enumerate(q["options"]):
        mark = "✓" if opt == q["correct_answer"] else " "
        print(f"  {chr(97+i)}) [{mark}] {opt[:50]}...")
