import numpy as np
import random
import pandas as pd

def estocasticMatrix(n):
    a = 1
    b = 10
    matrix = (b-a)*np.random.random_sample((n,n)) +a
    #columnas
    for i in range(n):
        for j in range(n):
            if i == j:
                matrix[i][j] = 0.0
    for x in range(n):
        matrix[x] = matrix[x]/ np.sum(matrix[x])
    for index, value in enumerate(matrix):
        print(index +1, value)
    print(" ")
    return(matrix)

def createEnemi(n):
    print("Number of warriors for each group")
    values = []
    for i in range(n):
        print("Enemies", (i+1), 30)
        values.append(30)
    enemis = dict(list(enumerate(values)))
    #Print dicctionary key enemy and value warriors
    #print(enemis)
    print("============================ ")
    print(" ")
    return enemis

def attack(n, matrix, col, matrixEnemis):
    maximum = 0
    row = matrix[col]
    rowSort = np.sort(row, axis=0)
    interval = []
    intervals = []
    dicKey = 0
    arrayKeys = []
    annihilatedTeam = 0
    g = 0
    number = random.uniform(0,1)
    #key_list = list(matrixEnemis.keys())
    for element in rowSort:
        interval.append(element)
    interval.append(1.0)
    for r in range(n):
        allInterval = pd.Interval(interval[r], interval[r+1])
        has = number in allInterval
        if has == True:
            intervals.append(r)
        #print(allInterval,allInterval.length )
    print(intervals)
    arrayValues  = matrixEnemis.values()
    while all(x >= 0 for x in arrayValues):
        for index, value in enumerate(intervals):
            dicKey = value
            arrayKeys.append(dicKey)
        #print("arrayKeys",arrayKeys)
        for elementKey in arrayKeys:
            key = elementKey
            if col == elementKey and elementKey != 0:
                matrixEnemis[elementKey-1] = matrixEnemis[elementKey-1]-1
                g =  matrixEnemis[elementKey-1]
                gr = list(matrixEnemis.keys())[list(matrixEnemis.values()).index(g)]
            elif col == elementKey and elementKey == 0:
                matrixEnemis[elementKey+1] = matrixEnemis[elementKey+1]-1
                g = matrixEnemis[elementKey+1]
                gr = list(matrixEnemis.keys())[list(matrixEnemis.values()).index(g)]
                     
            elif col != elementKey :
                matrixEnemis[elementKey] = matrixEnemis[elementKey]-1
                g = matrixEnemis[elementKey]
                gr = list(matrixEnemis.keys())[list(matrixEnemis.values()).index(g)]
            
        print("attack of enemies", col+1 , "to Group" , gr+1)
        for key in matrixEnemis:
            print("Group", key+1, ':', matrixEnemis[key])
    for index, value in matrixEnemis.items():
        if value <= 0:
            annihilatedTeam = index+1
            print("Group",annihilatedTeam,"is annihilated!")
        
        
    print("============================ ")
    return annihilatedTeam
        

        

def main():
    n = int(input("Enter the number of team = "))
    matrix = estocasticMatrix(n)
    matrixEnemis = createEnemi(n)
    attack(n, matrix, random.randint(0, n-1), matrixEnemis)
    
    
    
if __name__=="__main__":
    main()
