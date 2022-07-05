import ChiSquaredTest as chi
import numberGenerator as numGen

print(numGen.randomNumbers(6, 32, 3, 80, 10))
print("H0 is not rejected " if chi.chiSquaredPassed('chi_data-2.txt', 4) else "H0 is rejected")
