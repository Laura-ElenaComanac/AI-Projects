from service.geneticAlgorithm import GA


class Main:
    def __init__(self, gmlFile, settingFile, cycle, evolution):
        self.__ga = GA(gmlFile, settingFile)
        best = self.__ga.bestChromosome(), 0

        print(gmlFile)

        with open(cycle, "w") as cycleLog, open(evolution, "w") as evolutionLog:
            for generation in range(self.__ga.nrGen):
                self.__ga.oneGeneration()
                # ga.oneGenerationElitism()
                # ga.oneGenerationSteadyState()

                bestChromo = self.__ga.bestChromosome()

                if bestChromo.fitness < best[0].fitness:
                    best = bestChromo, generation

                evolutionLog.write(
                    f"Best solution in generation  {generation}:\nx = {bestChromo.repres}\nf(x) = {bestChromo.fitness}\n{len(set(bestChromo.repres))}\n")
                evolutionLog.write(
                    f"Best solution NOW in generation  {best[1]}:\nx = {best[0].repres}\nf(x) = {best[0].fitness}\n{len(set(best[0].repres))}\n\n")

                print(
                    f"Best solution in generation  {generation}:\nx = {bestChromo.repres}\nf(x) = {bestChromo.fitness}\n{len(set(bestChromo.repres))}")
                print(
                    f"Best solution NOW in generation  {best[1]}:\nx = {best[0].repres}\nf(x) = {best[0].fitness}\n{len(set(best[0].repres))}\n\n")

            # Number of cities
            cycleLog.write(f"{self.__ga.lenGraph}\n")
            # The optimal traversing cycle
            for city in best[0].repres:
                cycleLog.write(f"{city} ")
            # The value of the optimal cycle
            cycleLog.write(f"\n{best[0].fitness}\n")
            cycleLog.write("\n")


"""
c1, c2 = Chromosome({'noDim':8}), Chromosome({'noDim':8})
c1.repres = [1,2,3,4,5,6,7,8]
c2.repres = [7,2,6,8,1,5,4,3]
c3 = c1.crossover(c2)
print(c3.repres)
c3.mutation()
print(c3.repres)
"""

settingFile = "settings.json"

#print("EASY")
#Main("data/easy.txt", settingFile, "output/easy/easyCycle.txt", "output/easy/easyEvolution.txt")
#print("MEDIUM")
#Main("data/medium.txt", settingFile, "output/medium/mediumCycle.txt", "output/medium/mediumEvolution.txt")
#print("HARD")
#Main("data/hard.txt", settingFile, "output/hard/hardCycle.txt", "output/hard/hardEvolution.txt")