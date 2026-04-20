import zipfile
import xml.etree.ElementTree as ET

W_NS = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"

docx_files = ["questions.docx", "answersplusexplanation.docx"]

for docx_file in docx_files:
    print(f"\n=== {docx_file} ===")
    try:
        with zipfile.ZipFile(docx_file, "r") as zf:
            xml_data = zf.read("word/document.xml")
        
        root = ET.fromstring(xml_data)
        for i, p in enumerate(root.iter(f"{W_NS}p")):
            runs = []
            for t in p.iter(f"{W_NS}t"):
                if t.text:
                    runs.append(t.text)
            line = "".join(runs).strip()
            if line:
                print(f"[{i}] {line[:100]}")
                if i >= 20:  # Print first 20 lines
                    print("...")
                    break
    except Exception as e:
        print(f"Error: {e}")
