from repository.graph import MyGraph
from model.ant import Ant
import numpy as np
from random import randint
from random import random


class ACO:
    def __init__(self, graphFile, settingFile):
        self.__graph = MyGraph(graphFile, settingFile)

    def epoch(self):
        if self.__graph.settings['dynamic'] and random() < self.__graph.settings['changeProb']:
            x, y = np.random.choice(self.__graph.nodes, size=2, replace=False)
            self.__graph[x][y] = self.__graph[y][x] = randint(self.__graph.settings['minCost'], self.__graph.settings['maxCost'])

        ants = [Ant(self.__graph) for _ in range(self.__graph.settings['noAnts'])]
        for _ in range(len(self.__graph) - 1):
            for ant in ants:
                ant.addMove()

        pheromons = [self.__graph.settings['Q'] / ant.fitness for ant in ants]

        for i in range(len(self.__graph)):
            for j in range(len(self.__graph)):
                self.__graph.trace[i][j] *= (1 - self.__graph.settings['decay']) # intensitatea urmei de feromon

        for index, ant in enumerate(ants):
            for i in range(len(ant.path) - 1):
                x = ant.path[i]
                y = ant.path[i + 1]
                self.__graph.trace[x][y] = pheromons[index]

        # furnica cu cel mai bun fitness
        return min(
            [(ant.fitness, ant) for ant in ants], key=lambda pair: pair[0]
        )[1]

    @property
    def epochs(self):
        return self.__graph.settings['epochs']

    @property
    def graph(self):
        return self.__graph
