"""
Exercise 13:
 Generate a 1-D array containing 5 random integers from 0 to 20.
 Get input from the user.
 if the user input matches the random number, then
 print "Success" and exit
 else
 print failure and try again. If the number of chances exceeds 3, then exit.
"""
import numpy as np

def guess_number_game(n=5,m=3):
    random_numbers = []

    for i in range(n):
        random_numbers.append(np.random.randint(0, 21))

    random_numbers = np.array(random_numbers)
    print(random_numbers)

    attempts = 0
    max_attempts = m

    while attempts < max_attempts:
        try:
            user_input = int(input("Guess a number between 0 and 20: "))
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue

        if user_input in random_numbers:
            print("Success!")
            break
        else:
            closest_distance = min(abs(user_input - num) for num in random_numbers)

            if closest_distance == 1:
                print("Hot! You're very close!")
            elif closest_distance == 2:
                print("Warm. You're getting closer.")
            else:
                print("Cold. You're far from the correct number.")

        attempts += 1

    if attempts == max_attempts:
        print("You've used all your attempts. Game Over.")
        print(f"The random numbers were: {random_numbers}")

guess_number_game()