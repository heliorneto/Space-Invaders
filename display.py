import time, os
from enemies import enemies

def display():
    score = 589000
    hiScore = 000000

    startTime = time.time()
    currentTime = time.time()

    while(currentTime < startTime + 30):
        print(f'SCORE {score} HI-SCORE {hiScore}\n')
        enemies()
        print('  CCCC  CCCC  CCCC  CCCC\n')
        print('---\n')
                    
        time.sleep(1)
        os.system('cls')
        currentTime = time.time()

display()
