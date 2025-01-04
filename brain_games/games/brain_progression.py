import random

DESCRIPTION = "What number is missing in the progression?"


def get_question_and_answer():
    length = random.randint(5, 10)
    start = random.randint(1, 20)
    step = random.randint(1, 5)
    progression = [start + i * step for i in range(length)]

    hidden_index = random.randint(0, length - 1)
    hidden_value = progression[hidden_index]

    progression[hidden_index] = '..'

    return ' '.join(map(str, progression)), str(hidden_value)
