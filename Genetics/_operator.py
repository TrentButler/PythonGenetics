import os
import random
from _chromosome import Chromosome
from _expression import Expression

def Selection(population):
    #DISPLAY ALL OF THE POPULATION
    #SELECT TWO FROM POPULATION FOR CROSSOVER
    #RETURN A NEW LIST OF CHROMOSOME 
    p1 = population[0] # 1ST MOST FIT

    random_parent = random.randint(1, len(population) - 1)
    p2 = population[random_parent] # PICK A RANDOM SECOND PARENT
    new_population = [p1,p2]
    return new_population

def Crossover(pivot, c1, c2):
        #RETURN TWO CHROMOSOME OBJECTS
        C1 = ""
        C2 = ""
        for i in range(0, pivot):
            C1 += c1._info[i]
            C2 += c2._info[i]
        
        for i in range(pivot, len(c1._info)):
            C1 += c2._info[i]
            C2 += c1._info[i]

        c1 = Chromosome(C1)
        c2 = Chromosome(C2)

        return [c1, c2]

def Mutation(mutationRate, c):
    #ITERATE THROUGH THE CHROMOSOME, DETERMINE IF A SPECIFIC SPOT NEEDS TO BE REVERSED
    if mutationRate > 100: #LIMIT THE RATE OF MUTUATION BY 100%
        mutationRate = 100 #IF MUTATION RATE IS GREATER THAN 100%, ASSIGN 100 TO 'mutationRate'

    mutatedChromo = "" 
    for i in range(0, len(c._info)):
        x = random.uniform(0, 100) #GENERATE A RANDOM NUMBER
        if x <= mutationRate: #IF THE RANDOM NUMBER GENERATED IS LESS THAN OR EQUAL TO THE MUTATION RATE, MUTATE THIS SPOT
            m = bool(int(c._info[i])) #TYPECAST AS A BOOLEAN
            mutatedChromo += str(int(not m)) #REVERSE THE RESULT, TYPECAST BACK TO STRING AND APPEND
            #c._info[i] = str(not m)
        else:
            mutatedChromo += c._info[i] #SAVE THE ORIGINAL INFO
    
    return mutatedChromo