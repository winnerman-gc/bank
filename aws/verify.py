import json

with open('compiled.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

total = len(data)
with_answers = sum(1 for q in data if q.get('correct_answers'))
single_answer = sum(1 for q in data if q.get('correct_answers') and len(q.get('correct_answers', [])) == 1)
multiple_answers = sum(1 for q in data if q.get('correct_answers') and len(q.get('correct_answers', [])) > 1)
without_answers = total - with_answers

print(f"Total questions: {total}")
print(f"With answers: {with_answers}")
print(f"  - Single answer: {single_answer}")
print(f"  - Multiple answers: {multiple_answers}")
print(f"Without answers: {without_answers}")

if with_answers > 0:
    sample = next((q for q in data if q.get('correct_answers')), None)
    if sample:
        print(f"\nSample with answer(s):")
        print(f"  Question: {sample['question_text'][:100]}...")
        print(f"  Answers: {sample['correct_answers']}")
        
    multi_sample = next((q for q in data if q.get('correct_answers') and len(q.get('correct_answers', [])) > 1), None)
    if multi_sample:
        print(f"\nSample with multiple answers:")
        print(f"  Question: {multi_sample['question_text'][:100]}...")
        print(f"  Answers: {multi_sample['correct_answers']}")

