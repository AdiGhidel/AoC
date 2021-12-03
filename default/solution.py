def readInput():
    vals = []
    with open('input.txt', 'r') as reader:
        vals = reader.readlines()
    return vals

def writeOutput(res):
    with open('output.txt', 'w') as writer:
        writer.write(str(res))

def val(input: str):
    return int(input.split(" ")[1])

def solve(input):
    pass

def run():
    input = readInput()
    res = solve(input)
    print(res)
    writeOutput(res)


if __name__ == '__main__':
    run()