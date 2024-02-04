import time
import random
import pandas as pd
from timeit import default_timer as timer

def search_secuential(data,target):
    time_start = timer()
    result = None
    for n in data:
        if(n==target):
            result = n
            break
    time_end = timer()
    return result, time_end-time_start

def search_binary(data,target):
    time_start = timer()
    result = None
    low, high = 0, len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        mid_value = data[mid]
        if mid_value == target:
            result = mid
            break
        elif mid_value < target:
            low = mid + 1
        else:
            high = mid - 1
    time_end = timer()
    return result, time_end-time_start

if __name__ == "__main__":

    SIZE = 1000000
    data = [n for n in range(0,SIZE)]

    SAMPLES = 20
    search_targets = random.sample(data,SAMPLES)

    results = []
    for target_number in search_targets:
        resultSecuential, timeSecuential = search_secuential(data, target_number)
        resultBinary, timeBinary = search_binary(data, target_number)
        results.append([target_number,timeSecuential,timeBinary])

    df = pd.DataFrame(results, columns=['search number','time_by_secuential_search','time_by_binary_search'])
    print(df)