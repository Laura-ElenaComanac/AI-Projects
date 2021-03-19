from model.utils import interpretLabels
from repository.graph import *
from service.geneticAlgorithm import GA


class Main:
    def __init__(self, gmlFile, settingFile, communities, evolution):
        self.__ga = GA(gmlFile, settingFile)
        best = self.__ga.bestChromosome(), 0

        print(gmlFile)

        with open(communities, "w") as communitiesLog, open(evolution, "w") as evolutionLog:
            for generation in range(self.__ga.nrGen):
                self.__ga.oneGeneration()
                # ga.oneGenerationElitism()
                # ga.oneGenerationSteadyState()

                bestChromo = self.__ga.bestChromosome()

                if bestChromo.fitness < best[0].fitness:
                    best = bestChromo, generation

                evolutionLog.write(f"Best solution in generation  {generation}:\nx = {bestChromo.repres}\nf(x) = {bestChromo.fitness}\n{len(set(bestChromo.repres))}\n")
                evolutionLog.write(f"Best solution NOW in generation  {best[1]}:\nx = {best[0].repres}\nf(x) = {best[0].fitness}\n{len(set(best[0].repres))}\n\n")

                print(f"Best solution in generation  {generation}:\nx = {bestChromo.repres}\nf(x) = {bestChromo.fitness}\n{len(set(bestChromo.repres))}")
                print(f"Best solution NOW in generation  {best[1]}:\nx = {best[0].repres}\nf(x) = {best[0].fitness}\n{len(set(best[0].repres))}\n\n")

            communitiesLog.write(str(len(set(best[0].repres))) + "\n")
            interpretedSol = interpretLabels(best[0].repres)
            for node, community in enumerate(interpretedSol, start = 1):
                communitiesLog.write(f"{node} : {community}\n")


gmlFileDolphins = "data/dolphins/dolphins.gml"
gmlFileFootball = "data/football/football.gml"
gmlFileKarate = "data/karate/karate.gml"
gmlFileKrebs = "data/krebs/krebs.gml"

gmlFileBooks = "data/books/books.gml"
gmlFileLesMiserables = "data/lesmiserables/lesmiserables.gml"

settingFile = "settings.json"

dolphinsCommunities = "output/dolphins/dolphinsCommunities.txt"
dolphinsEvolution = "output/dolphins/dolphinsEvolution.txt"

footballCommunities = "output/football/footballCommunities.txt"
footballEvolution = "output/football/footballEvolution.txt"

karateCommunities = "output/karate/karateCommunities.txt"
karateEvolution = "output/karate/karateEvolution.txt"

krebsCommunities = "output/krebs/krebsCommunities.txt"
krebsEvolution = "output/krebs/krebsEvolution.txt"


booksCommunities = "output/books/booksCommunities.txt"
booksEvolution = "output/books/booksEvolution.txt"

lesMiserablesCommunities = "output/lesmiserables/lesmiserablesCommunities.txt"
lesMiserablesEvolution = "output/lesmiserables/lesmiserablesEvolution.txt"


#Main(gmlFileDolphins, settingFile, dolphinsCommunities, dolphinsEvolution)
#Main(gmlFileFootball, settingFile, footballCommunities, footballEvolution)
#Main(gmlFileKarate, settingFile, karateCommunities, karateEvolution)
Main(gmlFileKrebs, settingFile, krebsCommunities, krebsEvolution)

#Main(gmlFileBooks, settingFile, booksCommunities, booksEvolution)
#Main(gmlFileLesMiserables, settingFile, lesMiserablesCommunities, lesMiserablesEvolution)