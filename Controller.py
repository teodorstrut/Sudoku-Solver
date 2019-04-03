from Repo import Repository


class Controller:
    def __init__(self):
        self.__repo = Repository()

    def BFS(self):
        q = [self.__repo.getValues()]
        found = False
        while len(q) > 0 and not found:
            currentState = q.pop(0)
            nr = 0
            for i in currentState.getValues():
                for j in i:
                    if j == 0:
                        nr += 1

            if nr == 0:
                found = False
                return currentState

            q = q + self.__repo.expand(currentState)

    def BestFS(self):

        visited = []
        toVisit = [self.__repo.getValues()]
        while len(toVisit) > 0:
            node = toVisit.pop(0)
            visited = visited + [node]
            nr = 0
            for i in node.getValues():
                for j in i:
                    if j == 0:
                        nr += 1

            if nr == 0:
                return node

            aux = []
            for x in self.__repo.expand(node):
                if x not in visited:
                    aux.append(x)
            aux = [[x, self.__repo.heuristics(x)] for x in aux]
            aux.sort(key=lambda x: x[1])
            aux = [x[0] for x in aux]
            toVisit = aux[:] + toVisit
