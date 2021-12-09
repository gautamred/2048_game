import random
from copy import deepcopy

class Grid:
    def __init__(self,size=4):
        self.size=size
        self.grid = [[0 for cell in range(size)] for row in range(size)]
        self.freeCells = [1]*(size*size)
        self.isGridFull = 0
    
    def pushZero(self,arr,side):
        if side=="left":
            count = 0
            for i in range(len(arr)):
                if arr[i]!=0:
                    arr[count] = arr[i]
                    count+=1
        
            while(count<len(arr)):
                arr[count] = 0
                count+=1

        elif side=="right":
            count = len(arr)-1
            for i in range(len(arr)-1,-1,-1):
                if arr[i]!=0:
                    arr[count] = arr[i]
                    count-=1
            
            while(count>=0):
                arr[count] = 0
                count-=1


    def swipeUp(self):
        for i in range(self.size):
            arr = [row[i] for row in self.grid]
            self.pushZero(arr,"left")

            for j in range(len(arr)-1):
                if arr[j]==arr[j+1] and arr[j]!=0:
                    arr[j] += arr[j+1]
                    arr[j+1]=0
            
            self.pushZero(arr,"left")

            for k in range(len(arr)):
                self.grid[k][i] = arr[k]
                if self.grid[k][i] == 0:
                    self.freeCells[(k*self.size)+i] = 1
                else:
                    self.freeCells[(k*self.size)+i] = 0
    
    def swipeLeft(self):
        for i in range(self.size):
            arr = self.grid[i]
            self.pushZero(arr,"left")

            for j in range(len(arr)-1):
                if arr[j]==arr[j+1] and arr[j]!=0:
                    arr[j] += arr[j+1]
                    arr[j+1]=0
            
            self.pushZero(arr,"left")
            self.grid[i] = arr

            for k in range(len(arr)):
                if arr[k] == 0:
                    self.freeCells[(i*self.size)+k] = 1
                else:
                    self.freeCells[(i*self.size)+k] = 0
    
    def swipeDown(self):
        for i in range(self.size):
            arr = [row[i] for row in self.grid]
            self.pushZero(arr,"right")

            for j in range(len(arr)-1,0,-1):
                if arr[j]==arr[j-1] and arr[j]!=0:
                    arr[j] += arr[j-1]
                    arr[j-1]=0
                    
            
            self.pushZero(arr,"right")

            for k in range(len(arr)):
                self.grid[k][i] = arr[k]
                if self.grid[k][i] == 0:
                    self.freeCells[(k*self.size)+i] = 1
                else:
                    self.freeCells[(k*self.size)+i] = 0
    
    def swipeRight(self):
        for i in range(self.size):
            arr = self.grid[i]
            self.pushZero(arr,"right")

            for j in range(len(arr)-1,0,-1):
                if arr[j]==arr[j-1] and arr[j]!=0:
                    arr[j] += arr[j-1]
                    arr[j-1]=0

            
            self.pushZero(arr,"right")
            self.grid[i] = arr

            for k in range(len(arr)):
                if arr[k] == 0:
                    self.freeCells[(i*self.size)+k] = 1
                else:
                    self.freeCells[(i*self.size)+k] = 0
    
    def addRandom(self):
        
        randNum = random.randint(0,1)

        if randNum==0:
            randNum = 2
        else:
            randNum = 4
        
        arrWithOnes = [i for i in range(self.size*self.size) if self.freeCells[i]==1]

        if len(arrWithOnes)==0:
            self.isGridFull = 1
            print("GRID FULL!!!")
            return

        randPosition = random.randrange(len(arrWithOnes))
        randPosition = arrWithOnes[randPosition]

        self.freeCells[randPosition] = 0
        col = randPosition%self.size
        row = int((randPosition-col)/self.size)
        self.grid[row][col] = randNum
    
    def endGame(self):
        arrWithOnes = [i for i in range(self.size*self.size) if self.freeCells[i]==1]

        for i in arrWithOnes:
            col = i%self.size
            row = int((i-col)/self.size)
            if self.grid[row][col] == 2048:
                self.isGridFull = 1
                print("REACHED 2048!!!")
        
        
        

    def printGrid(self):
        print("--------------------")
        for i in range(self.size):
            for j in range(self.size):
                if self.grid[i][j] !=0:
                    print("%4d" % (self.grid[i][j]),end="|")
                else:
                    print("    ",end="|")
            print()
            print("--------------------")


print("---------------WELCOME!---------------")
print("1) PLAY")
print("2) EXIT")
while True:  
    try:
        option = int(input())
    except ValueError:
        print("Provide valid option")
        continue
    if option == 1 or option == 2:
        break
    else:
        print("Provide valid option")

if option == 1:
    print("CONTROLS\n1) Moves the cells left\n2) Moves the cells right\n3) Moves the cells up\n4) Moves the cells down")
    gameGrid = Grid()
    gameGrid.addRandom()
    gameGrid.addRandom()
    gameGrid.printGrid()

    while(gameGrid.isGridFull == 0):
        prevState = deepcopy(gameGrid.grid)
        print("Enter direction: ")
        try:
            ip = int(input())
        except ValueError:
            print("Invalid input! Please provide a number from 1 to 4")
            continue
        if ip == 1:
            gameGrid.swipeLeft()
        elif ip==2:
            gameGrid.swipeRight()
        elif ip==3:
            gameGrid.swipeUp()
        elif ip==4:
            gameGrid.swipeDown()
        else:
            gameGrid.printGrid()
            continue
        
        if gameGrid.grid == prevState:
            print(prevState)
            gameGrid.printGrid()
            continue
        gameGrid.endGame()
        gameGrid.addRandom()
        gameGrid.printGrid()

elif option == 2:
    print("------THANK YOU FOR PLAYING!------")
    pass
            
