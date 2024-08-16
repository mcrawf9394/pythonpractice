def bubblesort (numList):
    madeChange = True
    while madeChange == True:
        madeChange = False
        for i in range(0, len(numList) - 1):
            if numList[i] > numList[i + 1]:
                (x, y) = (numList[i], numList[i + 1])
                (numList[i], numList[i + 1], madeChange) = (y, x, True)
    return numList
print(bubblesort([4, 3, 78, 2, 0, 2]))
print(bubblesort([55, 66, 1, 4, 2, 3, 99, 98]))