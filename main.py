import chiSquaredTest as chi
import numberGenerator as numGen
import runsTest as runT

print(numGen.randomNumbers(6, 32, 3, 80, 10))
print("H0 is not rejected " if chi.chiSquaredPassed('InputFiles/chi_data-2.txt', 4) else "H0 is rejected")

list = [10,20,5,2,7,15]   
result_list = runT.checkSign(list)
numberStreak = runT.getStreak(result_list)
totalSign = runT.countSignNumber(result_list)
expVal = runT.getExpectedValue(totalSign)
variVal = runT.getVarinece(totalSign)
runT.getRunTestResult(expVal,variVal,numberStreak)
