from collections import defaultdict
import sys

from helper import clines


_DAY = sys.argv[0].split('.')[0]
MYINPUT = f'{_DAY}-input.txt'


def stack_line(pool, items, line):
    idx = 0
    pos = 1
    while pos < len(line):
        crate = line[pos]
        if crate != ' ':
            pool[items[idx]].append(crate)
        idx += 1
        pos += 4


def action_line(line):
    cs = line.split()
    return cs[1], cs[3], cs[5]


def parser():
    stacks = []
    actions = []
    target = stacks
    for line in clines(MYINPUT):
        if not line.strip():
            target = actions
            continue
        target.append(line)

    items = stacks[-1].split()
    pool = defaultdict(list)
    for stack in stacks[-2::-1]:
        stack_line(pool, items, stack)
    for k, v in pool.items():
        print(f"{k}: {''.join(v)}")
    return pool, actions


def part1():
    pool, actions = parser()
    for action in actions:
        cnt, src, dst = action_line(action)
        for _ in range(int(cnt)):
            pool[dst].append(pool[src].pop())
    print(''.join([v[-1] for _, v in pool.items()]))


def part2():
    pool, actions = parser()
    for action in actions:
        cnt, src, dst = action_line(action)
        cnt = int(cnt)
        pool[dst] += pool[src][-cnt:]
        del(pool[src][-cnt:])
    print(''.join([v[-1] for _, v in pool.items()]))


if __name__ == '__main__':
    part1()
    part2()
