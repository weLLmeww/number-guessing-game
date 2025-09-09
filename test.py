from random import randint


def select_difficulty():

    print("Please select the difficulty level: \n\
    1. Easy (10 chances)\n\
    2. Medium (5 chances) \n\
    3. Hard (3 chances)\n")

    while True:
        try:
            print("Enter your choice:", end=' ')
            diff_choice = int(input())

            match diff_choice:
                case 1: 
                    chances = 10
                    diff_level = 'Easy'
                case 2: 
                    chances = 5
                    diff_level = 'Medium'
                case 3: 
                    chances = 3
                    diff_level = 'Hard'
                case _: 
                    print("Incorrect choice. Please enter 1, 2, or 3.")
                    continue

            print(f"\nGreat! You have selected the   {diff_level} difficulty level.")
            return chances
        
        except ValueError:
            print("Invalid input. Please enter a number (1, 2, or 3).")

def is_guessed(number: int, user_input: int) -> bool:

    if number < user_input:
        print(f'Incorrect! The number is less than {user_input}.')
        return False
    elif number > user_input:
        print(f'Incorrect! The number is greater than {user_input}.')
        return False
    else:
        return True

def get_user_guess():
    """Безопасное получение числа от пользователя"""
    while True:
        try:
            print("\nEnter your guess:", end=' ')
            return int(input().strip())
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 100.")

def main():
    
    number = randint(1, 100)

    print("Welcome to the Number Guessing Game!\n\
          I'm thinking of a number between 1 and 100.\n\
          You have 5 chances to guess the correct number.\n")

    chances = select_difficulty()
    print("Let's start the game!")


    if chances:
        for attempt in range(1, chances+1):
            
            user_input = get_user_guess()
            left = chances - attempt
            

            if not is_guessed(number, user_input):
                print("Attempts left:", left)
                if left == 0:
                    print(f"\nGame over! The number was {number}. Better luck next time!")
                    return

            else:
                print(f"Congratulations! You guessed the correct number in {attempt} attempts.")
                return

if __name__ == '__main__':
    main()