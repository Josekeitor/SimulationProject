import chiFrequencyTable as freq
def chiSquaredPassed(filename, digits):
    observed = freq.getChiFrequencyTable(digits, filename, 10, 0.1, 0, 1)
    expected = sum(observed.values()) / 10

    test_value = 16.9190

    category_results = {}
    for category, number in zip(observed.keys(), observed.values()):
        category_results[category] = ((number - expected) ** 2) / expected

    print(category_results)
    chi_squared = sum(category_results.values())
    print("Chi squared:", chi_squared)
    return chi_squared < test_value