from random import choice
from random import random
from model.utils import *


class Ant:
    def __init__(self, graph):
        self.__graph = graph
        self.__path = [choice(self.__graph.nodes)]

    def computeProduct(self, node): # trace^alpha * (1/cost)^beta
        return (self.__graph.trace[self.__path[-1]][node] ** self.__graph.settings['alpha']) * \
                   (1 / self.__graph[self.__path[-1]][node] ** self.__graph.settings['beta'])

    def addMove(self): # alegera oraselor
        nextNodes = [node for node in self.__graph.nodes if node not in self.__path]
        if len(nextNodes) == 0:
            return

        pairs = [(node, self.computeProduct(node)) for node in nextNodes]

        if random() < self.__graph.settings['q0']:
            self.__path.append(max(pairs, key=lambda pair: pair[1])[0])
        else:
            # ruleta
            s = sum([pair[1] for pair in pairs])
            prob = [(node, val / s) for node, val in pairs]
            prob = [
                (
                    prob[i][0],
                    sum([prob[j][1] for j in range(i + 1)])  # suma prob pana la nod
                )
                for i in range(len(prob))]

            r = random()
            i = 0
            while r > prob[i][1]:
                i += 1
            self.__path.append(prob[i][0])

    @property
    def fitness(self):
        return fitness(self.__path, self.__graph)

    @property
    def path(self):
        return self.__path
