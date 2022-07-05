
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
    for i in range(len(signList) - 1):
        if signList[i+1] != signList[i]:
            numberStreak = numberStreak +1
        if signList[i+1] == signList[i]:
            numberStreak = numberStreak + 1
    print(numberStreak)
    return numberStreak

def getExpectedValue(totalSign):
    formula = (2(totalSign)-1)/3
    return formula

def getVarinece(totalSign):
    resultFormula = ((16(totalSign))-29)/90
    return resultFormula

def getRunTestResult(expVal,variVal, numberStreak):
     
    resultFormula = (numberStreak-expVal)/variVal
    print(resultFormula)
    return resultFormula