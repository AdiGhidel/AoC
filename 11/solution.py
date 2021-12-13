def readInput():
    vals = []
    with open('input.txt', 'r') as reader:
        vals = reader.readlines()
    return [[int(i) for i in line if i.isalnum()] for line in vals]


def writeOutput(res):
    with open('output.txt', 'w') as writer:
        writer.write(str(res))

def isValid(i, j):
    return  0 <= i < 10 and 0 <= j < 10 

def wave(grid, row, col):
    flashed = []
    states = {(-1,-1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)}
    for deltaI, deltaJ in states:
        i, j = row + deltaI, col + deltaJ
        if isValid(i, j) and grid[i][j] != 10:
            grid[i][j] += 1
            if grid[i][j] == 10:
                flashed.append((i, j))
    return flashed


def solve(grid):
    all_flashes = 0
    steps = 0

    while True:
        flashed = []
        for i in range(10):
            for j in range(10):
                grid[i][j] += 1
                if grid[i][j] == 10:
                    flashed.append((i, j))
        for (i, j) in flashed:
            flashed += wave(grid, i, j)
        all_flashes += len(flashed)
        steps += 1

        if steps == 100:
            part1 = all_flashes

        if all(sum(row) == 100 for row in grid):
            return part1, steps
        for i, j in flashed:
            grid[i][j] = 0


def run():
    input = readInput()
    res = solve(input)
    print(res)
    writeOutput(res)


if __name__ == '__main__':
    run()
