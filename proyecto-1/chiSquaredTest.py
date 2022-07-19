import chiFrequencyTable as freq
from tabulate import tabulate
def chiSquaredTest(filename, digits):
    intervals = []
    for i in range(10):
        intervals.append(round(0.1*i + 0.1, 1))

    observed = freq.getChiFrequencyTable(digits, filename, 10, 0.1, 0, 1)
    expected = sum(observed.values()) / 10

    test_value = 16.9190

    category_results = {}
    for category, number in zip(observed.keys(), observed.values()):
        category_results[category] = round(((number - expected) ** 2) / expected, digits)
    results = []

    for category, result, observed, interval in zip(category_results.keys(), category_results.values(),  observed.values(), intervals):
        results.append([interval, observed, expected, result])

    print()
    print("Chi squared test:")
    print(tabulate(results, headers=["Intervals", "Observed", "Expected", "(O - E)^2 / E"]))
    chi_squared = round(sum(category_results.values()), digits)
    print()
    print("Chi squared:", chi_squared)
    print()
    print('H0: Appereance of the numbers is random')
    print('H1: Appereance of the numbers is not random')
    if chi_squared < test_value:
        print("Since", chi_squared, "<", test_value, "H0 is not rejected ")
    else:
        print("Since", chi_squared, " >", test_value, "H0 is rejected ")