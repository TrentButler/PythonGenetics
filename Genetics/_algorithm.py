import os
from _operator import *
from _chromosome import Chromosome
from _expression import Expression

# INITIALIZE A POPULATION(GENERATION#)
# DETERMAINE FITNESS OF POPULATION(GENERATION#)
# WHILE TERMINATING CONDITION IS NOT MET:
# - SELECT PARENTS FROM POPULATION(GENERATION#)
# - PERFORM CROSSOVER ON PARENTS
#       - THIS CREATES A NEW POPULATION (POPULATION(GENERATION# + 1))
# - PERFORM MUTATION OF NEW POPULATION (POPULATION(GENERATION# + 1))
# - DETERMINE FITNESS OF NEW POPULATION (POPULATION(GENERATION# + 1))

class Algorithm(object):

    def __init__(self):
        self.data = []
        self.generation = 0
        self.population = []

    def _generate_population(self, chromo_length, count):
        population = []
        for x in range(0, count, 1):
            c = Chromosome("") # CREATE NEW CHROMOSOME
            c._generate(chromo_length, True) #INITIALIZE THE CHROMOSOME'S VALUES RANDOMLY
            population.append(c)
        return population

    def _run_algorithm(self, expression):
        #DETERMINE CHROMOSOME COUNT
        c_count = expression.GetVariables().count
        self.population = self._generate_population(c_count, 4)
        
        #FITNESS FUNCTION

        # while True:
        #     currentGeneration = Selection(self.population)

        


def main():
    a = Algorithm()
    e = Expression('(Z) * (A + B) * (B + A) * (!D + E + F)')
    chromo_count = len(e.GetVariables())
    popu1 = a._generate_population(chromo_count, 6)
    Selection(popu1)

main()