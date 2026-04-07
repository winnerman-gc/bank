import json
import hashlib
import os
import re

def clean_text(text):
    if not text:
        return ""
    # Remove common grading artifacts
    text = text.replace('Mark 1.00 out of 1.00', '').strip()
    
    # Fix fragmented dashes (e.g., "SHA- 2" -> "SHA-2", "connection- oriented" -> "connection-oriented")
    text = re.sub(r'-\s+', '-', text)
    
    # Fix missing answer placeholder dashes (e.g. "The ____ is a" where some might have weird spacing or count)
    # This specifically looks for instances where a word might be missing a dash if that was the user's intent, 
    # but based on the request "answer placeholder dashes", assuming you want to ensure they exist.
    # If the JSONs came from a system that stripped them, we can't guess where they were easily 
    # unless there is a specific pattern like triple spaces or "   ".
    
    return text

def get_question_hash(question):
    # Normalize question text (lowercase, strip whitespace, remove grading artifacts)
    text = clean_text(question.get('question_text', ''))
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
                        q['question_text'] = clean_text(q['question_text'])
                    
                    # Also clean options and correct answer to fix fragmented dashes there
                    if 'options' in q:
                        q['options'] = [clean_text(opt) for opt in q['options']]
                    if 'correct_answer' in q:
                        q['correct_answer'] = clean_text(q['correct_answer'])
                    
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
