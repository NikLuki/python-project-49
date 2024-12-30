import random
import math
from brain_games.engine import run_game


def get_question_and_answer():
    number1 = random.randint(1, 100)  # Генерация первого случайного числа
    number2 = random.randint(1, 100)  # Генерация второго случайного числа
    correct_answer = str(math.gcd(number1, number2))
    return f"{number1} {number2}", correct_answer


def main():
    game_logic = {
        'instructions': 'Find the greatest common divisor of given numbers.',
        'get_question_and_answer': get_question_and_answer
    }
    run_game(game_logic)


if __name__ == '__main__':
    main()
