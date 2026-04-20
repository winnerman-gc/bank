import zipfile
import xml.etree.ElementTree as ET
import re

W_NS = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"

def normalize_whitespace(text):
    return re.sub(r"\s+", " ", str(text or "")).strip()

# Check questions.docx structure
print("=== Searching questions.docx for patterns ===")
with zipfile.ZipFile("questions.docx", "r") as zf:
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

# Look for answer patterns in both files
print("\nLooking for patterns in questions.docx:")
question_re = re.compile(r"^(\d+)\.\s+(.+)$")
option_re_lower = re.compile(r"^[a-d]\)\s+(.+)$", re.IGNORECASE)
answer_re = re.compile(r"^answer\s*:\s*([a-d])\s*$", re.IGNORECASE)

question_count = 0
for i, line in enumerate(paragraphs[:100]):
    if question_re.match(line):
        question_count += 1
        print(f"Q{question_count}: {line[:70]}")
    if option_re_lower.match(line):
        print(f"  Option: {line[:70]}")
    if answer_re.match(line):
        print(f"  FOUND ANSWER: {line}")

print(f"\nFound {question_count} questions in first 100 lines")

# Check answers file
print("\n=== Searching answersplusexplanation.docx ===")
with zipfile.ZipFile("answersplusexplanation.docx", "r") as zf:
    xml_data = zf.read("word/document.xml")

root = ET.fromstring(xml_data)
paragraphs2 = []
for p in root.iter(f"{W_NS}p"):
    runs = []
    for t in p.iter(f"{W_NS}t"):
        if t.text:
            runs.append(t.text)
    line = normalize_whitespace("".join(runs))
    if line:
        paragraphs2.append(line)

answer_count = 0
for i, line in enumerate(paragraphs2):
    if answer_re.match(line):
        answer_count += 1
        print(f"Answer {answer_count}: {line}")
        if answer_count >= 5:
            break

if answer_count == 0:
    print("No 'ANSWER: X' pattern found")
    print("\nFirst 30 lines of answers file:")
    for line in paragraphs2[:30]:
        print(f"  {line[:80]}")
