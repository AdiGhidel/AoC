def readInput():
    vals = []
    with open('input.txt', 'r') as reader:
        vals = reader.readlines()
    return vals

def writeOutput(res):
    with open('output.txt', 'w') as writer:
        writer.write(str(res))

def solve(input):
    for i in range(256):
        input = fixZeros(input)
        input = decrease(input)
        # print(input)
    return len(input)
    

def decrease(vec):
    return [x - 1 for x in vec]

def fixZeros(vec):
    newstuff = []
    for i in range(len(vec)):
        if vec[i] == 0:
            vec[i] = 7
            newstuff += [9]
    return vec + newstuff

def run():
    input = readInput()
    input = [int(x) for x in input[0].split(",")]
    res = solve(input)
    print(res)
    writeOutput(res)


if __name__ == '__main__':
    run()