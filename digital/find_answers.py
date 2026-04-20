import zipfile
import xml.etree.ElementTree as ET
import re

W_NS = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"

def normalize_whitespace(text):
    return re.sub(r"\s+", " ", str(text or "")).strip()

# Parse answers file looking for answer patterns
print("=== Parsing answersplusexplanation.docx ===")
with zipfile.ZipFile("answersplusexplanation.docx", "r") as zf:
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

# Look for Q1, Q2, Answer patterns
print("\nSearching for answer patterns (after line 50):")
for i, line in enumerate(paragraphs[50:150], start=50):
    if re.match(r"^Q\d+\s*[\.\-]\s*", line, re.IGNORECASE):
        print(f"[{i}] {line[:80]}")
    elif re.match(r"^Answer\s*[\:\-]", line, re.IGNORECASE):
        print(f"[{i}] ANSWER FOUND: {line[:80]}")
    elif re.match(r"^\(?[a-d]\)", line, re.IGNORECASE):
        print(f"[{i}] Option candidate: {line[:80]}")
    elif re.match(r"^Solution|Working|Explanation", line, re.IGNORECASE):
        print(f"[{i}] Solution section: {line[:80]}")

# Search the entire file
print("\n=== Looking for numbered question answers ===")
print("Lines with patterns like '1.', '2.', etc:")
for i, line in enumerate(paragraphs):
    if re.match(r"^(\d+)\.\s+[a-d]\)", line):
        print(f"[{i}] Found answer line: {line}")
        if i < 20:
            continue
        break
