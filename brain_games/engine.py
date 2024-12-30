# engine.py

def welcome_user():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    return name


def ask_question(question):
    print(f"Question: {question}")
    return input("Your answer: ")


def check_answer(user_answer, correct_answer, name):
    if user_answer == correct_answer:
        print("Correct!")
        return True
    else:
        print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
        print(f"Let's try again, {name}!")
        return False


def run_game(game_logic):
    name = welcome_user()
    print(game_logic['instructions'])

    for _ in range(3):  # Максимальное количество раундов
        question, correct_answer = game_logic['get_question_and_answer']()
        user_answer = ask_question(question)

        if not check_answer(user_answer, correct_answer, name):
            return

    print(f"Congratulations, {name}!")


