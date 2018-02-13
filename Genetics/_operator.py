import os
import random
from _chromosome import Chromosome

def Selection(population):
    #DISPLAY ALL OF THE POPULATION
    #SELECT TWO FROM POPULATION FOR CROSSOVER
    #RETURN A NEW LIST OF CHROMOSOME 
    for p in population:
        p._printInfo()

def Crossover(pivot, c1, c2):
        #RETURN TWO CHROMOSOMES
        C1 = ""
        C2 = ""
        for i in range(0, pivot):
            C1 += c1._info[i]
            C2 += c2._info[i]
        
        for i in range(pivot, len(c1._info)):
            C1 += c2._info[i]
            C2 += c1._info[i]

        return [C1, C2]

def Mutation(mutationRate, c):
    #ITERATE THROUGH THE CHROMOSOME, DETERMINE IF THIS SPOT NEEDS TO BE FLIPPED
    if mutationRate > 100: #?????
        mutationRate = 100 #?????

    s = ""
    for i in range(0, len(c._info)):
        x = random.uniform(0, 100)
        if x <= mutationRate:
            m = bool(int(c._info[i])) #TYPECAST AS A BOOLEAN
            s += str(int(not m)) #REVERSE THE RESULT, TYPECAST BACK TO STRING AND APPEND
            #c._info[i] = str(not m)
        else:
            s += c._info[i] #SAVE THE ORIGINAL INFO
    
    return s