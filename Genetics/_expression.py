import os

class Expression(object):
    def __init__(self, expression):
        self.data = []
        self.expression = expression.lower()
        self.py_expression = self.GetPyExpression()
        self.pairs = []
        self.variables = []
        self.clauses = []
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


        self.variables = list(set(rawVariables)) #REMOVES DUPLICATES
        return self.variables #RETURN A LIST
    
    def GetPairs(self):
        #FIND THE PAIRS FROM 'expression'
        #NO DUPLICATES
        #TESTCASE = (A + B) * (B + C) * (!D + E + F)
        rawPairs = self.GetVariables()
        pairs = []
        for var in rawPairs:
            pair = (str(var), "")
            pairs.append(pair)
        
        self.pairs = pairs
        return self.pairs #RETURN A LIST

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
                    var = pair[0]
                    value = pair[1]
                    if(char is var):
                        new_expression += value
                        
            else:
                new_expression += char
        
        self.expression = new_expression
        self.py_expression = self.GetPyExpression()
        
    def TestExpression(self):
        print 'result: ' + str(bool(eval(self.py_expression)))


def main():
    e = Expression('(z) * (a + b) * (b + a) * (!d + e + f)')
    e.Injection('110111')
    e.PrintInfo()
    e.TestExpression()

main()