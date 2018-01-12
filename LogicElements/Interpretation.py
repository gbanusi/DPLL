__author__ = 'gbbanusic'


class Interpretation:

    def __init__(self, map):
        self.map = map

    def __str__(self):
        string = ""
        for k, v in self.map.iteritems():
            string += k + "  " + str(v) + "\n"
        return string

    def definition(self):
        return self.map.keys()

    def getMap(self):
        return self.map

    def union(self, intp):
        temp = Interpretation(self.map.copy())
        temp.getMap().update(intp.getMap())
        return temp

