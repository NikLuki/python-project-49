import random

DESCRIPTION = 'What is the result of the expression?'

def get_random_expression():
    operations = ['+', '-', '*']
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    operation = random.choice(operations)
    expression = f"{num1} {operation} {num2}"
    return expression, eval(expression)

def get_question_and_answer():
    expression, correct_answer = get_random_expression()
    return expression, str(correct_answer)
