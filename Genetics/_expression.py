import os
import random

class Expression(object):
    def __init__(self, expression):
        self.data = []
        self.expression = expression
        self._original_expression = self.expression
        self.py_expression = self.GetPyExpression()
        self.pairs = []
        self.variables = []
        self.clauses = []
        self.GetPairs()
        self.GetVariables()
        self.GetClauses()

    def LoadRandomExpression(self):
        #READ IN EACH EXPRESSION FROM FILE 'expressions.txt' INTO A LIST
        #PICK A RANDOM EXPRESSION
        file = open('expressions.txt', 'r')
        all_expressions = list(file)
        count = len(all_expressions)
        i = random.randint(0, count-1)
        expression = all_expressions[i]

        self.expression = expression #ASSIGN NEW EXPRESSION
        self.py_expression = self.GetPyExpression() #UPDATE MEMEBER VARIABLES
        self.GetPairs()
        self.GetVariables()
        self.GetClauses()
    
    def GetPyExpression(self):
        return self.expression.replace('*', 'and').replace('+', 'or').replace('!', 'not ')

    def GetVariables(self):
        #FIND THE VARIABLES FROM 'expression'
        #NO DUPLICATES
        #TESTCASE = (A + B) * (B + C) * (!D + E + F)
        rawVariables = []
        
        for char in self.expression:
            if(ord(char) >= 97 and ord(char) <= 122):
                #VALID VARIABLE
                rawVariables.append(char)
                continue

            if(ord(char) >= 65 and ord(char) <= 90):
                #VALID VARIABLE
                rawVariables.append(char)
                continue


        self.variables = list(set(rawVariables)) #REMOVES DUPLICATES
        self.variables.sort(cmp=None, key=lambda x: x, reverse=False)
        return self.variables #RETURN A LIST
    
    def GetPairs(self):
        #FIND THE PAIRS FROM 'expression'
        #NO DUPLICATES
        #TESTCASE = (A + B) * (B + C) * (!D + E + F)
        
        rawVariables = []
        
        s = '' 
        for char in self.expression:
            if(char is '!'):
                s += '!'
                continue
            if(ord(char) >= 97 and ord(char) <= 122): #LOWERCASE CHECK
                #VALID VARIABLE
                c = ''
                if(s is '!'):
                    c += s
                    c += char
                    rawVariables.append(c)
                    s = ''
                else:
                    rawVariables.append(char)
                continue
            if(ord(char) >= 65 and ord(char) <= 90): #UPPERCASE CHECK
                #VALID VARIABLE
                C = ''
                if(s is '!'):
                    C += s
                    C += char
                    rawVariables.append(C)
                    s = ''
                else:
                    rawVariables.append(char)
                continue
                
        variables = rawVariables #REMOVES DUPLICATES                
        #variables = list(set(rawVariables)) #REMOVES DUPLICATES
        #variables.sort(cmp=None, key=lambda x: x, reverse=False) #SORT THE LIST

        rawPairs = variables
        pairs = []
        for val in rawPairs:
            pair = (val, '')
            pairs.append(pair)

        #AFTER REMOVING DUPLICATES, SORT THE LIST
        # for var in rawPairs: #FIRST PASS, ONLY STRINGS WITHOUT '!'
        #     if(len(var) > 1):
        #         continue
        #     pair = (str(var), "")
        #     pairs.append(pair)

        # for var in rawPairs: #SECOND PASS, ONLY STRINGS WITH '!'
        #     if(len(var) <= 1):
        #         continue
        #     pair = (str(var), "")
        #     pairs.append(pair)

        self.pairs = pairs
        return self.pairs #RETURN A LIST

    def _get_pairs(self):
        return self.pairs

    def GetClauses(self):
        clause = ''
        rawClauses = self.expression
        log = False
        clauses = []
        for c in rawClauses:
            if c is '(':
                clause += c
                log = True
                continue
            if c is ')':
                clause += c
                clauses.append(clause)
                clause = ''
                log = False
                continue
            if log:
                clause += c

        self.clauses = clauses
        return self.clauses

    def PrintInfo(self):
        print 'expression: ' + self.expression
        print 'python expression: ' + self.py_expression
        print 'variables: ' + str(self.variables)
        print 'clauses: ' + str(self.clauses)
        print 'pairs: ' + str(self.pairs)
        
    def Injection(self, values):
        #EXPECTING A STRING' REPRESENTATION OF BOOLEAN VALUES -> values = '00001111'
        
        #INJECTION ON PAIRS
        for i in range(0, len(self.pairs), 1):
            val = values[i]
            old_pair = self.pairs[i]
            new_pair = (old_pair[0], val)
            self.pairs[i] = new_pair

        #INJECTION ON EXPRESIION
        new_expression = ''
        for char in self.expression:
            if(ord(char) >= 97 and ord(char) <= 122):
                #VALID VARIABLE
                for pair in self.pairs:                    
                    raw_var = pair[0]
                    var = ''
                    if(len(raw_var) > 1):
                        var = raw_var[1]
                    else:
                        var = raw_var

                    value = pair[1]
                    if(char is var):
                        new_expression += value
                continue

            if(ord(char) >= 65 and ord(char) <= 90):
                #VALID VARIABLE
                for pair in self.pairs:
                    var = pair[0]
                    value = pair[1]
                    if(char is var):
                        new_expression += value
                continue
                        
            else:
                new_expression += char
                continue
        
        self.expression = new_expression
        self.py_expression = self.GetPyExpression()
        #self.GetPairs()
        #self.GetVariables()
        self.GetClauses()
        
    def PrintTestExpression(self):
        print 'result: ' + str(bool(eval(self.py_expression)))

    def _test_expression(self):
        return bool(eval(self.py_expression))

def main():
    e = Expression('(a) * (b) * (c) * (!d)')

    #e.LoadRandomExpression()
    #e.Injection('1110')
    e.PrintInfo()
    #e.PrintTestExpression()

main()