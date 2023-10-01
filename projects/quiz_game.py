# Sample solution for the Python Quiz Game

# 1. Setup & Basic Structure:
questions = [
    {
        "question": "What's the capital of France?",
        "options": ["London", "Berlin", "Paris", "Rome"],
        "answer": "Paris"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Jupiter", "Venus"],
        "answer": "Mars"
    }
    # Additional questions can be added in a similar manner
]

# 2. Displaying Questions & Taking Input:
score = 0
correct_questions = []
incorrect_questions = []

for q in questions:
    print(q["question"])
    for idx, option in enumerate(q["options"], 1):  # This numbers each option for easy selection
        print(f"{idx}. {option}")
    answer = input("Your answer (1/2/3/4): ")

    # 3. Checking Answers & Scoring:
    if q["options"][int(answer) - 1] == q["answer"]:
        score += 1
        correct_questions.append(q["question"])
    else:
        incorrect_questions.append(q["question"])

# 4. Displaying Final Results:
print(f"\nYour final score is: {score}/{len(questions)}")
print("\nQuestions you got right:")
for q in correct_questions:
    print("- " + q)

if incorrect_questions:
    print("\nQuestions you got wrong:")
    for q in incorrect_questions:
        print("- " + q)

# This completes the basic Python Quiz Game. The bonus challenges can be implemented for added complexity.
