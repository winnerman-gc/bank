import json
import hashlib
import os

def get_question_hash(question):
    # Normalize question text (lowercase, strip whitespace)
    text = question.get('question_text', '').strip().lower()
    return hashlib.sha256(text.encode('utf-8')).hexdigest()

def compile_questions():
    all_questions = []
    seen_hashes = set()
    
    files = [f'{i}.json' for i in range(1, 7)]
    
    for filename in files:
        if not os.path.exists(filename):
            print(f"File {filename} not found, skipping.")
            continue
            
        with open(filename, 'r', encoding='utf-8') as f:
            try:
                questions = json.load(f)
                for q in questions:
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
