#Take input from User
encryptedValue = []
decryptedValue = []
c = input("1..Upper\n2..Lower\n")
choice = int(c)

if int(choice) == 1:
	text=input("Enter Plain text here in uppercase\n")
	keyString=input("Enter Key\n")
	key = int(keyString)

	#Perform Upper Encryption
	for x in range(len(text)):
		getAscii = ord(text[x])
		getAscii = getAscii + key
		"""if getAscii > 122:
			setAscii = getAscii - 122
			getAscii = setAscii + 96"""
		if getAscii > 90:
			setAscii = getAscii - 90
			getAscii = setAscii + 64
		encryptedValue.append(chr(getAscii))
	print("Encryption is ",encryptedValue)
	
	#Perform  Decryption
	for x in range(len(text)):
		getAscii = ord(encryptedValue[x])
		getAscii = getAscii - key
		"""if getAscii < 97 or getAscii > 122 :
			setAscii = 97 - getAscii
			getAscii = 123 - setAscii"""
		if getAscii < 65:
			setAscii = 65 - getAscii
			getAscii = 91 - setAscii	
		decryptedValue.append(chr(getAscii))
	print("Decryption is ",decryptedValue)	



if int(choice) == 2:	
	text=input("Enter Plain text either in lowercase\n")
	keyString=input("Enter Key\n")
	key = int(keyString)
	
	#Perform Encryption
	for x in range(len(text)):
		getAscii = ord(text[x])
		getAscii = getAscii + key
		if getAscii > 122:
			setAscii = getAscii - 122
			getAscii = setAscii + 96
		"""if getAscii > 90:
			setAscii = getAscii - 90
			getAscii = setAscii + 64 """
		encryptedValue.append(chr(getAscii))
	print("Encryption is ",encryptedValue)
	
	#Perform Decryption
	for x in range(len(text)):
		getAscii = ord(encryptedValue[x])
		getAscii = getAscii - key
		if getAscii < 97 or getAscii > 122 :
			setAscii = 97 - getAscii
			getAscii = 123 - setAscii
		"""if getAscii < 65 or getAscii > 90:
			setAscii = 65 - getAscii
			getAscii = 91 - setAscii	"""
		decryptedValue.append(chr(getAscii))
	print("Decryption is ",decryptedValue)	

