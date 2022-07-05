def checkSign(list):
    signList = []
    for i in range(len(list) - 1):
        if list[i + 1] < list[i]:
            signList.append("+")
        else:
            signList.append("-")
    print(signList)
    return signList

def getStreak(signList):
    numberStreak = 0
    for i in range(len(signList) - 1):
        if signList[i+1] != signList[i]:
            numberStreak = numberStreak +1
        if signList[i+1] == signList[i]:
            numberStreak = numberStreak + 1
    print(numberStreak)
    return numberStreak