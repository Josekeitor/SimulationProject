import math


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
        if i == 0 or signList[i] != signList[i-1]:
            numberStreak = numberStreak + 1
    print(numberStreak)
    return numberStreak


def getExpectedValue(numberStreak):
    formula = ((2*numberStreak)-1)/3
    return formula


def getVarinece(totalSign):
    resultFormula = math.sqrt(((16*totalSign)-29)/90)
    return resultFormula


def getRunTestResult(expVal, variVal, numberStreak):
    resultFormula = (numberStreak-expVal)/variVal
    tableValue = 1.96
    print("H0 los numeros aparecen de manera aletoria, H1: los numeros no aparecen de forma aleatoria")
    print("Estadistico de prueba es:", resultFormula)

    return abs(resultFormula) < tableValue


def readList(file_name, decimals):
    file_data = open(file_name, 'r')
    raw_data = []

    for element in file_data.readlines():
        raw_data.append(round(float(element), decimals))

    return raw_data


def runsTestPassed(file_name, decimals):
    list = readList(file_name, decimals)
    result_list = checkSign(list)
    numberStreak = getStreak(result_list)
    totalSign = countSignNumber(result_list)
    expVal = getExpectedValue(totalSign)
    variVal = getVarinece(totalSign)
    return getRunTestResult(expVal, variVal, numberStreak)
