from random import uniform
from random import randint


def generateNewValue(lim1, lim2):
    # return uniform(lim1, lim2)
    return randint(lim1, lim2)


def functionFactory(function):
    if function == "modularityFitness":
        return modularityFitness
    else:
        raise Exception("Non-existent fitness function")


def L(representation, graph, leftLabel=None, rightLabel=None):  # L(C1, C2)
    if leftLabel is None:
        leftCommunity = graph.nodes
    else:
        leftCommunity = [pos for pos, label in enumerate(representation) if label == leftLabel]

    if rightLabel is None:
        rightCommunity = graph.nodes
    else:
        rightCommunity = [pos for pos, label in enumerate(representation) if label == rightLabel]

    sum = 0
    for i in leftCommunity:
        for j in rightCommunity:
            if i in graph[j]:
                sum += 1

    return sum


def modularityFitness(representation, graph):  # Q
    communities = set(representation)
    m = graph.edges

    return -sum(
        [
            L(representation, graph, community, community) / (2 * m) -
            (L(representation, graph, community) / (2 * m)) ** 2
            for community in communities
        ]
    )


def interpretLabels(representation):  # labels to numbers
    map = {}
    newRepresentation = []
    currentCommunity = 0

    for label in representation:
        if label not in map:
            currentCommunity += 1
            map[label] = currentCommunity
        newRepresentation.append(map[label])

    return newRepresentation
