# ============================================================
# 4. QUIZ APPLICATION
# ============================================================

def quiz_application():
    """Run a five-question Python quiz."""

    questions = [
        {
            "question": "Which keyword is used to create a function?",
            "answer": "def"
        },
        {
            "question": "Which loop is condition controlled?",
            "answer": "while"
        },
        {
            "question": "Which function gives the length of a list?",
            "answer": "len"
        },
        {
            "question": "Which keyword immediately exits a loop?",
            "answer": "break"
        },
        {
            "question": "Which symbol starts a Python comment?",
            "answer": "#"
        }
    ]

    score = 0

    print("\n--- PYTHON QUIZ ---")

    for item in questions:
        print("\n", item["question"])

        answer = input("Your answer: ").strip().lower()

        if answer == item["answer"].lower():
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")
            print("Correct Answer:", item["answer"])

    percentage = score / len(questions) * 100

    print("\nFinal Score:", score, "/", len(questions))
    print("Percentage:", percentage, "%")


quiz_application()