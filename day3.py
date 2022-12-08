with open("puzzle3.txt") as f:
    visited = {(0, 0)}
    x, y, = 0, 0
    for line in f:
        line = line.strip()
        line = list(line)
        for c in line:
            if c == '>':
                x += 1
            elif c == '<':
                x -= 1
            elif c == '^':
                y += 1
            elif c == 'v':
                y -= 1
            vtuple = (x, y)
            visited.add(vtuple)
    print("Part 1:", len(visited))
##############################################################
with open("puzzle3.txt") as f:
    svisited, rsvisited = {(0, 0)}, {(0, 0)}
    sx, sy, rsx, rsy = 0, 0, 0, 0
    for line in f:
        line = line.strip()
        line = list(line)
        for i, c in enumerate(line):
            if i % 2 == 0:
                if c == '>':
                    sx += 1
                elif c == '<':
                    sx -= 1
                elif c == '^':
                    sy += 1
                elif c == 'v':
                    sy -= 1
                vtuple = (sx, sy)
                svisited.add(vtuple)
            else:
                if c == '>':
                    rsx += 1
                elif c == '<':
                    rsx -= 1
                elif c == '^':
                    rsy += 1
                elif c == 'v':
                    rsy -= 1
                vtuple = (rsx, rsy)
                rsvisited.add(vtuple)
    print("Part 2:", len(svisited.union(rsvisited)))