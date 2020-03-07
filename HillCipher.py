import numpy as np 

plainText = "ASM"
key = "PASSWORDS"
# matrix that we fill the key and ciper and plain text 
keyMatrix = [[0] * 3 for i in range(3)]
messageVector = [[0] for i in range(3)]
cipherMatrix = [[0] for i in range(3)] 
decipherMatrix = [[0] for i in range(3)] 

# loop to fill the key in matrix 
k = 0
for i in range(3): 
    for j in range(3): 
        keyMatrix[i][j] = ord(key[k])-65
        k+=1

# loop to fill the plaintext in matrix 
for i in range(3): 
        messageVector[i][0] = ord(plainText[i])-65

# loop to multiplay the number and fill it in cipher matrix 
for i in range(3): 
    for j in range(1): 
        cipherMatrix[i][j] = 0
        for x in range(3): 
            cipherMatrix[i][j] += (keyMatrix[i][x] * 
                                       messageVector[x][j]) 
        cipherMatrix[i][j] = cipherMatrix[i][j] % 26

#cipher text from number to text 
ciphertext=""
for i in range(3): 
    i=cipherMatrix[i]
    i=chr(i[0]+65)
    ciphertext = ciphertext+i

#invers function to decreypt 
inv = np.linalg.inv(keyMatrix)
for i in range(3): 
    for j in range(1): 
        decipherMatrix[i][j] = 0
        for x in range(3): 
            decipherMatrix[i][j] += (inv[i][x] * 
                                       cipherMatrix[x][j]) 
        decipherMatrix[i][j] = decipherMatrix[i][j] % 26




print("plaintext : "+plainText)
print("key : "+key)
print ("cipherText : "+ciphertext)

print(" this is the key in number form : ")
print(keyMatrix)
print(" this is the plain text in number form : ")
print(messageVector)
print(" this is the cipher in number form : ")
print(cipherMatrix)

print(" this is the decipher in number form : ")
print(decipherMatrix)
#

