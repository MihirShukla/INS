key = input("Enter Key:")
pt = input("Enter Plain Text:")
key = key.replace("j","i") 
lenpt = len(pt)

opt = pt
if (lenpt % 2) != 0:
    pt = pt + "x"

ptGroup = []
j=0
k=2
l = int(len(pt)/2)
for i in range(l):
    ptGroup.append('')
for i in range(l):
    ptGroup[i] = pt[j:k]
    j=j+2
    k=k+2
matrix = []

for i in key:
    if i not in matrix:
        matrix.append(i)

alphabet = "abcdefghiklmnopqrstuvwxyz"

for i in alphabet:
    if i not in matrix:
        matrix.append(i)
matrix = "".join(matrix)
matrixGroup = []

for e in range(5):
		matrixGroup.append('')

matrixGroup[0] = matrix[0:5]
matrixGroup[1] = matrix[5:10]
matrixGroup[2] = matrix[10:15]
matrixGroup[3] = matrix[15:20]
matrixGroup[4] = matrix[20:25]

print(ptGroup)
print(matrixGroup)

def findPosition(char):
    k=0
    for i in range(len(matrixGroup)):
        if char in matrixGroup[i]:
            s = matrixGroup[i]
            for j in s:
                if char in j:
                    return i,k
                k = k + 1

def findCharE(x,xi,y,yi):
    if x != y and xi != yi:
        group1 = matrixGroup[x]
        group2 = matrixGroup[y]
        k1 = group1[yi]
        k2 = group2[xi]
        return k1,k2

    if xi == yi:
        if x == 4:
            x = -1
        if y == 4:
            y = -1
        group1 = matrixGroup[x+1]
        group2 = matrixGroup[y+1]
        
        k1 = group1[xi]  # or k1 = group1[yi]
        k2 = group2[xi]  # or k2 = group2[yi]
        return k1,k2

    if x == y:
        if xi == 4:
            xi = -1
        if yi == 4:
            yi = -1
        group = matrixGroup[x]  # or group = matrixGroup[y]
        k1 = group[xi+1]
        k2 = group[yi+1]
        return k1,k2

def findCharD(x,xi,y,yi):
    if x != y and xi != yi:
        group1 = matrixGroup[x]
        group2 = matrixGroup[y]
        k1 = group1[yi]
        k2 = group2[xi]
        return k1,k2

    if xi == yi:
        if x == 0:
            x = 5
        if y == 0:
            y = 5
        group1 = matrixGroup[x-1]
        group2 = matrixGroup[y-1]
        
        k1 = group1[xi]  # or k1 = group1[yi]
        k2 = group2[xi]  # or k2 = group2[yi]
        return k1,k2

    if x == y:
        if xi == 0:
            xi = 5
        if yi == 0:
            yi = 5
        group = matrixGroup[x]  # or group = matrixGroup[y]
        k1 = group[xi-1]
        k2 = group[yi-1]
        return k1,k2

encry = ""
for i in range(len(ptGroup)):
    z = ptGroup[i]
    x,xi = findPosition(z[0])
    y,yi = findPosition(z[1])
    k1,k2 = findCharE(x,xi,y,yi)
    encry = encry + k1 + k2


enGroup = []
j=0
k=2
l = int(len(encry)/2)
for i in range(l):
    enGroup.append('')
for i in range(l):
    enGroup[i] = encry[j:k]
    j=j+2
    k=k+2
   
decry = ""
for i in range(len(enGroup)):
    z = enGroup[i]
    x,xi = findPosition(z[0])
    y,yi = findPosition(z[1])
    k1,k2 = findCharD(x,xi,y,yi)
    decry = decry + k1 + k2

if len(opt)!=len(pt):
    decry = decry[:-1]
print("Encrypted Text:" + encry)
print("Decrypted Text:" + decry)