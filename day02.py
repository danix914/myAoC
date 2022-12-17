def main():
    table = {
        'A': 1, # rock
        'B': 2, # paper
        'C': 3, # scissors
        'X': 1,
        'Y': 2,
        'Z': 3,
    }
    csum = 0
    with open('day2-input.txt', 'r') as fs:
        for line in fs.readlines():
            elf, player = line.split()
            ve = table[elf]
            vp = table[player]
            game = ve - vp
            if game == 0:
                csum += (3 + vp)
            if game == 1 or game == -2:
                csum += vp
            if game == 2 or game == -1:
                csum += (6 + vp)
    print(csum)


def part2():
    table = {
        'A': 1, # rock
        'B': 2, # paper
        'C': 3, # scissors
        'X': -1,
        'Y': 0,
        'Z': 1,
    }
    csum = 0
    with open('day2-input.txt', 'r') as fs:
        for line in fs.readlines():
            elf, game = line.split()
            ve = table[elf]
            vg = table[game]
            player = ve + vg
            if player == 0:
                player = 3
            elif player == 4:
                player = 1
            csum += ((vg + 1) * 3 + player)
    print(csum)


if __name__ == '__main__':
    #main()
    part2()
