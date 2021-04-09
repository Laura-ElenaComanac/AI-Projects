from service.ACO import ACO


class Main:
    def __init__(self, graphFile, settingFile, cycle, evolution):
        self.__aco = ACO(graphFile, settingFile)
        best = None

        with open(cycle, "w") as cycleLog, open(evolution, "w") as evolutionLog:
            for epoch in range(self.__aco.epochs):
                bestAnt = self.__aco.epoch()

                if best is None:
                    best = (bestAnt, epoch)

                if bestAnt.fitness < best[0].fitness:
                    best = bestAnt, epoch

                evolutionLog.write(
                    f"Best solution in epoch {epoch}:\nx = {bestAnt.path}\nf(x) = {bestAnt.fitness}\n")
                evolutionLog.write(
                    f"Best solution NOW in epoch {best[1]}:\nx = {best[0].path}\nf(x) = {best[0].fitness}\n")

                print(
                    f"Best solution in epoch {epoch}:\nx = {bestAnt.path}\nf(x) = {bestAnt.fitness}\n")
                print(
                    f"Best solution NOW in epoch {best[1]}:\nx = {best[0].path}\nf(x) = {best[0].fitness}\n")

            # Number of cities
            cycleLog.write(f"{len(best[0].path)}\n")
            # The optimal traversing cycle
            for city in best[0].path:
                cycleLog.write(f"{city} ")
            # The value of the optimal cycle
            cycleLog.write(f"\n{best[0].fitness}\n")
            cycleLog.write("\n")
            cycleLog.write(str(self.__aco.graph))
            cycleLog.write("\n")

settingFile = "settings.json"

#print("EASY")
Main("data/easy.txt", settingFile, "output/easy/easyCycle.txt", "output/easy/easyEvolution.txt")
#print("MEDIUM")
#Main("data/medium.txt", settingFile, "output/medium/mediumCycle.txt", "output/medium/mediumEvolution.txt")
#print("HARD")
#Main("data/hard.txt", settingFile, "output/hard/hardCycle.txt", "output/hard/hardEvolution.txt")