def clines(path):
    with open(path, 'r') as fs:
        for line in fs.readlines():
            yield line.rstrip()
