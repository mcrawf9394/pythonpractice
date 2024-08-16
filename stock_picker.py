def stock_picker(numList):
    (dif, x, y) = (-1, 0, 1)
    for num in numList:
        partial = numList[numList.index(num) + 1: len(numList)]
        for secondNum in partial:
            if dif < secondNum - num:
                (dif, x, y) = (secondNum - num, numList.index(num), numList.index(secondNum))
    if dif == -1:
        return "Do Not Invest!"
    else:
        return list([x, y])
print(stock_picker([17,3,6,9,15,8,6,1,10]))
print(stock_picker([17, 18]))
print(stock_picker([18, 17, 16, 15]))