import json
import random
from pathlib import Path

from docx import Document
from docx.shared import Inches, Pt


BASE_DIR = Path(__file__).resolve().parent
SOURCE_FILES = [
    BASE_DIR / "fib_200.json",
    BASE_DIR / "fib_200_generated.json",
]


def load_questions(json_path: Path):
    with json_path.open("r", encoding="utf-8") as file_handle:
        payload = json.load(file_handle)
    return payload["meta"], payload["questions"]


def unique_answers(questions):
    answers = []
    seen = set()
    for question in questions:
        answer = str(question["answer"]).strip()
        key = answer.casefold()
        if key in seen:
            continue
        seen.add(key)
        answers.append(answer)
    return answers


def set_cell_text(cell, text, bold=False):
    cell.text = ""
    paragraph = cell.paragraphs[0]
    run = paragraph.add_run(text)
    run.bold = bold
    paragraph.paragraph_format.space_after = Pt(0)


def build_document(meta, questions, output_path: Path):
    document = Document()

    section = document.sections[0]
    section.top_margin = Inches(0.7)
    section.bottom_margin = Inches(0.7)
    section.left_margin = Inches(0.7)
    section.right_margin = Inches(0.7)

    normal_style = document.styles["Normal"]
    normal_style.font.name = "Calibri"
    normal_style.font.size = Pt(10.5)

    for question in questions:
        question_paragraph = document.add_paragraph(style="Normal")
        question_paragraph.paragraph_format.space_after = Pt(0)
        question_paragraph.add_run(f'{question["id"]}. Q: {question["question"]}')

        answer_paragraph = document.add_paragraph(style="Normal")
        answer_paragraph.paragraph_format.space_after = Pt(6)
        answer_paragraph.add_run(f'A: {question["answer"]}')

    # Add vocabulary bank at end with random mix
    vocab_answers = unique_answers(questions)
    shuffled_vocab = vocab_answers.copy()
    random.shuffle(shuffled_vocab)
    
    # Add spacing before vocab section
    document.add_paragraph()
    
    # Add vocab heading
    vocab_heading = document.add_paragraph(style="Normal")
    vocab_heading.paragraph_format.space_after = Pt(6)
    vocab_run = vocab_heading.add_run("Vocabulary Bank (Random Mix)")
    vocab_run.bold = True
    
    # Add shuffled vocabulary
    for index, answer in enumerate(shuffled_vocab, 1):
        vocab_paragraph = document.add_paragraph(style="Normal")
        vocab_paragraph.paragraph_format.space_after = Pt(0)
        vocab_paragraph.add_run(f"{index}. {answer}")

    document.save(output_path)


def write_vocab_file(questions, output_path: Path):
    answers = unique_answers(questions)
    with output_path.open("w", encoding="utf-8", newline="\n") as file_handle:
        file_handle.write("Vocabulary Bank\n")
        file_handle.write("\n")
        for index, answer in enumerate(answers, 1):
            file_handle.write(f"{index}. {answer}\n")


def main():
    for source_path in SOURCE_FILES:
        if not source_path.exists():
            raise FileNotFoundError(source_path)

        meta, questions = load_questions(source_path)
        output_stem = source_path.with_suffix("")
        docx_path = output_stem.with_suffix(".docx")
        vocab_path = output_stem.with_name(f"{output_stem.name}_vocabulary_bank.txt")

        build_document(meta, questions, docx_path)
        write_vocab_file(questions, vocab_path)
        print(f"Wrote {docx_path.name} and {vocab_path.name}")


if __name__ == "__main__":
    main()