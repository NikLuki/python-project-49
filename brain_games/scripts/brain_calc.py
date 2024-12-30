import random


def get_random_expression():
    operations = ['+', '-', '*']
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    operation = random.choice(operations)
    expression = f"{num1} {operation} {num2}"
    return expression, eval(expression)


def main():
    print('Welcome to the Brain Games!')
    name = input('May I have your name? ')
    print(f'Hello, {name}!')
    print('What is the result of the expression?')
    
    rounds = 3
    for _ in range(rounds):
        expression, correct_answer = get_random_expression()
        print(f"Question: {expression}")
        answer = input("Your answer: ")
        
        if str(answer) != str(correct_answer):
            print(
                f"'{answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            return
        
        print("Correct!")
    
    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
