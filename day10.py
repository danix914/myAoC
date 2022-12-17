import sys

from helper import clines


_DAY = sys.argv[0].split('.')[0]
MYINPUT = f'{_DAY}-input.txt'



def part1():
    x = 1
    cycle = 1
    targets = [20 + i * 40 for i in range(0, 6)]
    pool = []
    for line in clines(MYINPUT):
        print(f'[{cycle}] {x} ({line})')
        if cycle in targets:
            pool.append(x)
        cycle += 1
        if line == 'noop':
            continue

        print(f'[{cycle}] {x}')
        if cycle in targets:
            pool.append(x)
        _, val = line.split()
        x += int(val)
        cycle += 1
    print(targets)
    print(pool)
    print([x * t for x, t in zip(pool, targets)])
    print(sum([x * t for x, t in zip(pool, targets)]))
    print(cycle)


def crt(x, cycle):
    width = 40
    crtpos = (cycle - 1) % 40
    pixel = '#' if -1 <= x - crtpos <= 1 else '.'
    end = '' if cycle % 40 else '\n'
    print(pixel, end=end)


def part2():
    x = 1
    cycle = 1
    targets = [20 + i * 40 for i in range(0, 6)]
    pool = []
    for line in clines(MYINPUT):
        if cycle in targets:
            pool.append(x)
        crt(x, cycle)
        cycle += 1
        if line == 'noop':
            continue

        if cycle in targets:
            pool.append(x)
        _, val = line.split()
        crt(x, cycle)
        cycle += 1
        x += int(val)


if __name__ == '__main__':
    part1()
    part2()
