MSIZE = 1000

def readInput():
    vals = []
    with open('input.txt', 'r') as reader:
        vals = reader.readlines()
    return vals

def writeOutput(res):
    with open('output.txt', 'w') as writer:
        writer.write(str(res))

def parsePairs(entries: str):
    pairs = []
    for entry in entries:
        entry = entry.split("->")
        e1, e2 = [e.strip().split(",") for e in entry]
        pairs += [(e1, e2)]
    return pairs

def val(input: str):
    return int(input.split(" ")[1])

def fillVertical(matrix,pairs):
    p1, p2 = pairs
    p1x, p1y = [int(x) for x in p1]
    p2x, p2y = [int(x) for x in p2]

    if p1y != p2y:
        return
    rng = sorted([p1x, p2x])
    rng[1] += 1
    for i in range(rng[0], rng[1]):
        matrix[p1y][i] += 1

def fillHorizontal(matrix, pairs):
    p1, p2 = pairs
    p1x, p1y = [int(x) for x in p1]
    p2x, p2y = [int(x) for x in p2]

    if p1x != p2x:
        return
    rng = sorted([p1y, p2y])
    rng[1] += 1
    for i in range(rng[0], rng[1]):
        matrix[i][p1x] += 1

def fillDiagonal(matrix, pairs):
    p1, p2 = pairs
    p1x, p1y = [int(x) for x in p1]
    p2x, p2y = [int(x) for x in p2]
    if p2y - p1y == p2x - p1x:
        print("first")
        rng = sorted([p1y, p2y])
        rng[1] += 1
        print(rng)
        print(p1, p2)
        for i in range(rng[0], rng[1]):
            j = min(p2x, p1x) + (i - rng[0])
            matrix[i][j] += 1
    if p2y - p1y == p1x - p2x:
        print("second")
        rng = sorted([p1y, p2y])
        print(rng)
        print(p1, p2)
        for i in range(rng[0], rng[1] + 1):
            j = max(p2x, p1x) -i + rng[0]
            matrix[i][j] += 1

def solve(input):
    matrix = [[0 for _ in range(MSIZE)] for _ in range(MSIZE)]
    for p in input:
        # print(p)
        fillVertical(matrix, p)
        fillHorizontal(matrix, p)
        fillDiagonal(matrix,p)
    for l in matrix:
        print(l)
    cnt = 0
    for l in matrix:
        for el in l:
            if el > 1:
                cnt += 1
    return cnt
    


def run():
    input = readInput()
    pairs = parsePairs(input)
    res = solve(pairs)
    print(res)
    writeOutput(res)


if __name__ == '__main__':
    run()