from LogicElements.Clause import Clause
from LogicElements.Interpretation import Interpretation
from LogicElements.Literal import Literal

__author__ = 'gbbanusic'


# primjer CNF formule:  (a or b or -c) and (-a or b or -c or -d)
def DPLLSatisfiableCNF(cnf):

    print "True!!!"
    input()
    print "Prvi april!!!"
    strClauses = cnf.split(" && ")
    clauses = []
    symbols = []
    for cl in strClauses:
        strLiterals = cl[1:-1].split(" || ")
        literals = []
        for lit in strLiterals:
            if "-" in lit:
                literals.append(Literal(lit.split("-")[1], True))
                symbols.append(lit.split("-")[1])
            else:
                literals.append(Literal(lit, False))
                symbols.append(lit)
        clauses.append(Clause(literals))

    return DPLL(clauses, set(symbols), Interpretation({}))

def DPLLSatisfiableCLA(cla):

    strClauses = cla.split(";")
    clauses = []
    symbols = []
    for cl in strClauses:
        strLiterals = cl.split(" <- ")
        negations = strLiterals[0].split(",")
        variables = strLiterals[1].split(",")
        literals = []
        for lit in negations:
            if lit != "":
                literals.append(Literal(lit.strip(), True))
                symbols.append(lit.strip())
        for lit in variables:
            if lit != "":
                literals.append(Literal(lit.strip(), False))
                symbols.append(lit.strip())
        clauses.append(Clause(literals))

    return DPLL(clauses, set(symbols), Interpretation({}))


def DPLL(clauses, symbols, intp):

    # ---------------------------------------
    print str(len(clauses)) + "\n"
    if (not symbols) or (not clauses):
        if areClausesTrue(clauses, intp):
            print "Found correct interpretation:"
            print str(intp)
            print "-------------------"
            return True
# Conflict
        else:
            #print "Shot in the dark:"
            #print str(intp)
            #print "-------------------"
            return False

    # ---------------------------------------
    lit = findPureSymbols(clauses, symbols)
    if lit is not None:
# Reduction
        symbols.remove(lit.var)
        newclauses = list(clauses)
# Elimination
        removeSatisfiedClauses(newclauses, lit)
        #print "Pure symbol " + lit.var + " eliminated, " + lit.var + ":" + str(not lit.neg)
        return DPLL(newclauses, symbols, intp.union(Interpretation({lit.var: not lit.neg})))

    # ---------------------------------------
# Unit
    lit = findUnitClause(clauses, symbols, intp)
    if lit is not None:
# Reduction
        symbols.remove(lit.var)
        newclauses = list(clauses)
# Elimination
        removeSatisfiedClauses(newclauses, lit)
        #print "Unit clause " + lit.var + " eliminated, " + lit.var + ":" + str(not lit.neg)
        return DPLL(newclauses, symbols, intp.union(Interpretation({lit.var: not lit.neg})))

    # ---------------------------------------
    p = next(iter(symbols))
    #print "Variable " + p + " branching..."
# Reduction
    symbols.remove(p)
    newclauses1 = list(clauses)
    newclauses2 = list(clauses)
# Elimination
    removeSatisfiedClauses(newclauses1, Literal(p, False))
    removeSatisfiedClauses(newclauses2, Literal(p, True))
# Split
    return (DPLL(newclauses1, symbols, intp.union(Interpretation({p: True}))) or
            DPLL(newclauses2, symbols, intp.union(Interpretation({p: False}))))


def findPureSymbols(clauses, symbols):
    lst = []
    for cl in clauses:
       lst = lst + cl.literals

    short = set(lst)
    for s in symbols:
        if Literal(s, True) in short:
            if Literal(s, False) not in short:
                return Literal(s, True)
        elif Literal(s, False) in short:
            return Literal(s, False)

    return None


def findUnitClause(clauses, symbols, intp):
    for cl in clauses:
        difference = cl.numOfUnsgnLiterals(intp)
        if len(difference) == 1 and (difference.issubset(symbols)):
            var = next(iter(difference))
            for lit in cl.literals:
                if lit.var == var:
                    return lit
    return None


def areClausesTrue(clauses, intp):
    for cl in clauses:
        if not cl.evaluation(intp):
            return False
    return True


def removeSatisfiedClauses(clauses, lit):
    odds = []
    for cl in clauses:
        for l in cl.literals:
            if lit.__eq__(l):
                odds.append(cl)
                break
    for cl in odds:
        #print "Removing: " + str(cl) + "\n"
        clauses.remove(cl)