import pprint as pp
def readInput(): 
    vals = []
    with open('input.txt', 'r') as reader:
        vals = reader.readlines()
    return vals

def writeOutput(res):
    with open('output.txt', 'w') as writer:
        writer.write(str(res))

def parseBoards(input):
    boards = []
    localboard = []
    for l in range(2, len(input)):
        if input[l] != "\n":
            line =  input[l].split(" ")
            localboard += [[int(l) for l in line if l]]
        else:
            boards += [localboard][:]
            localboard = []

    return boards

def done(line):
    for l in line:
        if l >= 0:
            return False
    return True

def rest(board):
    s = 0
    for l in board:
        for el in l:
            if el >= 0:
                s += el
    return s


def val(input: str):
    return int(input.split(" ")[1])

def solve(picks, boards):
    for p in picks:
        for board in boards:
            for line in board:
                for i in range(len(line)):
                    if line[i] == p:
                        line[i] = ~line[i]
        pp.pprint(p)
        pp.pprint(boards)
        for board in boards:
            for line in board:
                if done(line):
                    pp.pprint(board)
                    return p * rest(board)
    return -1

def solve2(picks, boards):
    for p in picks:
        for board in boards:
            for line in board:
                for i in range(len(line)):
                    if line[i] == p:
                        line[i] = ~line[i]
        pp.pprint(p)
        pp.pprint(boards)
        deleted = False
        for i, board in enumerate(boards):
            for line in board:
                if done(line):
                    if len(boards) == 1:
                        pp.pprint(board)
                        return p * rest(board)                        
                    print(i)
                    del boards[i]
                    deleted = True
            if not deleted:
                for line in zip(*board):
                    if done(line):
                        if len(boards) == 1:
                            pp.pprint(board)
                            return p * rest(board)              
                        print(i)
                        del boards[i]
                        continue
                    
    return -1

                

def run():
    input = readInput()
    picks = [int(p) for p in input[0].split(",") if p]
    boards = parseBoards(input)
    res = solve2(picks, boards)
    print(res)
    writeOutput(res)


if __name__ == '__main__':
    run()