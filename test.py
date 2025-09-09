from random import randint


def select_difficulty():
    print("Please select the difficulty level: \n\
    1. Easy (10 chances)\n\
    2. Medium (5 chances) \n\
    3. Hard (3 chances)\n")
    while True:
        print("Enter your choice:", end=' ')
        diff_choise = int(input())

        match diff_choise:
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
                print("Incorrect choice, try again.")
                continue

        print(f"\nGreat! You have selected the {diff_level} difficulty level.")
        return chances


def is_quessed(number: int, user_input: int) -> bool:
    if number < user_input:
        print(f'Incorrect! The number is less than {user_input}.')
        return False
    elif number > user_input:
        print(f'Incorrect! The number is greater than {user_input}.')
        return False
    else:
        return True

def main():
    
    attempt = 0
    number = randint(1, 100)

    print("Welcome to the Number Guessing Game!\n\
          I'm thinking of a number between 1 and 100.\n\
          You have 5 chances to guess the correct number.\n")

    chances = select_difficulty()
    print("Let's start the game!")


    if chances:
        for _ in range(0, chances):

            print("\nEnter your guess:", end=' ' )
            user_input = int(input())

            attempt += 1
            left = chances - attempt
            

            if not is_quessed(number, user_input):
                print("Attempts left:", left)
                if left == 0:
                    print("\nNah, You lost! Try again.")

            else:
                print(f"Congratulations! You guessed the correct number in {attempt} attempts.")

if __name__ == '__main__':
    main()