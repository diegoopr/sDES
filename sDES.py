

def permutation(keyList, permTable):
    newList = []
    for i in permTable:
        newList.append(keyList[i])
    
    return(newList)

def keyGen(keyList):
    p8table = [5, 2, 6, 3, 7, 4, 9, 8]
    p10table = [2, 4, 1, 6, 3, 9, 0, 8, 7, 5]

    keyList = permutation(keyList, p10table)
    leftHalf = keyList[:5]
    rightHalf = keyList[5:]
    
    #cool way of shifting i discovered
    leftHalf.append(leftHalf.pop(0))
    rightHalf.append(rightHalf.pop(0))

    keyList = leftHalf + rightHalf
    keyOne = permutation(keyList, p8table)
    print(keyOne)
    
    leftHalf.append(leftHalf.pop(0))
    leftHalf.append(leftHalf.pop(0))
    rightHalf.append(rightHalf.pop(0))
    rightHalf.append(rightHalf.pop(0))

    keyList = leftHalf + rightHalf
    keyTwo = permutation(keyList, p8table)
    
    print(keyTwo)

    


key = "1010000010"
keyList = list(key)

keyGen(keyList)
