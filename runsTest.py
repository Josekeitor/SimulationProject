import math


def getSigns(values):
    signs = []

    for i in range(len(values) - 1):
        if values[i + 1] > values[i]:
            signs.append('+')
        else:
            signs.append('-')

    return signs


def countSigns(signs):
    return len(signs)


def getRuns(signs):
    if not signs:
        return 0

    runs = 1

    for i in range(len(signs) - 1):
        if signs[i + 1] != signs[i]:
            runs += 1

    return runs


def getExpectedValue(n, decimals):
    return round(((2 * n) - 1) / 3, decimals)


def getVariance(n, decimals):
    return round(math.sqrt(((16 * n) - 29) / 90), decimals)


def getStandardScore(expectedValue, variance, runs, decimals):
    return round((runs - expectedValue) / variance, decimals)


def getRunsTestResult(zscore, tableValue):
    return abs(zscore) < abs(tableValue)


def readValues(fileName, decimals):
    file_data = open(fileName, 'r')
    raw_data = []

    for element in file_data.readlines():
        raw_data.append(round(float(element), decimals))

    return raw_data


def runsTest(file_name, decimals):
    tableValue = 1.96

    values = readValues(file_name, decimals)
    signs = getSigns(values)
    runs = getRuns(signs)
    n = countSigns(signs)
    expectedValue = getExpectedValue(n, decimals)
    variance = getVariance(n, decimals)
    zscore = getStandardScore(expectedValue, variance, runs, decimals)
    res = getRunsTestResult(zscore, tableValue)

    print('Runs test')
    print('Generated signs')
    print(' '.join(signs))
    print(f'total: {n}')
    print(f'total runs: {runs}')
    print(f'Sigma: {variance}')
    print(f'Zscore: {zscore}')
    print()
    print('H0: Appereance of the numbers is random')
    print('H1: Appereance of the numbers is not random')

    if res:
        print(f'Since |{zscore}| < |{tableValue}|, H0 is not rejected')
    else:
        print(f'Since |{zscore}| > |{tableValue}|, H0 is rejected')
