# engine.py

def run_game(game_module):
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    
    print(game_module.DESCRIPTION)
    
    for _ in range(3):
        question, correct_answer = game_module.get_question_and_answer()
        print(f"Question: {question}")
        answer = input("Your answer: ")
        
        if answer == correct_answer:
            print("Correct!")
        else:
            print(
            f"'{answer}' is wrong answer ;(. Correct answer was " 
            f"'{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            return
    
    print(f"Congratulations, {name}!")


