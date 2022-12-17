def main():
    with open('day1-input.txt', 'r') as fs:
        pool = []
        csum = 0
        for line in fs.readlines():
            if not line.strip():
                pool.append(csum)
                csum = 0
                continue
            csum += int(line.strip())
    print(max(pool))
    spool = sorted(pool)
    print(sum(spool[-3:]))


if __name__ == '__main__':
    main()
