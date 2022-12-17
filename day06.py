import sys

from helper import clines


_DAY = sys.argv[0].split('.')[0]
MYINPUT = f'{_DAY}-input.txt'


def part1():
    for line in clines(MYINPUT):
        pool = {}
        ptn = ''
        start = 0
        for idx, c in enumerate(line):
            if c in pool:
                pos = pool[c]
                if pos < start:
                    ptn += c
                else:
                    #print(ptn, c, start, pos, idx)
                    ptn = ptn[pos - start + 1:] + c
                    start = pos + 1
            else:
                ptn += c
            
            pool[c] = idx
            if len(ptn) == 4:
                print(ptn, pos, idx, '(0-base)')
                break


def part2():
    for line in clines(MYINPUT):
        pool = {}
        ptn = ''
        start = 0
        for idx, c in enumerate(line):
            if c in pool:
                pos = pool[c]
                if pos < start:
                    ptn += c
                else:
                    #print(ptn, c, start, pos, idx)
                    ptn = ptn[pos - start + 1:] + c
                    start = pos + 1
            else:
                ptn += c
            
            pool[c] = idx
            if len(ptn) == 14:
                print(ptn, pos, idx, '(0-base)')
                break


if __name__ == '__main__':
    part1()
    part2()
