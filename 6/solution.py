import threading 
from collections import defaultdict
lock = threading.Lock()
temp_input = []
perNo = defaultdict(int)

def readInput():
    vals = []
    with open('input.txt', 'r') as reader:
        vals = reader.readlines()
    return vals

def writeOutput(res):
    with open('output.txt', 'w') as writer:
        writer.write(str(res))

def solve(cnt, input):
    global result, temp_input, perNo
    crt = input[0]
    for i in range(cnt):
        input = fixZeros(input)
        input = decrease(input)
    lock.acquire()
    perNo[crt] = len(input)
    temp_input += input
    lock.release()
    
def solvethreads(input):
    global temp_input

    threadPool = []
    for el in range(0,9):
        t = threading.Thread(target=solve, args=(128, [el],))
        threadPool += [t]
        t.start()
    for t in threadPool:
        t.join()

    temp_input = []
    threadPool = []

    for el in input:
        t = threading.Thread(target=solve, args=(128, [el],))
        threadPool += [t]
        t.start()
    
    for t in threadPool:
        t.join()


    counts = defaultdict(int)
    for el in temp_input:
        counts[el] += 1
    
    result = 0
    for k, v in counts.items():
        print(perNo[k] * v)
        result += perNo[k] * v


    print(result)
    return result

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
    res = solvethreads(input)
    writeOutput(res)


if __name__ == '__main__':
    run()