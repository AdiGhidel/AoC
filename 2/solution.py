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
    horizontal, vertical = 0, 0
    depth = 0
    for l in input:
        if 'forward' in l:
            horizontal += val(l)
            depth += vertical * val(l)
        elif 'up' in l:
            vertical -= val(l)
        elif 'down' in l:
            vertical += val(l)
    
    return horizontal * depth


def run():
    input = readInput()
    res = solve(input)
    print(res)
    writeOutput(res)


if __name__ == '__main__':
    run()