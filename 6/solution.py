import threading 
lock = threading.Lock()
temp_input = []


def readInput():
    vals = []
    with open('input.txt', 'r') as reader:
        vals = reader.readlines()
    return vals

def writeOutput(res):
    with open('output.txt', 'w') as writer:
        writer.write(str(res))

def solve(cnt, t,input):
    global result, temp_input
    for i in range(cnt):
        # if t % 1000 == 0:
        print(f"from thread{t}: step {i}")
        input = fixZeros(input)
        input = decrease(input)
        # print(input)
    lock.acquire()
    temp_input += input
    lock.release()
    
def solvethreads(input):
    threadPool = []
    for i,el in enumerate(input):
        t = threading.Thread(target=solve, args=(128, i, [el],))
        threadPool += [t]
        t.start()
    for t in threadPool:
        t.join()

    global temp_input
    input= temp_input
    temp_input = []
    threadPool = []
    for i,el in enumerate(input):
        t = threading.Thread(target=solve, args=(128, i, [el],))
        threadPool += [t]
        t.start()
    print(len(threadPool))
    for t in threadPool:
        print("joining")
        t.join()

    print(len(temp_input))
    input= temp_input
    temp_input = []
    # print(input)

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
    print(res)
    writeOutput(res)


if __name__ == '__main__':
    run()