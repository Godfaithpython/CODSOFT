# Structural questions for the user to input the correct answer
class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

    def display_question(self):
        print(self.prompt)

    def check_answer(self, user_answer):
        return user_answer.lower() == self.answer.lower()


def play_quiz(questions):
    score = 0
    total_questions = len(questions)

    for question in questions:
        question.display_question()
        user_answer = input("Enter your answer: ")
        if question.check_answer(user_answer):
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")
            print("The correct answer is:", question.answer)
        print()

    final_score = int((score / total_questions) * 100)
    print("Quiz completed!")
    print(f"Your score: {score}/{total_questions}")
    print(f"Your performance: {final_score}%")

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == "yes":
        play_quiz(questions)
    else:
        print("Thank you for playing!")


# Load Quiz Questions
questions = [
    Question("Who is the world best player?", "Messi"),
    Question("Which football player has the most ballon d'or?", "Messi"),
    Question("What is the capital of France?", "Paris"),
    Question("Who painted the Mona Lisa?", "Leonardo da Vinci"),
    Question("What is the largest planet in our solar system?", "Jupiter"),
    Question("What is the chemical symbol for gold?", "Au"),
    Question("Which country won the FIFA World Cup in 2018?", "France"),
    Question("Which country won the FIFA World Cup in 2022?", "Argentina"),
    Question("Which scientist proposed the theory of relativity?",
             "Albert Einstein"),
    Question("What is the national animal of India?", "Tiger"),
    Question("What year did World War II end?", "1945"),
    Question("What is the tallest mountain in the world?", "Mount Everest"),
    Question("Which musical instrument has 88 keys?", "Piano"),
]

# Display Welcome Message and Rules
print("Welcome to the Quiz Game!")
print("Answer the following questions by typing your answer.")
print()

# Start the Quiz
play_quiz(questions)
