import string

from helper import clines


def main():
    csum = 0
    table = {a: i for a, i in zip(string.ascii_letters, range(1, 53))}
    for line in clines('day03-input.txt'):
        mid = len(line) // 2
        ls = set(line[:mid])
        lr = set(line[mid:])
        char = ls.intersection(lr).pop()
        csum += table[char]
    print(csum)


def part2():
    csum = 0
    table = {a: i for a, i in zip(string.ascii_letters, range(1, 53))}
    cnt = 0
    pool = None
    for line in clines('day03-input.txt'):
        cnt += 1
        l = set(line)
        if pool:
            pool = pool.intersection(l)
        else:
            pool = l

        if cnt != 3:
            continue

        char = pool.pop()
        csum += table[char]
        cnt = 0
        pool = None
    print(csum)


if __name__ == '__main__':
    main()
    part2()
