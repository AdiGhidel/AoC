def readInput():
    lines = open("input.txt", "r").readlines()

    coordinates = []
    folds = []
    for line in lines:
        if not line.strip():
            continue
        if line.startswith("fold along"):
            fold_axis, fold_coord = line.split()[2].split("=")
            folds.append((fold_axis, int(fold_coord)))
        else:
            x, y = line.split(",")
            coordinates.append((int(x), int(y)))
    return folds, coordinates

def writeOutput(res):
    with open('output.txt', 'w') as writer:
        writer.write(str(res))


def foldx(sheet, fold_coord):
    new_sh = [[False for _ in range(len(sheet[0]))] for _ in range(fold_coord)]
    for y in range(len(sheet[0])):
        for x in range(fold_coord):
            new_sh[x][y] = sheet[x][y]
            if len(sheet) - (2 * fold_coord) - 2 < x:
                new_sh[x][y] = sheet[2 * fold_coord - x][y] or sheet[x][y]
    return new_sh


def foldy(sheet, fold_coord):
    new_sh = [[False for _ in range(fold_coord)] for _ in range(len(sheet))]
    for x in range(len(sheet)):
        for y in range(fold_coord):
            new_sh[x][y] = sheet[x][y]
            if len(sheet[0]) - 2 * fold_coord - 2 < y:
                new_sh[x][y] = sheet[x][2 * fold_coord - y] or sheet[x][y] 
    return new_sh


def foldall(sheet, fold_axis, fold_coord):
    if fold_axis == "y":
        return foldy(sheet, fold_coord)
    return foldx(sheet, fold_coord)



def solve(folds, coordinates):
    n = max(x for x, _ in coordinates)
    m = max(y for _, y in coordinates)
    sheet = [[False for _ in range(m + 1)] for __ in range(n + 1)]
    for x, y in coordinates:
        sheet[x][y] = True
    
    print("Part 1 ", sum(1 for row in foldall(sheet, folds[0][0], folds[0][1]) for pixel in row if pixel))


    for fold in folds:
        sheet = foldall(sheet, fold[0], fold[1])
    print("Part 2:")
    for row in zip(*sheet):
        print("".join("█" if c else "." for c in row))

def run():
    folds, coordinates = readInput()
    res = solve(folds, coordinates)
    print(res)
    writeOutput(res)


if __name__ == '__main__':
    run()