from random import randint
from model.utils import functionFactory
from repository.graph import *
from model.chromosome import Chromosome


class GA:
    def __init__(self, txtFile, settingFile):
        self.__graph = MyGraph(txtFile, settingFile)
        self.__problParam = self.__graph.settings
        self.__population = []
        self.initialisation()
        self.evaluation()

    @property
    def lenGraph(self):
        return len(self.__graph)

    @property
    def nrGen(self):
        return self.__graph.settings['generations']

    @property
    def population(self):
        return self.__population

    def initialisation(self):
        for _ in range(0, self.__problParam['popSize']):
            c = Chromosome(self.__problParam)
            self.__population.append(c)

    def evaluation(self): # fitness
        for c in self.__population:
            c.fitness = functionFactory(self.__problParam['function'])(c.repres, self.__graph)

    def bestChromosome(self):
        best = self.__population[0]
        for c in self.__population:
            if c.fitness < best.fitness:
                best = c
        return best

    def worstChromosome(self):
        best = self.__population[0]
        for c in self.__population:
            if c.fitness > best.fitness:
                best = c
        return best

    def selection(self):
        pos1 = randint(0, self.__problParam['popSize'] - 1)
        pos2 = randint(0, self.__problParam['popSize'] - 1)
        if self.__population[pos1].fitness < self.__population[pos2].fitness:
            return pos1
        else:
            return pos2

    def oneGeneration(self):
        newPop = []
        for _ in range(self.__problParam['popSize']):
            p1 = self.__population[self.selection()]
            p2 = self.__population[self.selection()]
            off = p1.crossover(p2)
            off.mutation()
            newPop.append(off)
        self.__population = newPop
        self.evaluation()

    def oneGenerationElitism(self):
        newPop = [self.bestChromosome()]
        for _ in range(self.__problParam['popSize'] - 1):
            p1 = self.__population[self.selection()]
            p2 = self.__population[self.selection()]
            off = p1.crossover(p2)
            off.mutation()
            newPop.append(off)
        self.__population = newPop
        self.evaluation()

    def oneGenerationSteadyState(self):
        for _ in range(self.__problParam['popSize']):
            p1 = self.__population[self.selection()]
            p2 = self.__population[self.selection()]
            off = p1.crossover(p2)
            off.mutation()
            off.fitness = self.__problParam['function'](off.repres)
            worst = self.worstChromosome()
            if (off.fitness < worst.fitness):
                worst = off