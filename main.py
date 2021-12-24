import time, os
import random

class Colors:
    black = '\033[30m'
    white = '\033[37m'
    bg_white = '\033[47m'

if __name__ == "__main__":

    print(f'{Colors.white}{Colors.bg_white}')

    os.system('cls')
    while True:
        j=12
        for i in range(1,20,2):
            j-=1
            c = random.randint(1,5)
            print(f'{Colors.white}{Colors.bg_white}░'*j, end='')
            print(f'\033[4{random.randint(1,6)}m\033[1;9{random.randint(1,5)}m▄'*i, end='')
            print(f'{Colors.white}{Colors.bg_white}\033[37m░'*j)

        for i in range(2):
            for j in range(11):
                print('░', end='')
            print(f'{Colors.black}▐{Colors.white}' if i==0 else '' ,end='')

        print('\n',f'{Colors.black}🌟 Feliz Natal 🌟'.center(23))

        time.sleep(random.randint(5, 10)/10)
        os.system('cls')