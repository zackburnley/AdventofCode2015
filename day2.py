with open("puzzle2.txt") as f:
    presents, ribbon = [], []
    for line in f:
        line = line.strip()
        l, w, h = line.split("x")
        l, w, h = int(l), int(w), int(h)
        side1, side2, side3 = l*w, w*h, l*h
        surfaceArea = 2 * (side1 + side2 + side3)
        if side1 <= side2 and side1 <= side3:
            surfaceArea += side1
        elif side2 <= side1 and side2 <= side3:
            surfaceArea += side2
        elif side3 <= side1 and side3 <= side2:
            surfaceArea += side3
        presents.append(surfaceArea)
        sidels = [l, w, h]
        sidels.sort()
        perimeter = 2 * sidels[0] + 2 * sidels[1]
        perimeter = perimeter + (l*w*h)
        ribbon.append(perimeter)
    print("Part 1:", sum(presents))
    print("Part 2:", sum(ribbon))