import random

def main():
    print('Welcome to the Brain Even Game!')
    name = input('May I have your name? ')
    print(f'Hello, {name}!')
    
    rounds = 3
    for _ in range(rounds):
        number = random.randint(1, 100)
        correct_answer = 'yes' if number % 2 == 0 else 'no'
        print(f'Question: {number}')
        answer = input("Your answer (yes/no): ")
        
        if answer == correct_answer:
            print('Correct!')
        else:
            print(f'Wrong! The correct answer was {correct_answer}.')
            break
    else:
        print('Congratulations, you won!')

if __name__ == '__main__':
    main()

