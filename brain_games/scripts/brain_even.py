import random

def main():
    print('Welcome to the Brain Games!')
    name = input('May I have your name? ')
    print(f'Hello, {name}!')
    print(f'Answer "yes" if the number is even, otherwise answer "no".')

    correct_answers = 0
    while correct_answers < 3:
        number = random.randint(1, 100)  # Генерация случайного числа
        print(f"Question: {number}")
        answer = input('Your answer: ')

        correct_answer = 'yes' if number % 2 == 0 else 'no'
        
        if answer.lower() == correct_answer:
            print("Correct!")
            correct_answers += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return  # Завершение игры при неправильном ответе

    print(f"Congratulations, {name}!")  # Поздравление при успешной игре
    
if __name__ == '__main__':
    main()

