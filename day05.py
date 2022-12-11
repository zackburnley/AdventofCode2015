with open("puzzle05.txt") as f:
    nice = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    forbiddenPairs = ['ab', 'cd', 'pq', 'xy']
    for line in f:
        line = line.strip()
        numVowels = 0
        threeVowels = False
        doubleLetter = False
        forbiddenStrings = False
        for c in line:
            if c in vowels:
                numVowels += 1
        if numVowels >= 3:
            threeVowels = True
        for i, c in enumerate(line):
            if i == len(line)-1:
                break
            if c == line[i+1]:
                doubleLetter = True
            test = c + line[i+1]
            if test in forbiddenPairs:
                forbiddenStrings = True
                break
        if threeVowels and doubleLetter and not forbiddenStrings:
            nice += 1
    print("Part 1:", nice)
####################################################################################
with open("puzzle05.txt") as f:
    nice = 0
    for line in f:
        line = line.strip()
        pairs = []
        pairCheck = False
        spaceCheck = False
        for i, c in enumerate(line):
            if i == len(line)-1:
                break
            temp = c + line[i+1]
            pairs.append(temp)
        for pair in pairs:
            pairCount = 0
            i = 0
            while i < len(line)-1:
                temp = line[i:i+2]
                if temp == pair:
                    pairCount += 1
                    i += 1
                if pairCount == 2:
                    break
                i += 1
            if pairCount == 2:
                pairCheck = True
                break
        for i, c in enumerate(line):
            if i == len(line)-2:
                break
            if c == line[i+2]:
                spaceCheck = True
                break
        if pairCheck and spaceCheck:
            nice += 1
    print("Part 2:", nice)