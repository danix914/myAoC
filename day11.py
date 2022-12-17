from collections import namedtuple, Counter
import sys

from helper import clines


_DAY = sys.argv[0].split('.')[0]
MYINPUT = f'{_DAY}-input.txt'
Monkey = namedtuple('Monkey', ['items', 'op', 'test', 'tot', 'tof'])


def parser():
    def _p(ls):
        name = ls[0].replace(':', '').split()[1]
        items = [int(i.strip()) for i in ls[1].split(':')[1].split(',')]
        op = ls[2].split(':')[1].split('=')[1].strip()
        test = int(ls[3].split()[-1])
        tot = ls[4].split()[-1]
        tof = ls[5].split()[-1]
        return name, Monkey(items, op, test, tot, tof)

    temp = []
    ms = {}
    cnt = 0
    for line in clines(MYINPUT):
        if not line:
            k, v = _p(temp)
            ms[k] = v
            temp = []
            continue
        temp.append(line)
    k, v = _p(temp)
    ms[k] = v
    return ms


def worrylevel(item, opstr):
    l, o, r = opstr.split()
    l = item if l == 'old' else int(l)
    r = item if r == 'old' else int(r)
    if o == '+':
        wl = l + r
    elif o == '*':
        wl = l * r
    return wl


def runround(ms, cnt, div):
    # for k, v in ms.items():
        # print(f'[{k}] {v.items}')
    # print()
    for name, attrs in ms.items():
        # print(f'[{name}] {attrs.items}')
        while attrs.items:
            item = attrs.items.pop(0)
            cnt[name] += 1
            wl = worrylevel(item, attrs.op)
            if div != 1:
                wl //= div
            # print(f'[{name}] {wl}')
            if wl % attrs.test == 0:
                ms[attrs.tot].items.append(wl)
            else:
                ms[attrs.tof].items.append(wl)
    # for k, v in ms.items():
        # print(f'[{k}] {v.items}')
    # print(cnt)


def part1():
    ms = parser()
    cnt = Counter()
    for _ in range(20):
        runround(ms, cnt, 3)
    t1, t2 = cnt.most_common(2)
    print(t1[1] * t2[1])


def part2():
    ms = parser()
    cnt = Counter()
    for _ in range(10000):
        runround(ms, cnt, 3)
    t1, t2 = cnt.most_common(2)
    print(t1[1] * t2[1])


if __name__ == '__main__':
    part1()
    part2()
