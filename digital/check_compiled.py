import json

# Load and check compiled.json
with open("compiled.json", "r", encoding="utf-8") as f:
    questions = json.load(f)

print(f"Total questions: {len(questions)}\n")

# Check first 5
for q in questions[:5]:
    print(f"Q{q['question_number']}: {q['question_text'][:60]}...")
    print(f"  Correct answer: {q['correct_answer'][:70]}")
    print(f"  Options:")
    for i, opt in enumerate(q["options"]):
        match = "✓" if opt == q["correct_answer"] else ""
        print(f"    {chr(97+i)}) {opt[:60]} {match}")
    print()
