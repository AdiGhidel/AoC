def readInput():
    vals = []
    with open('input.txt', 'r') as reader:
        vals = reader.readlines()
    return vals

def writeOutput(res):
    with open('output.txt', 'w') as writer:
        writer.write(str(res))

def solve(input):
    cnt = 0
    print(len(input))
    for i in range(1, len(input)):
        if input[i] > input[i - 1]:
            cnt += 1
    return cnt

def solve2(input, window=3):
    cnt = 0
    crt = 0
    for i in range(window):
        crt += input[i]
    for i in range(window, len(input)):
        prev = crt
        crt = crt - input[i - window] + input[i]
        print(prev, crt)
        if crt > prev:
            cnt += 1

    return cnt



def run():
    input = readInput()
    print(list(enumerate(input)))
    lines = [int(line.rstrip()) for line in input]
    res = solve2(lines)
    print(res)
    writeOutput(res)


if __name__ == '__main__':
    run()