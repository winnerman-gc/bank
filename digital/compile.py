import json
import os
import re
import zipfile
import xml.etree.ElementTree as ET


W_NS = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"


def normalize_whitespace(text):
    return re.sub(r"\s+", " ", str(text or "")).strip()


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


def parse_docx_questions(paragraphs, source_name):
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
        if len(current["options"]) >= 2 and current.get("correct_answer"):
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

        # Preserve multiline content when DOCX wraps long question/option text.
        if current_option_idx is not None and not current.get("correct_answer"):
            current["options"][current_option_idx] = normalize_whitespace(
                current["options"][current_option_idx] + " " + line
            )
        elif not current.get("correct_answer"):
            current["question_text"] = normalize_whitespace(current["question_text"] + " " + line)

    finalize_current()

    # Renumber sequentially for frontend stability.
    for i, q in enumerate(questions, 1):
        q["question_number"] = i

    return questions


def compile_from_docx(docx_path):
    paragraphs = extract_docx_paragraphs(docx_path)
    return parse_docx_questions(paragraphs, os.path.basename(docx_path))


def compile_questions():
    docx_files = sorted([f for f in os.listdir(".") if f.lower().endswith(".docx")])

    if not docx_files:
        print("No DOCX files found in this directory")
        return

    all_questions = []
    for docx_file in docx_files:
        print(f"Compiling: {docx_file}")
        questions = compile_from_docx(docx_file)
        all_questions.extend(questions)

    # Renumber all questions sequentially
    for i, q in enumerate(all_questions, 1):
        q["question_number"] = i

    with open("compiled.json", "w", encoding="utf-8") as f:
        json.dump(all_questions, f, indent=2, ensure_ascii=False)

    print(f"Compiled {len(all_questions)} questions into compiled.json")


if __name__ == "__main__":
    compile_questions()
