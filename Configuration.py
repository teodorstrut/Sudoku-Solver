from copy import deepcopy

from math import sqrt


class Configuration:
    """
    Configuration of the puzzle
    """

    def __init__(self, matrix):
        self.__matrix = deepcopy(matrix)

    def getLength(self):
        return len(self.__matrix[1])

    def getValues(self):
        return deepcopy(self.__matrix)

    def nextConfig(self, i, j):
        next = []
        newmatrix = deepcopy(self.__matrix)
        if (newmatrix[i][j] != 0):
            return next
        for x in range(self.getLength() + 1):
            if x not in newmatrix[i]:
                if x not in [row[j] for row in newmatrix]:
                    if x not in self.getSquareElems(i, j):
                        newmatrix[i][j] = x
                        next.append(Configuration(newmatrix))
        return next

    def __str__(self):
        return str(self.__matrix)

    def getSquareElems(self, i, j):
        l = []
        width = sqrt(self.getLength())
        startRow = int(int(i / width) * width)
        startCol = int(int(j / width) * width)
        endRow = int(startRow + width)
        endCol = int(startCol + width)

        for x in range(startRow, endRow):
            for y in range(startCol, endCol):
                l.append(self.__matrix[x][y])
        return l

    def __eq__(self, other):
        if self.__matrix == other.getValues():
            return True
        else:
            return False

# conf = Configuration([[2,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]])
# conf2 = Configuration([[2,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]])
# print(conf==conf2)
# for i in conf.nextConfig(1, 2):
#     print("")
#     for j in i.getValues():
#         print(j)
