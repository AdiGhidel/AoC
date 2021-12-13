from collections import defaultdict

def readInput():
    graph = defaultdict(list)
    caves = set()
    with open('input.txt', 'r') as reader:
        lines = reader.readlines()
        for line in lines:
            edge = line.strip().split('-')
            a, b = edge[0], edge[1]

            if (a.lower() == a):
                caves.add(a)
            if (b.lower() == b):
                caves.add(b)

            graph[a].append(b)
            graph[b].append(a)

    return graph, caves


def writeOutput(res):
    with open('output.txt', 'w') as writer:
        writer.write(str(res))


def val(input: str):
    return int(input.split(" ")[1])


def dfs1(graph, caves, current, visited):
    total_paths = 0

    if current in visited:
        return total_paths
    if current == 'end':
        return 1

    if current in caves:
        visited.add(current)

    for neighbor in graph[current]:
        total_paths += dfs1(graph, caves, neighbor, visited)

    visited.discard(current)
    return total_paths

def dfs2(graph, caves, current, visited, isTwice):
    total_paths = 0

    if visited[current] > 0 and isTwice:
        return total_paths
    if current == 'end':
        return 1

    if current in caves:
        visited[current] += 1
        if visited[current] == 2:
            isTwice = True

    for neighbor in graph[current]:
        if (neighbor != 'start'):
            total_paths += dfs2(graph, caves, neighbor, visited, isTwice)

    visited[current] -= 1

    return total_paths


def solve(graph, caves):
    #pt1 
    print(dfs1(graph, caves, "start", set()))
    #pt2
    print(dfs2(graph, caves, 'start', defaultdict(int), False))


def run():
    graph, caves = readInput()
    res = solve(graph, caves)
    print(res)
    writeOutput(res)


if __name__ == '__main__':
    run()
