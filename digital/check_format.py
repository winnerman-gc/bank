import zipfile
import xml.etree.ElementTree as ET
import re

W_NS = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"

def normalize_whitespace(text):
    return re.sub(r"\s+", " ", str(text or "")).strip()

# Extract paragraphs
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

# Look for Q1, Q2, etc markers and what comes after
print("Looking for question markers and answers:")
for i, line in enumerate(paragraphs):
    if re.match(r"^Q\d+\b", line, re.IGNORECASE) or re.match(r"^Question\s+\d+", line, re.IGNORECASE):
        print(f"\n[{i}] Found Q marker: {line[:70]}")
        # Print next few lines
        for j in range(1, 4):
            if i+j < len(paragraphs):
                print(f"  [{i+j}] {paragraphs[i+j][:70]}")

# Look for lines starting with letters a, b, c, d that might be answers
print("\n\nLines that look like answer choices:")
count = 0
for i, line in enumerate(paragraphs):
    if re.match(r"^[a-d]\)?\s+(?!.*\d{1,3}\))", line, re.IGNORECASE):
        if count < 10:
            print(f"[{i}] {line[:70]}")
            count += 1

# Search for question numbers like "1.", "2." in answers file
print("\n\nLines starting with question numbers:")
for i, line in enumerate(paragraphs):
    if re.match(r"^\d+\.\s+", line):
        print(f"[{i}] {line[:80]}")
