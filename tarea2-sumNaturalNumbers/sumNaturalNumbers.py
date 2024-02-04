import sys, getopt
import time
import pandas as pd
from timeit import default_timer as timer

def sumNaturalNumbersFormula(N):
    time_start = timer()
    suma = N*(N+1)/2
    time_end = timer()
    return suma, time_end-time_start

def sumNaturalNumbersIterations(N):
    time_start = timer()
    suma = 0
    for n in range(N+1):
        suma += n
    time_end = timer()
    return suma, time_end-time_start

if __name__ == "__main__":
    numbers = [100,1000,10000,100000]
    results = []
    for number in numbers:
        resultFormula, timeFormula = sumNaturalNumbersFormula(number)
        resultIterations, timeIterations= sumNaturalNumbersIterations(number)
        results.append( [number, resultFormula, timeFormula, timeIterations] )
    df = pd.DataFrame(results, columns=['numbers','sum','time_by_formula','time_by_iterations'])
    print(df)