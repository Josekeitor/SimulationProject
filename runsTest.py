def checkSign(list):
    signList = []
    for i in range(len(list) - 1):
        if list[i + 1] < list[i]:
            signList.append("+")
        else:
            signList.append("-")
    print(signList)
    return signList 

def countSignNumber(signList):
    signNumber = len(signList)
    print(signNumber)
    return signNumber
    
def getStreak(signList):
    numberStreak = 0
    for i in range(len(signList)):
        if i == 0 or signList[i] !=signList[i-1]:
            numberStreak = numberStreak + 1
    print(numberStreak)
    return numberStreak

def getExpectedValue(numberStreak):
    formula = ((2*numberStreak)-1)/3
    return formula

def getVarinece(totalSign):
    resultFormula = ((16*totalSign)-29)/90
    return resultFormula

def getRunTestResult(expVal,variVal, numberStreak):
     
    resultFormula = (numberStreak-expVal)/variVal
    tableValue = 1.96
    print("H0 los numeros aparecen de manera aletoria, H1: los numeros no aparecen de forma aleatroia ")
    print("Estadistico de prueba es:", resultFormula)
    if  abs(resultFormula) < tableValue:
        print("H0 no se rechaza")
    else:
        print("H1 se rechaza")
    return resultFormula