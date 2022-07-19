import chiSquaredTest as chi
import numberGenerator as numGen
import runsTest as runsT

from pathlib import Path

dir_input = Path('InputFiles')
runs_data = Path(dir_input / 'runs_data.txt')
chi_data = Path(dir_input / 'chi_data-2.txt')

print("Random numbers generated: ")
print(numGen.randomNumbers(6, 32, 3, 80, 10))
chi_result = chi.chiSquaredTest(chi_data, 4)
runsT.runsTest(runs_data, 4)
