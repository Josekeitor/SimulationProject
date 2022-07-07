import chiSquaredTest as chi
import numberGenerator as numGen
import runsTest as runT

from pathlib import Path

dir_input = Path('InputFiles')
runs_data = Path(dir_input / 'runs_data.txt')
chi_data = Path(dir_input / 'chi_data-2.txt')

print(numGen.randomNumbers(6, 32, 3, 80, 10))
print("H0 is not rejected " if chi.chiSquaredPassed(
    chi_data, 4) else "H0 is rejected")

runT.runsTest(runs_data, 4)
