with open("puzzle01.txt") as f:
    for line in f:
        line = line.strip()
        line = list(line)
        floor, pos = 0, 0
        basementFound = False
        for i, c in enumerate(line):
            if c == '(':
                floor += 1
            elif c == ')':
                floor -= 1
            if floor == -1 and not basementFound:
                pos = i+1
                basementFound = True
    print("Part 1:", floor)
    print("Part 2:", pos)