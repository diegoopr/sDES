def permutation(keyList, permTable):
    newList = []
    for i in permTable:
        newList.append(keyList[i])
    
    return(newList)


def xor(toXor, key):
    xored = []
    for i in range(len(key)):
        new = int(toXor[i]) ^ int(key[i])
        xored.append(new)
    
    return xored

#To apply sBoxes we cast from bin to dec the first and last bits
#for the row, and the two middle bits for the col.
#then we turn back into binary and return
def sBoxes(sBox, half):
    row = int("0b" + str(half[0]) + str(half[-1]), 2)
    col = int("0b" + str(half[1]) + str(half[2]), 2)
    
    testbin = bin(sBox[row][col])[2:]
    if len(testbin) < 2:
        testbin = "0" + bin(sBox[row][col])[2:]

    return testbin



#key = "0000011111"
#plainText = "01010101"

#key = "0010010111"
#plainText = "00110110"

#key = "0000000000"
#plainText = "00000000"

key = "1111111111"
plainText = "11111111"

#key = "1010000010"
#plainText = "10010111" 

keyList = list(key)

#different tables used for encryption
p4table = [1, 3, 2, 0]
p8table = [5, 2, 6, 3, 7, 4, 9, 8]
p10table = [2, 4, 1, 6, 3, 9, 0, 8, 7, 5]
ipTable = [1, 5, 2, 0, 3, 7, 4, 6]
epTable = [3, 0, 1, 2, 1, 2, 3, 0]
invTable = [3, 0, 2, 4, 6, 1, 7, 5]

s0 = [[1, 0, 3, 2], [3, 2, 1, 0], [0, 2, 1, 3], [3, 1, 3, 2]]
s1 = [[0, 1, 2, 3], [2, 0, 1, 3], [3, 0, 1, 0], [2, 1, 0, 3]]

#Key Generation:
#1. We permutate with p10table
#2. We divide the list in two halves. 
keyList = permutation(keyList, p10table)
leftHalf = keyList[:5]
rightHalf = keyList[5:]

#3. We apply one bit left-shift to each half.
#cool way of shifting i discovered
leftHalf.append(leftHalf.pop(0))
rightHalf.append(rightHalf.pop(0))

#4. We combine both keys and permutate them with p8table
#That's key1
keyList = leftHalf + rightHalf
keyOne = permutation(keyList, p8table)
#print(keyOne)

#5. Using the output of step 3, we now do a 2 bit left-shift.
leftHalf.append(leftHalf.pop(0))
leftHalf.append(leftHalf.pop(0))
rightHalf.append(rightHalf.pop(0))
rightHalf.append(rightHalf.pop(0))

#6. Combined the keys and then permutated them with p8table
keyList = leftHalf + rightHalf
keyTwo = permutation(keyList, p8table)
#print(keyTwo)


#==========================================================#
#On to the actual encription
#1. Initial Permutation
cyphered = []
cyphered = permutation(plainText, ipTable)

#2. We divide the above 8 bit block into two
#We also expand the rightHalf with the epTable
#then we XOR it with keyOne
leftHalf = cyphered[:4]
rightHalf = cyphered[4:]


rightExpand = permutation(rightHalf, epTable)


xored = xor(rightExpand, keyOne)
xorLeft = xored[:4]
xorRight = xored[4:]

coordL = sBoxes(s0, xorLeft)
coordR = sBoxes(s1, xorRight)

boxOut = coordL + coordR
boxOut = permutation(boxOut, p4table)

xorLeft = xor(leftHalf, boxOut)

combined = xorLeft + rightHalf

#3. We divide combine into two halves and swap them
combined[:4], combined[4:] = combined[4:], combined[:4]

#4. We repeat step 2, but after we expand,
#we now use keyTwo for the XOR, and what we use as an input
#now, is the "combined" variable
leftHalf = combined[:4]
rightHalf = combined[4:]

rightExpand = permutation(rightHalf, epTable)

xored = xor(rightExpand, keyTwo) 
xorLeft = xored[:4]
xorRight = xored[4:]

coordL = sBoxes(s0, xorLeft)
coordR = sBoxes(s1, xorRight)

boxOut = coordL + coordR
boxOut = permutation(boxOut, p4table)

xorLeft = xor(leftHalf, boxOut)

combined = xorLeft + rightHalf

rightExpand = permutation(rightHalf, epTable)

xored = xor(rightExpand, keyTwo)
xorLeft = xored[:4]
xorRight = xored[4:]

coordL = sBoxes(s0, xorLeft)
coordR = sBoxes(s1, xorRight)

boxOut = coordL + coordR
boxOut = permutation(boxOut, p4table)

xorLeft = xor(leftHalf, boxOut)

combined = xorLeft + rightHalf

inverse = permutation(combined, invTable)
print("Key:\n" + key + "\n" + "Plaintext:\n" + plainText + "\n" + "Ciphertext: " )
print(inverse)
