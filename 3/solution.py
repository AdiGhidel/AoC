import math
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
    epsilon = ""
    gamma  = ""
    size = len(input[0]) - 1  
    print(size)
    minCommon  = len(input) // 2
    for l in range(size):
        common = 0
        for n in input:
            if n[l] == "1":
                common += 1
        if common >= minCommon:
            epsilon += "1"
            gamma += "0"
        else:
            epsilon += "0"
            gamma += "1"
    return int(epsilon, 2) * int(gamma, 2)

def solve2(input):
    size = len(input[0]) - 1  
    inputO2, inputCO2 = input, input
    for l in range(size):
        if len(inputO2) == 1:
            break
        # o2
        minCommon  = math.ceil(len(inputO2) / 2)
        common = 0
        for n in inputO2:
            if n[l] == "1":
                common += 1
        if common >= minCommon:
            inputO2 = [x for x in inputO2 if x[l] == "1"]
        else:
            inputO2 = [x for x in inputO2 if x[l] == "0"]
    for l in range(size):
        if len(inputCO2) == 1:
            break
        # co2
        minCommon  = math.ceil(len(inputCO2) / 2)
        common = 0
        for n in inputCO2:
            if n[l] == "1":
                common += 1
        if common < minCommon:
            inputCO2 = [x for x in inputCO2 if x[l] == "1"]
        else:
            inputCO2 = [x for x in inputCO2 if x[l] == "0"]
        
    return (int(inputO2[0], 2) * int(inputCO2[0], 2))

def run():
    input = readInput()
    print(input)
    res = solve2(input)
    print(res)
    writeOutput(res)


if __name__ == '__main__':
    run()