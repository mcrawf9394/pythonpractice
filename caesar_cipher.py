def caesar_cipher(str, shift):
    charList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    newStr = ''
    for x in str:
        isUpper = x.upper() == x
        currentNum = charList.index(x.lower()) if x.lower() in charList else -1
        if currentNum == -1:
            newStr = newStr + x
        else:
            currentNum = currentNum + shift
            if currentNum > len(charList):
                currentNum = currentNum - len(charList)
            newChar = charList[currentNum]
            if isUpper:
                newChar = newChar.upper()
            newStr = newStr + newChar
    return newStr
print(caesar_cipher("What a string!", 5))