from numpy import random
import numpy as np


class Chromosome:
    def __init__(self, problParam=None):
        self.__problParam = problParam
        self.__repres = np.random.permutation(problParam['noDim'])
        self.__fitness = 0.0

    @property
    def repres(self):
        return self.__repres

    @property
    def fitness(self):
        return self.__fitness

    @repres.setter
    def repres(self, l=[]):
        self.__repres = l

    @fitness.setter
    def fitness(self, fit=0.0):
        self.__fitness = fit

    def crossover(self, c):  # source and destination
        first, second = random.choice(range(1, len(self.__repres)), size=2, replace=False)
        newRepresentation = [-1 for _ in range(len(self.__repres))]

        for pos in range(first, second):
            newRepresentation[pos] = self.__repres[pos]

        posOffspring = second
        posDestination = second
        while newRepresentation[posOffspring] == -1:
            if c.__repres[posDestination] not in newRepresentation:
                newRepresentation[posOffspring] = c.__repres[posDestination]
                posOffspring = (posOffspring + 1) % len(self.__repres)
            posDestination = (posDestination + 1) % len(self.__repres)

        offspring = Chromosome(self.__problParam)
        offspring.repres = newRepresentation

        return offspring

    def mutation(self):
        first, second = random.choice(len(self.__repres), size=2, replace=False)
        self.__repres[first], self.__repres[second] = self.__repres[second], self.__repres[first]

    def __str__(self):
        return '\nChromo: ' + str(self.__repres) + ' has fit: ' + str(self.__fitness)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, c):
        return self.__repres == c.__repres and self.__fitness == c.__fitness
