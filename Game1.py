#Multiple choice questions for the user to choose the correct answer
class Question:
    def __init__(self, prompt, choices, answer):
        self.prompt = prompt
        self.choices = choices
        self.answer = answer

    def display_question(self):
        print(self.prompt)
        for i, choice in enumerate(self.choices):
            print(f"{i + 1}. {choice}")

    def check_answer(self, user_answer):
        return user_answer == self.answer


def play_quiz(questions):
    score = 0
    total_questions = len(questions)

    for question in questions:
        question.display_question()
        user_answer = input("Enter your answer (1, 2, 3, ...): ")
        if question.check_answer(int(user_answer)):
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")
            print("The correct answer is:",
                  question.choices[question.answer - 1])
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
    Question("Where i Codsoft located?", [
             "Brasil", "India", "Spain", "Germany"], 2),
    Question("Which is the best software company?", [
             "Google", "Facebook", "Codsoft", "Twitter"], 3),
    Question("What is the capital of France?", [
             "Paris", "London", "Madrid", "Rome"], 1),
    Question("Who painted the Mona Lisa?", [
             "Vincent van Gogh", "Leonardo da Vinci", "Pablo Picasso", "Claude Monet"], 2),
    Question("What is the largest planet in our solar system?",
             ["Mars", "Jupiter", "Saturn", "Neptune"], 2),
    Question("What is the chemical symbol for gold?",
             ["Cu", "Ag", "Fe", "Au"], 4),
    Question("Which country won the FIFA World Cup in 2022?",
             ["Brazil", "Germany", "France", "Argentina"], 4),
    Question("Which country won the FIFA World Cup in 2018?",
             ["Brazil", "Germany", "France", "Argentina"], 3),
    Question("Which scientist proposed the theory of relativity?", [
             "Isaac Newton", "Albert Einstein", "Galileo Galilei", "Stephen Hawking"], 2),
    Question("What is the national animal of India?", [
             "Elephant", "Tiger", "Lion", "Peacock"], 2),
    Question("What year did World War II end?", [
             "1943", "1945", "1947", "1950"], 2),
    Question("What is the tallest mountain in the world?", [
             "Mount Everest", "K2", "Kangchenjunga", "Makalu"], 1),
    Question("Which musical instrument has 88 keys?", [
             "Violin", "Guitar", "Piano", "Drums"], 3),
]

# Display Welcome Message and Rules
print("Welcome to the Quiz Game!")
print("Answer the following questions by selecting the correct option.")
print()

# Start the Quiz
play_quiz(questions)
