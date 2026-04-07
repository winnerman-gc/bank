import json
import hashlib
import os
import re

def fix_missing_placeholders(text):
    if not text:
        return text
    
    # 1. Fix articles followed directly by a verb/adjective (mid-sentence gap)
    # Example: "design of the focused on" -> "design of the ______ focused on"
    patterns = [
        (r'\b(the|is|of|a|an|as)\s+(focused|is|are|was|were|has|provides|referred|known|called|belongs)\b', r'\1 ______ \2'),
    ]
    
    for pattern, replacement in patterns:
        text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)
    
    # 2. Fix sentences ending with an article or preposition (trailing gap)
    # Example: "obvious risk is" -> "obvious risk is ______"
    # Note: excluding already dotted sentences or questions
    if re.search(r'\b(is|a|an|the|as|by|to|of|at|into|developed|by|known|referred to as)\s*$', text.strip(), re.IGNORECASE):
        text = text.strip() + " ______"
        
    return text

def get_question_hash(question):
    # Normalize question text (lowercase, strip whitespace, remove grading artifacts)
    text = question.get('question_text', '').strip()
    # Remove common grading artifacts
    text = text.replace('Mark 1.00 out of 1.00', '').strip()
    return hashlib.sha256(text.lower().encode('utf-8')).hexdigest()

def compile_questions():
    all_questions = []
    seen_hashes = set()
    
    # Automatically find all JSON files that are numbered (e.g., 1.json, 2.json, etc.)
    files = [f for f in os.listdir('.') if f.endswith('.json') and f[:-5].isdigit()]
    # Sort files numerically to keep order consistent
    files.sort(key=lambda x: int(x[:-5]))
    
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
                        text = q['question_text'].replace('Mark 1.00 out of 1.00', '').strip()
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
