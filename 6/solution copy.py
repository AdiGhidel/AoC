import numpy as np
input = np.loadtxt('input.txt', delimiter=',', dtype=int)
status = []
for i in range(0,9):
    status.append(len(np.where(input == i)[0]))

for i in range(256):
    repro = status.pop(0)
    status.append(repro)
    status[6] += repro
print(sum(status))