"""
    findSlow.py
    Colin Fausnaught
"""

import time

def medianFunc(lst):
    lst.sort()
    length = len(lst)
    median = 0
    if length % 2 == 1:
        median = lst[length//2]
    else:
        median = (lst[length//2] + lst[(length//2) - 1]) / 2

    return median

def fileManagement():
    f = open("testDataSet10K.txt", encoding='utf-8')
    lst = []
    x = 0
    for line in f:
        if x <= 9:
            lst += int(line[11:])
        elif x <= 99:
            lst += int(line[12:])
        elif x <= 999:
            lst += int(line[13:])
        elif x <= 9999:
            lst += int(line[14:])

        x += 1
        
    f.close()
    print(lst)
    
def main():
    starttime = time.clock()
    fileManagement()
    print(medianFunc([1,3,5,9,2]))
    print(time.clock() - starttime)

main()
