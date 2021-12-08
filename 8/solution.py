mappingA = {2: 1, 4: 4, 3: 7, 7: 8}


def readInput():
    vals = []
    with open('input.txt', 'r') as reader:
        vals = reader.readlines()
    return vals


def writeOutput(res):
    with open('output.txt', 'w') as writer:
        writer.write(str(res))


def getOutVals(input):
    res = []
    for l in input:
        res.append([x.strip('\n') for x in l.split("|")[1].split(" ") if x])
    return res


def getOutVals2(line):
    all = line.split("|")
    tens = [x.strip('\n') for x in all[0].split(" ") if x]
    fours = [x.strip('\n') for x in all[1].split(" ") if x]
    return tens, fours


def common(s1, s2):
    return len(set(s1) & set(s2))


def solve(input):
    # part1
    vals = getOutVals(input)
    s = 0
    for line in vals:
        for v in line:
            if len(v) in [2, 3, 4, 7]:
                s += 1
    print("part 1")
    print(s)
    # part2
    s = 0
    for i in range(len(input)):
        line = input[i]
        tens, fours = getOutVals2(line)
        # need sorting
        for crt in range(len(tens)):
            tens[crt] = "".join(sorted(tens[crt]))
        for crt in range(len(fours)):
            fours[crt] = "".join(sorted(fours[crt]))
        zero = one = two = three = four = five = six = seven = eight = nine = ""
        # find common
        for crt in tens:
            if len(crt) == 2:
                one = crt
            elif len(crt) == 3:
                seven = crt
            elif len(crt) == 4:
                four = crt
            elif len(crt) == 7:
                eight = crt
        # do some magic matching
        for crt in tens:
            if common(four, crt) == 3 and common(one, crt) == 2 and len(crt) == 6:
                zero = crt
            elif common(four, crt) == 2 and common(one, crt) == 1 and len(crt) == 5:
                two = crt
            elif common(four, crt) == 3 and common(one, crt) == 2 and len(crt) == 5:
                three = crt
            elif common(four, crt) == 3 and common(one, crt) == 1 and len(crt) == 5:
                five = crt
            elif common(four, crt) == 3 and common(one, crt) == 1 and len(crt) == 6:
                six = crt
            elif common(four, crt) == 4 and len(crt) == 6:
                nine = crt

        digits = {zero: "0", one: "1", two: "2", three: "3", four: "4",
                  five: "5", six: "6", seven: "7", eight: "8", nine: "9"}

        crt = [digits[i] for i in fours]
        num = int("".join(crt))
        s += num
    print("part 2")
    print(s)


def run():
    input = readInput()
    res = solve(input)
    print(res)
    writeOutput(res)


if __name__ == '__main__':
    run()
