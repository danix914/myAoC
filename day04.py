import re
import sys

from helper import clines


_DAY = sys.argv[0].split('.')[0]
MYINPUT = f'{_DAY}-input.txt'


def parser(line):
    return [int(i) for i in re.split(r'[-,]', line)]
    
def part1():
    cnt = 0
    for line in clines(MYINPUT):
        ll, lr, rl, rr = parser(line)
        if ((ll <= rl and rr <= lr)  # ll - rl - rr - lr
                or (rl <= ll and lr <= rr)):  # rl - ll - lr - rr
            cnt += 1
    print(cnt)


def part2():
    cnt = 0
    for line in clines(MYINPUT):
        ll, lr, rl, rr = parser(line)
        if ((ll <= rl <= lr)  # ll - rl - lr
                or (rl <= ll <= rr)):  # rl - ll - rr
            cnt += 1
    print(cnt)


if __name__ == '__main__':
    part1()
    part2()
