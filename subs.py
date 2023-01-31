import string

# f u all
print("Implementation of substitution cipher method as python")
all_letters = string.ascii_letters

# plain text function
fubuki = {}
key = 4
for i in range(len(all_letters)):
	fubuki[all_letters[i]] = all_letters[(i+key)%len(all_letters)]
aseli= input('Input a text : ')
ciphtext=[]

# Encrypt function
for char in aseli:
	if char in all_letters:
		temp = fubuki[char]
		ciphtext.append(temp)
	else:
		temp =char
		ciphtext.append(temp)

# exec enc function 
exec= "".join(ciphtext)
print("Encrypted text : ",exec)

# Decrypt function
zetauwu = {}	
for i in range(len(all_letters)):
	zetauwu[all_letters[i]] = all_letters[(i-key)%(len(all_letters))]
	
maisan = []
for char in exec:
	if char in all_letters:
		temp = zetauwu[char]
		maisan.append(temp)
	else:
		temp = char
		maisan.append(temp)

# exec dec function 
execc = "".join(maisan)
print("Decrypted text :", execc)
