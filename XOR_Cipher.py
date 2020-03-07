Ptext = "hellow world"
#reverse text 
key = ''.join(reversed(Ptext))

print("plintext : "+Ptext)
print("key : "+key)

# using join() + ord() + format() 
# Converting String to binary 
inBinaryP = ''.join(format(ord(i), 'b') for i in Ptext) 
inBinaryK = ''.join(format(ord(i), 'b') for i in key) 

print("binary plintext : "+inBinaryP)
print("binary key : "+inBinaryK)
#excluseve or operation for encrypt 
cipher = (int(inBinaryK) ^ int(inBinaryP))
print("ciphertext : "+str(cipher))

#excluseve or operation for decrypt 
cipherxor = ((int(inBinaryK) ^ int(cipher)))
print("after xor with key : "+str(cipherxor))


