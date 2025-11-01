import random

EASY_LEVEL = 10
HARD_LEVEL = 5


#function to check user's guess against actual answer
def check_answer(user_guess, answer, attempts):
    """check answer against the guessed and return the numer of turns"""
    if user_guess > answer:
        print("too high")
        return attempts - 1
    elif user_guess < answer:
        print("too low")
        return attempts -1
    else:
        print(f"you got it! the answer was {answer}")


#function to set the difficulty
def set_difficulty():
    level = input("choose a difficult. type 'easy' or 'hard': ").lower()
    if level == "easy":  
        return EASY_LEVEL
    else:
        return HARD_LEVEL

def game():
    #user welcome
    print("welcome to the guessig game!")
    print("i am thinking of a number between 1 to 100.")

    #choosing a random number
    random_number = random.randint(1, 100)

    attempts = set_difficulty()


    #repeat the guessing functionality if they get it wrong
    user_guess = 0
    while user_guess != random_number:
        print(f"you have {attempts} attempts reamining to guess the number.")

        #let the user guess the number
        user_guess = int(input("Make a guess: "))

        #track the number of turns and reduce by 1 if they get it wrong
        attempts = check_answer(user_guess, random_number, attempts)

game()