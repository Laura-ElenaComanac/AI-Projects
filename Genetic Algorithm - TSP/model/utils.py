from random import randint


def generateNewValue(lim1, lim2):
    return randint(lim1, lim2)


def functionFactory(function):
    if function == "fitness":
        return fitness
    else:
        raise Exception("Non-existent fitness function")


def fitness(representation, graph): # cost
    return sum([graph[representation[i]][representation[i + 1]] for i in range(len(representation) - 1)])


def transform_input(filename):  # to a matrix
    f = open(filename, "r")
    v = f.readlines()
    graph = []

    for line in v[1:-2]:
        graph.append([int(x) for x in line.split(",")])

    return graph
