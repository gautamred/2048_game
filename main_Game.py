import random

class Grid:
    def __init__(self,size=4):
        self.size=size
        self.grid = [[0 for cell in range(size)] for row in range(size)]
        self.freeCells = [1]*(size*size)
    
    def pushZeroCol(self,arr,side):
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
            self.pushZeroCol(arr,"left")

            for j in range(len(arr)-1):
                if arr[j]==arr[j+1] and arr[j]!=0:
                    arr[j] += arr[j+1]
            
            self.pushZeroCol(arr,"left")

            for k in range(len(arr)):
                self.grid[k][i] = arr[k]
                if self.grid[k][i] == 0:
                    self.freeCells[(k*self.size)+1] = 1
                else:
                    self.freeCells[(k*self.size)+1] = 0
    
    def swipeLeft(self):
        for i in range(self.size):
            arr = self.grid[i]
            self.pushZeroCol(arr,"left")

            for j in range(len(arr)-1):
                if arr[j]==arr[j+1] and arr[j]!=0:
                    arr[j] += arr[j+1]
            
            self.pushZeroCol(arr,"left")
            self.grid[i] = arr
    
    def swipeDown(self):
        for i in range(self.size):
            arr = [row[i] for row in self.grid]
            self.pushZeroCol(arr,"right")

            for j in range(len(arr)-1,0,-1):
                if arr[j]==arr[j-1] and arr[j]!=0:
                    arr[j] += arr[j-1]
            
            self.pushZeroCol(arr,"right")

            for k in range(len(arr)):
                self.grid[k][i] = arr[k]
                if self.grid[k][i] == 0:
                    self.freeCells[(k*self.size)+1] = 1
                else:
                    self.freeCells[(k*self.size)+1] = 0
    
    def swipeRight(self):
        for i in range(self.size):
            arr = self.grid[i]
            self.pushZeroCol(arr,"right")

            for j in range(len(arr)-1,0,-1):
                if arr[j]==arr[j-1] and arr[j]!=0:
                    arr[j] += arr[j-1]
            
            self.pushZeroCol(arr,"right")
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

        randPosition = random.randrange(len(arrWithOnes))
        randPosition = arrWithOnes[randPosition]

        self.freeCells[randPosition] = 0
        col = randPosition%self.size
        row = (randPosition-col)/self.size
        self.grid[row][col] = randNum

        
                
            
