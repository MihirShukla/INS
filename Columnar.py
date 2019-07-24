plainText = input("Enter Plain text\n")
plainTextLength = len(plainText)


keyString = input("Enter Key\n")
keyLength = len(keyString)


#--------------------------------Encryption----------------------------
keyList = []

for i in keyString:
	keyList.append(int(i))
keyList.sort()
print(keyList)
encryption = ""
dict = {}

appendLength = len(plainText) % keyLength
print(keyLength - appendLength)
for i in range(keyLength - appendLength):
	plainText = plainText + "#"

plainTextLength = len(plainText) 
for i in range(keyLength):
	for j in range(i,plainTextLength,keyLength):
		encryption = encryption + plainText[j]	
	dict[str(keyList[i])] = encryption
	encryption = "" 

encryptionString = ""	
for i in keyString:
	encryptionString = encryptionString + dict[i]  

	
encryptionList = encryptionString.split("#")
encryptionString = ""
for i in range(len(encryptionList)):
	encryptionString = encryptionString + encryptionList[i]  
print(encryptionString)

print(dict)
	
	
#---------------------------------------Decryption---------------------------

decryptionList = []
lenOfValue = len(dict[str(keyList[0])])



for j in range(lenOfValue):
	for i in range(len(dict)):
		x = dict[str(keyList[i])]
		decryptionList.append(x[j])
	
		
decryptionString = ""

for i in range(len(decryptionList)):
	decryptionString = decryptionString + decryptionList[i]  
		
decryptionString = decryptionString.split("#")
print(decryptionString[0])

