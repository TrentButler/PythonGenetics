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


#NEEDS WORK
#WILL FIND SOLUTION, BUT WILL NOT FALL OUT OF EXECUTION
#LN118 'self.is_finished = self._determine_solution(expression)'
class Algorithm(object):
    def __init__(self):
        self.data = []
        self.generation = 1
        self.population = []
        self.population_scored = []
        self.is_finished = False
        self._file_dump = open('algo_dump.txt', 'w+')

    def _generate_population(self, chromo_length, count):
        population = []
        for x in range(0, count, 1):
            c = Chromosome("") # CREATE NEW CHROMOSOME
            c._generate(chromo_length, True) #INITIALIZE THE CHROMOSOME'S VALUES RANDOMLY
            population.append(c)
        return population

    def _determine_fitness(self, expression):
        #ITERATE THROUGHT THE LIST OF CHROMOSOMES, 
        #   - ASSIGN A SCORE BASED ON CLOSENESS TO THE SOLUTION OUT OF ONE-HUNDRED (100)
        #   - SORT 'population' BASED ON HIGHEST FITNESS SCORE
        
        for chromo in self.population:
            expression.expression = expression._original_expression
            expression.Injection(chromo._getInfo()) #INJECT THE INFORMATIION FROM THE CHROMOSOME INTO THE EXPRESSION
            
            pairs = expression._get_pairs() #GET THE ('VARIABLE', 'VALUE') PAIRS FROM THE EXPRESSION

            raw_score = 0 #TOTAL NUMBER OF TRUE VALUES THE CHROMOSOME CONTAINS
            final_score = 0 #FINAL CALCULATED FITNESS SCORE
            chromosome_length = len(chromo._getInfo()) #LENGTH OF THE CHROMOSOME
            for pair in pairs:
                value = pair[1] #TRUE/FALSE VALUE
                variable = pair[0] #STRING REPRESENTATION OF VARIABLE (a-z A-Z) or (!a-!z !A-!Z) 
                
                if('!' in variable):
                    if(value is '0'): #CHECK IF THIS POSITION IS FALSE
                        raw_score += 1 #INCREMENT THIS CHROMOSOME'S SCORE
                else:
                    if(value is '1'): #CHECK IF THIS POSITION IS TRUE
                        raw_score += 1 #INCRENMENT THIS CHROMOSOME'S SCORE

                
            
            final_score = (float(raw_score) / chromosome_length) * 100 #FITNESS SCORE CALCULATION

            scored_chromo = (chromo, final_score) #CREATE A NEW CHROMOSOME,SCORE PAIR
            self.population_scored.append(scored_chromo) #APPEND NEW PAIR TO 'population_scored' LIST

        self.population_scored.sort(cmp=None, key=lambda x: x[1], reverse=True) #SORT THE POPULATION BY THE HIGHEST SCORE
        self.population = [] #CLEAR OUT THE POPULATION
        for c in self.population_scored:
            self.population.append(c[0]) #REPLACE WITH THE SORTED CHROMOSOME
            
    def _determine_solution(self, expression):
        #RETURN TRUE IF HIGHEST SCORED CHROMOSOME IS THE SOLUTION
        # - FALSE IF NOT THE SOLUTION
        s1 = self.population[0] #HIGHEST SCORED CHROMOSOME

        expression.expression = expression._original_expression
        expression.Injection(s1._getInfo())

        return expression._test_expression() #RETURN RESULT

    def _dump_info(self):
        self._file_dump.write('\n')

        self._file_dump.write('ALGORITHM FINISHED?: ' + str(self.is_finished) + '\n')
        for chromo_pair in self.population_scored:
           dump = (chromo_pair[0]._getInfo(), str(chromo_pair[1]), 'GENERATION: ' + str(self.generation))
           self._file_dump.write(str(dump) + '\n')
    def _print_info(self):
        os.system('cls')

        print('ALGORITHM FINISHED?: ' + str(self.is_finished) + '\n')
        for chromo_pair in self.population_scored:
           dump = (chromo_pair[0]._getInfo(), str(chromo_pair[1]), 'GENERATION: ' + str(self.generation))
           print(str(dump) + '\n')

    def _run_algorithm(self, expression):
        #DETERMINE CHROMOSOME COUNT
        c_count = len(expression.GetVariables())
        self.population = self._generate_population(c_count, 4)

        while not self.is_finished:
            print 'GENERATION: ' + str(self.generation)
            if(self.generation >= 1000):
                #self.is_finished = True
                self._dump_info()
                return

            self._determine_fitness(expression)
            self.is_finished = self._determine_solution(expression)
            self._dump_info() #OUTPUT INFORMATION
            #self._print_info() 
            
            if(self.is_finished):
                print 'SOLUTION: ' + self.population[0]._getInfo()
                self._dump_info()
                return

            # random_pivot = random.randint(0, c_count) #RANDOM CROSSOVER PIVOT POINT BETWEEN 0 AND LENGTH(CHROMOSOME)
            # random_mutation_rate = random.randint(0, 100) #RANDOM MUTATION RATE BETWEEN 0-100
            pivot = int(c_count / 2)
            mutation_rate = 25

            current_generation = Selection(self.population) #SELECT PARENTS
            self.population = []
            self.population = Crossover(pivot, current_generation[0], current_generation[1]) #PERFORM CROSSOVER
            self.generation += 1
            for chromo in self.population:
                chromo._info = Mutation(mutation_rate, chromo) #PERFORM MUTATION
                #self.population.append(chromo) #ADD THE CHROMOSOME TO THE POPULATION
        
        self._file_dump.close() #CLOSE THE OPENED FILE AFTER ALGORITHM IS FINISHED


def main():
    a = Algorithm()
    e = Expression('(a) * (b) * (c) * (!d) * (!e) * (!f)')
    #e.LoadRandomExpression()
    a._run_algorithm(e)
    a._file_dump.close()
    print 'DONE'
    

main()