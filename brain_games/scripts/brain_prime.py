import random
from brain_games.engine import run_game


def is_prime(n):
    # Проверяет, является ли число простым
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def generate_question():
    # Создает вопрос и правильный ответ
    number = random.randint(1, 100)
    # Генерация случайного числа от 1 до 100
    correct_answer = 'yes' if is_prime(number) else 'no'
    return str(number), correct_answer


def game_logic():
    return {
        'instructions': (
            'Answer "yes" if given number is prime. '
            'Otherwise answer "no".'
        ),
        'get_question_and_answer': generate_question
    }


def main():
    run_game(game_logic())


if __name__ == "__main__":
    main()
