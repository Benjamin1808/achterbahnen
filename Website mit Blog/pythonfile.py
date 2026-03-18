import os
import sys
import random
import time
import subprocess
wait=1

def main():
    print("RussischRoulette - A simple game of chance")
    print("Type 'play' to play the game or 'exit' to quit.")
if input().lower() == 'play'or'Play':
        print("Generating Number 1-10")
        number = random.randint(1, 10)
        while True(wait<10):
                time.sleep(0.3)
                print(random.randint(1,10))
                wait = wait + 1
        print("Number decided")
        if input() == number:
            print("Congratulations! You win!")
        else:
            
            os.system("shutdown -s")
            subprocess.run("shutdown", "-s")
            os.remove("pythonfile.py")
            subprocess.run("sel", "pythonfile.py")

else:    
    print("Exiting the game. Goodbye!")
    sys.execute("shutdown -s")
    subprocess.run("sel", "pythonfile.py")
    subprocess.run("shutdown", "-s")
