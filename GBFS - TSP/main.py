from queue import PriorityQueue


def transform_input(filename): # to a matrix and a tuple (source, destination)
    f = open(filename, "r")
    v = f.readlines()
    graph = []

    for line in v[1:-2]:
        graph.append([int(x) for x in line.split(",")])

    return graph, (int(v[-2]), int(v[-1]))


# print(transform_input("input.txt"))

def output(filename, strategy): # GBFS or NearestNeighbour
    graph, (source, destination) = transform_input(filename)
    path = strategy(graph, source - 1, destination - 1)
    cycle = strategy(graph, 0, 0)

    # number of cities
    print(len(graph))
    # the optimal traversing cycle
    print([x + 1 for x in cycle[:-1]])
    # the value of the optimal cycle
    print(cost(graph, cycle))
    # the length of the optimal path (source -> destination)
    print(len(path))
    # the optimal traversing path
    print([x + 1 for x in path])
    # the value of the optimal path
    print(cost(graph, path))


def cost(graph, path):
    return sum([graph[path[i]][path[i + 1]] for i in range(len(path) - 1)])


def processPredecessors(source, destination, predecessors, isCycle):  # from dictionary to list
    path = [source]
    currentNode = destination

    while source != currentNode:
        path.insert(1, currentNode)
        currentNode = predecessors[currentNode]
    if isCycle:
        path.append(source)

    return path


def GBFS(graph, source, destination): # Greedy Best First Search
    found = False
    visited = set()
    toVisit = PriorityQueue()
    toVisit.put((0, source))
    predecessors = {source: -1}
    lastNode = None # for cycles

    while not toVisit.empty() and not found:
        currentNode = toVisit.get()[1]
        visited.add(currentNode)
        if len(visited) == len(graph) and lastNode is None:
            lastNode = currentNode
        if currentNode == destination and len(visited) > 1:
            found = True
        for child in range(len(graph)):
            if child not in visited:
                cost = graph[currentNode][child]
                toVisit.put((cost, child))
                predecessors[child] = currentNode
    if lastNode is None:
        lastNode = destination # for paths

    return processPredecessors(source, lastNode, predecessors, source == destination)


def nearestNeighbour(graph, source, destination):
    visited = set()
    predecessors = {source: -1}
    currentNode = source

    while True:
        visited.add(currentNode)
        if currentNode == destination and len(visited) > 1 or len(visited) == len(graph): # path or cycle
            break
        neighbours = [(node, cost) for node, cost in enumerate(graph[currentNode]) if node not in visited]
        prev = currentNode
        currentNode = min(neighbours, key=lambda neighbour: neighbour[1])[0]
        predecessors[currentNode] = prev

    return processPredecessors(source, currentNode, predecessors, source == destination)


strategy = nearestNeighbour
# strategy = GBFS

print("demo")
output("input.txt", strategy)
print("EASY")
output("easy.txt", strategy)
print("MEDIUM")
output("medium.txt", strategy)
print("HARD")
output("hard.txt", strategy)
