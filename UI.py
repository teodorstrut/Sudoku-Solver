from time import time

from Controller import Controller


class UI:
    def __init__(self):
        self.__ctrl=Controller()

    def printMenu(self):
        print("Welcome to sudoku solver!")
        print("Options:")
        print("0:exit")
        print("1:Breadth First Search method")
        print("2:Best First Search method")

    def runBfs(self):
        startClock = time()
        for i in self.__ctrl.BFS().getValues():
            print(i)
        print('execution time = ', time() - startClock, " seconds")

    def runBestfs(self):
        startClock = time()
        for i in self.__ctrl.BestFS().getValues():
            print(i)
        print('execution time = ', time() - startClock, " seconds")

    def run(self):
        while True:
            self.printMenu()
            try:
                command = int(input(">>"))
                if command == 0:
                    break
                elif command == 1:
                    self.runBfs()
                elif command == 2:
                    self.runBestfs()
            except:
                print('invalid command')

ui=UI()
ui.run()