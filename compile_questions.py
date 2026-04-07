import json
import hashlib
import os
import re


def strip_grading_artifacts(text):
    if not text:
        return text
    cleaned = text.strip()
    # Remove quiz grading fragments like "Mark 0.00 out of 1.00" wherever they appear.
    cleaned = re.sub(r'\s*Mark\s+\d+(?:\.\d+)?\s+out\s+of\s+\d+(?:\.\d+)?\s*', ' ', cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r'\s{2,}', ' ', cleaned).strip()
    return cleaned

def fix_missing_placeholders(text):
    if not text:
        return text

    text = text.strip()
    
    # 1. Fix articles followed directly by a verb/adjective (mid-sentence gap)
    # Example: "design of the focused on" -> "design of the ______ focused on"
    patterns = [
        (r'\b(the|is|of|a|an|as)\s+(focused|is|are|was|were|has|provides|referred|known|called|belongs)\b', r'\1 ______ \2'),
        (r'\b(a)\s+(can)\b', r'\1 ______ \2'),
    ]
    
    for pattern, replacement in patterns:
        text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)
    
    # 2. Fix sentences ending with an article or preposition (trailing gap)
    # Example: "obvious risk is" -> "obvious risk is ______"
    # Note: excluding already dotted sentences or questions
    if re.search(r'\b(is|a|an|the|as|by|to|of|at|into|developed|by|known|referred to as)\s*$', text, re.IGNORECASE):
        text = text + " ______"

    # 3. If the first alphabetic character is lowercase, assume missing leading blank.
    first_alpha = re.search(r'[A-Za-z]', text)
    if first_alpha and text[first_alpha.start()].islower() and not text.startswith("______"):
        text = "______ " + text
        
    return text

def get_question_hash(question):
    # Normalize question text (lowercase, strip whitespace, remove grading artifacts)
    text = strip_grading_artifacts(question.get('question_text', ''))
    return hashlib.sha256(text.lower().encode('utf-8')).hexdigest()

def compile_questions():
    all_questions = []
    seen_hashes = set()
    
    # Include numbered JSON files and deepseek_json_*.json files.
    numbered_files = [f for f in os.listdir('.') if f.endswith('.json') and f[:-5].isdigit()]
    deepseek_files = [f for f in os.listdir('.') if re.match(r'^deepseek_json_.*\.json$', f)]

    # Sort numbered files numerically and deepseek files lexicographically.
    numbered_files.sort(key=lambda x: int(x[:-5]))
    deepseek_files.sort()
    files = numbered_files + deepseek_files
    
    for filename in files:
        if not os.path.exists(filename):
            print(f"File {filename} not found, skipping.")
            continue
            
        with open(filename, 'r', encoding='utf-8') as f:
            try:
                questions = json.load(f)
                for q in questions:
                    # Clean the question text in the actual object
                    if 'question_text' in q:
                        text = strip_grading_artifacts(q['question_text'])
                        q['question_text'] = fix_missing_placeholders(text)
                    
                    q_hash = get_question_hash(q)
                    if q_hash not in seen_hashes:
                        seen_hashes.add(q_hash)
                        # Re-number questions sequentially in the compiled list
                        q['original_file'] = filename
                        all_questions.append(q)
            except json.JSONDecodeError:
                print(f"Error decoding {filename}")

    # Renumber questions for the final list
    for i, q in enumerate(all_questions, 1):
        q['question_number'] = i

    with open('compiled.json', 'w', encoding='utf-8') as f:
        json.dump(all_questions, f, indent=2, ensure_ascii=False)
    
    print(f"Compiled {len(all_questions)} unique questions into compiled.json")

if __name__ == "__main__":
    compile_questions()
