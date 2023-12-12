import random


def guess(num_comp, attempts):
    # Checks the attempts
    if attempts == 0:
        print("You don't have more attempts.")
        # If the user have more than 1 attempts
    else:
        print(f"You have {attempts} attempts remaining to guess the number.")
        num = int(input("Enter a number between 1 and 100: "))
        if num_comp == num:
            print(f"Congratulations! The number is {num_comp}")
        # The user pass the number
        elif num_comp < num:
            attempts -= 1
            print("Too high")
            guess(num_comp, attempts)
            # The user lack the number
        elif num_comp > num:
            attempts -= 1
            print("Too low")
            guess(num_comp, attempts)


# Number Guessing Game Objectives:
print("Welcome to Number Guessing Game:")
level = input("Enter difficulty level 'easy' or 'hard':").lower()
num_comp = random.randint(1, 100)
# print(num_comp)

if level == "easy":
    attempts = 10
    guess(num_comp, attempts)
elif level == "hard":
    attempts = 5
    guess(num_comp, attempts)
else:
    print("You have entered an invalid")
