import os
import random
from _chromosome import Chromosome
from _expression import Expression

def Selection(population):
    #SELECT TWO FROM POPULATION FOR CROSSOVER
    #RETURN A NEW LIST OF CHROMOSOME 
    p1 = population[0] # 1ST MOST FIT

    random_parent = random.randint(1, len(population) - 1) #RANDOM NUMBER BETWEEN SECOND PARENT, AND LAST PARENT 
    p2 = population[random_parent] # PICK A RANDOM SECOND PARENT
    new_population = [p1,p2] #CREATE A LIST WITH THE NEW POPULATION
    return new_population #RETURN THE POPULATION

def Crossover(pivot, c1, c2):
    #RETURN TWO CHROMOSOME OBJECTS
    C1 = "" #EMPTY STRING
    C2 = "" #EMPTY STRING

    for i in range(0, pivot): #ADD HEAD OF PARENT ONE TO CHILD ONE, ADD HEAD OF PARENT TWO TO CHILD TWO
        C1 += c1._info[i]
        C2 += c2._info[i]
    
    for i in range(pivot, len(c1._info)): #ADD TAIL OF PARENT TWO TO CHILD ONE, ADD TAIL OF PARENT ONE TO CHILD TWO
        C1 += c2._info[i] 
        C2 += c1._info[i]

    c1 = Chromosome(C1) #INITALIZE A CHROMOSOME OBJECT WITH 'C1' AS ITS INFORMATION
    c2 = Chromosome(C2) #INITALIZE A CHROMOSOME OBJECT WITH 'C2' AS ITS INFORMATION

    return [c1, c2] #RETURN A LIST WITH 'c1' AND 'c2'

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
        else:
            mutatedChromo += c._info[i] #SAVE THE ORIGINAL INFO
    
    return mutatedChromo #RETURN THE MUTATED CHROMOSOME'S INFORMATION