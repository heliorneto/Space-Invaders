import sys, time

def enemies():
    enemies = 'B '
    for i in range(5):
        print('\n')
        for i in range(10):
            print(enemies, end='')
            sys.stdout.flush()
            time.sleep(0.5)
    print('\n\n')
