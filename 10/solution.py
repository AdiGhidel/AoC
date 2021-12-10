def readInput():
    vals = []
    with open('input.txt', 'r') as reader:
        vals = reader.readlines()
    return [x.strip("\n") for x in vals]


def writeOutput(res):
    with open('output.txt', 'w') as writer:
        writer.write(str(res))


def val(input: str):
    return int(input.split(" ")[1])


def solve(input):
    #part 1
    sum = 0
    mapping = {"{": "}", "[": "]", "(": ")", "<": ">"}
    vals = {")": 3, "]": 57, "}": 1197, ">": 25137}
    mapping2 = {"(":1, "[":2, "{":3, "<":4}
    remainders = []
    for i, line in enumerate(input):
        stack = []
        wrong = False
        for c in line:
            if c in ["{", "[", "(", "<"]:
                stack += c
                continue
            if mapping[stack[-1]] != c:
                print(f"{i}:At line {line} Exp {mapping[stack[-1]]} and got {c}")
                sum += vals[c]
                wrong = True
                break
   
            stack.pop()
    #part2 
        if wrong:
            continue
        if len(stack):
            "".join(stack)
            print(f"{i}:stack not empty: {''.join(stack)}")
            omicron = 0
            for c in reversed(stack):
                omicron = omicron * 5 + mapping2[c]
            remainders += [omicron]
            print(omicron)
    print("Part1:\n" + str(sum))
    print("Part2:")
    print(sorted(remainders)[len(remainders)//2]) 
   

def run():
    input = readInput()
    res = solve(input)
    print(res)
    writeOutput(res)


if __name__ == '__main__':
    run()
