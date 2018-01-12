__author__ = 'gbbanusic'


class Clause:
    def __init__(self, literals):
        self.literals = literals

    def __str__(self):
        stri = "("
        for lit in self.literals[: -1]:
            stri = stri + lit.__str__() + " or "
        stri = stri + str(self.literals[-1]) + ")"
        return stri

    def getVariables(self):
        varis = []

        for var in self.literals:
            varis.append(var.variable())

        return set(varis)

    def evaluation(self, intp):
        for lit in self.literals:
            if lit.evaluation(intp):
                return True
        return False

    def numOfUnsgnLiterals(self, intp):
        return set(self.getVariables()) - set(intp.definition())
