import numpy as np
import random
import pandas as pd

def reshapeMatrix(matrix, newN, teamToRemove):
    removedValues = []

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if j == teamToRemove or i == teamToRemove and i != teamToRemove:
                value = matrix[i][j]
                if value > 0:
                    removedValues.append(value)

    print("Removed Values: ", removedValues)

    newSubMatrix = np.delete(np.delete(matrix, teamToRemove, axis=0), teamToRemove, axis=1)

    for i in range(len(newSubMatrix)):
        for j in range(len(newSubMatrix)):
            if newSubMatrix[i][j] != 0 :
                newSubMatrix[i][j] += removedValues[i] / (len(newSubMatrix) -1)


    return newSubMatrix

def stochasticMatrix(n):
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

def createEnemy(n):
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

def attack(n, matrix, col, matrixEnemies):
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
    arrayValues  = matrixEnemies.values()
    while all(x >= 0 for x in arrayValues):
        for index, value in enumerate(intervals):
            dicKey = value
            arrayKeys.append(dicKey)
        #print("arrayKeys",arrayKeys)
        for elementKey in arrayKeys:
            key = elementKey
            if col == elementKey and elementKey != 0:
                matrixEnemies[elementKey - 1] = matrixEnemies[elementKey - 1] - 1
                g =  matrixEnemies[elementKey - 1]
                gr = list(matrixEnemies.keys())[list(matrixEnemies.values()).index(g)]
            elif col == elementKey and elementKey == 0:
                matrixEnemies[elementKey + 1] = matrixEnemies[elementKey + 1] - 1
                g = matrixEnemies[elementKey + 1]
                gr = list(matrixEnemies.keys())[list(matrixEnemies.values()).index(g)]
                     
            elif col != elementKey :
                matrixEnemies[elementKey] = matrixEnemies[elementKey] - 1
                g = matrixEnemies[elementKey]
                gr = list(matrixEnemies.keys())[list(matrixEnemies.values()).index(g)]
            
        print("attack of enemies", col+1 , "to Group" , gr+1)
        for key in matrixEnemies:
            print("Group", key + 1, ':', matrixEnemies[key])
    for index, value in matrixEnemies.items():
        for key in matrixEnemies:

            if matrixEnemies[key] < 0:
                zeroI = matrixEnemies[key]
                zeroI = 0
                print("Group", key+1, ':', zeroI)
            else:
                print("Group", key+1, ':', matrixEnemies[key])
    for index, value in matrixEnemies.items():
        if value <= 0:
            annihilatedTeam = index+1
            print("Group",annihilatedTeam,"is annihilated!")
            print("Original: ", matrix)
            print("Reshaped: ", reshapeMatrix(matrix, n-1, annihilatedTeam-1))

        
    print("============================ ")
    return annihilatedTeam
        

        

def main():
    n = int(input("Enter the number of team = "))
    matrix = stochasticMatrix(n)
    matrixEnemis = createEnemy(n)
    print('attack return: ', attack(n, matrix, random.randint(0, n-1), matrixEnemis))
    
    
    
if __name__=="__main__":
    main()
