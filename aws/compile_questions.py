import json
import re
import requests

def fetch_and_parse_exam(exam_number):
    """Fetch and parse a single AWS practice exam from GitHub"""
    url = f"https://raw.githubusercontent.com/kananinirav/AWS-Certified-Cloud-Practitioner-Notes/master/practice-exam/practice-exam-{exam_number}.md"
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        content = response.text
    except Exception as e:
        print(f"Error fetching exam {exam_number}: {e}")
        return []
    
    questions = []
    
    # Split by question pattern: number followed by dot and space
    # Look for patterns like "1. " or "10. " at the start of a line
    question_pattern = r'^(\d+)\.\s+(.+?)(?=^\d+\.\s|\Z)'
    matches = re.finditer(question_pattern, content, re.MULTILINE | re.DOTALL)
    
    for match in matches:
        q_num = int(match.group(1))
        q_block = match.group(2).strip()
        
        # Extract question text (first line or up to first option)
        lines = q_block.split('\n')
        
        # Find where options start (lines starting with - A., - B., etc or ◦)
        q_text_lines = []
        option_lines = []
        in_options = False
        
        for line in lines:
            line_stripped = line.strip()
            if re.match(r'^[-◦]\s*[A-E]\.\s*', line_stripped):
                in_options = True
            
            if not in_options and line_stripped and not line_stripped.startswith('---'):
                q_text_lines.append(line_stripped)
            elif in_options:
                option_lines.append(line_stripped)
        
        question_text = ' '.join(q_text_lines)
        
        # Parse options
        options = []
        for line in option_lines:
            # Match options like "- A. text" or "◦ A. text"
            option_match = re.match(r'^[-◦]\s*([A-E])\.\s*(.+?)$', line)
            if option_match:
                options.append(option_match.group(2))
        
        # Extract correct answers from <details> tag (case-insensitive and handle various formats)
        details_match = re.search(r'Correct answer:\s*([A-E](?:,\s*[A-E])*)', q_block, re.IGNORECASE)
        correct_answers = []
        if details_match:
            correct_answers_str = details_match.group(1)
            # Split by comma to get all correct answers
            answer_letters = [ans.strip().upper() for ans in correct_answers_str.split(',')]
            # Convert letters to option texts
            for letter in answer_letters:
                letter_idx = ord(letter) - ord('A')
                if 0 <= letter_idx < len(options):
                    correct_answers.append(options[letter_idx])
        
        if question_text and options and len(options) >= 2:
            questions.append({
                "question_number": q_num + (exam_number - 1) * 50,  # Global question number
                "exam_number": exam_number,
                "question_text": question_text,
                "options": options,
                "correct_answers": correct_answers if correct_answers else None,
                "is_multiple_choice": len(correct_answers) > 1,
                "original_file": f"practice-exam-{exam_number}.md"
            })
    
    return questions

def main():
    all_questions = []
    total_exams = 23  # Based on the GitHub repo
    
    print("Fetching AWS Practice Exams from GitHub...")
    for exam_num in range(1, total_exams + 1):
        print(f"Processing exam {exam_num}...", end=" ")
        exam_questions = fetch_and_parse_exam(exam_num)
        all_questions.extend(exam_questions)
        print(f"Found {len(exam_questions)} questions")
    
    # Save to JSON
    with open('compiled.json', 'w', encoding='utf-8') as f:
        json.dump(all_questions, f, indent=2, ensure_ascii=False)
    
    print(f"\nTotal questions compiled: {len(all_questions)}")
    print("Saved to compiled.json")

if __name__ == "__main__":
    main()
