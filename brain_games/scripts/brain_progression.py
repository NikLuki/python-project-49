import random
from brain_games.engine import run_game


def generate_progression():
    length = random.randint(5, 10)  # Генерация длины прогрессии от 5 до 10
    start = random.randint(1, 20)    # Начальное число
    step = random.randint(1, 5)      # Шаг прогрессии
    progression = [start + i * step for i in range(length)]

    # Случайно выбираем позицию для замены
    hidden_index = random.randint(0, length - 1)
    hidden_value = progression[hidden_index]

    progression[hidden_index] = '..'  # Заменяем скрытое значение на '..'

    return ' '.join(map(str, progression)), str(hidden_value)


def game_logic():
    return {
        'instructions': "What number is missing in the progression?",
        'get_question_and_answer': generate_progression
    }


def main():
    run_game(game_logic())


if __name__ == "__main__":
    main()
