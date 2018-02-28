import os
import random

class Chromosome(object):
    def __init__(self, info):
        self._info = str(info) #MAKE SURE ITS A STRING

    def _generate(self, count, randomize): #INITILIZE THE CHROMOSOME TO ALL (0)s IF 'RANDOMIZE' IS FALSE
        self._info = ""
        if not randomize:
            for i in range(0, count, 1):
                self._info += str(i)
        else:
            for i in range(0, count, 1):
                x = random.randint(0, 1)
                self._info += str(x)

    def _getInfo(self):
        return self._info

    def _printInfo(self):
        print self._info

def main():
    c = Chromosome('111111')
    print c._printInfo()