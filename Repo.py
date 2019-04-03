from Configuration import Configuration


class Repository:
    def __init__(self):
        self.__initial = self.readFile()

    def getValues(self):
        return self.__initial

    def readFile(self):
        with open('matrix.txt', 'r') as f:
            l = [[int(num) for num in line.split(' ')] for line in f]
        return Configuration(l)

    def expand(self,config):
        mtx = config.getValues()

        for i in range(0,len(mtx)):
            for j in range(len(mtx)):
                if mtx[i][j] == 0:
                    return config.nextConfig(i,j)

    def heuristics(self, x):
        mtx = x.getValues()
        sum=0
        for i in range(0,len(mtx)):
            for j in range(0,len(mtx)):
                if mtx[i][j] == 0:
                    sum = sum+len(x.nextConfig(i,j))
        return sum



