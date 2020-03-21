#ahmad saed mohammad maqboul 11613411
#adel jibrel shtayyeh 11642719


import operator
import random
import time
start = time.time()

#open and read from cipher text file 
with open('cipher.txt', 'r') as file:
    string1 = file.read().replace('\n', '')
    string1 = string1.upper()
#open and read from plain text file 
with open('plain.txt', 'r') as file1:
    plain = file1.read().replace('\n', '')
    plain = plain.upper()
ciphertext = string1.replace(" ", "")

print(len(ciphertext))

freq = {} 

for i in ciphertext:     
    if i in freq: 
        freq[i] += 1
    else: 
        freq[i] = 1
plaintext1 = string1

#find higest freq latter in cipher text
# 1 mean compare the lefft side in dictionary
#print(max(freq.items(), key=operator.itemgetter(1))[0])
#the latter with maximum freq

e = max(freq.items(), key=operator.itemgetter(1))[0]
i = 0

plaintext1 = plaintext1.replace("E", "1") # we replace there form every e in ciphe to 1 to delete repation
plaintext1 = plaintext1.replace(e, "E")

#use plind text one in first edite to know sub string like the than ,...
#the new cipher text after we change useing frequance
ciphertext = plaintext1.replace(" ", "")
the = "***"
#small to compare 
small = ""

#get e and 3 letter before it and get higest freq to know "the" 
for i in range(len(ciphertext)):
    if(ciphertext[i] == 'E'):
        small = ciphertext[i-2] + ciphertext[i-1] + ciphertext[i]
        if (ciphertext.count(the) < ciphertext.count(small)):
            the = small

#change. all T , H in plain text to correct one
# new plain text 
# to remover frequance with the latter we know
plaintext1 = plaintext1.replace('T', '2')  #  --- T,H  in cipher text
plaintext1 = plaintext1.replace('H', '3')
# to change all T , H in text 
plaintext1 = plaintext1.replace(the[0], 'T') # --- T,H  in plain text
plaintext1 = plaintext1.replace(the[1], 'H')

#E 1
#T 2
#H 3

b = "*" #4
o = "*" #5
a = "*" #6
l = "*" #7
f = "*" #8
n = "*" #9
d = "*" #! 
r = "*" #@
w = "*" ##
ii= "*" #$
s = "*" #%
u = "*" #^


for i in range(len(plaintext1)-4):
    # be condition
    if(plaintext1[i] == 'E' and plaintext1[i-2] == ' ' and plaintext1[i + 1] == ' 'and plaintext1[i-1] != 'H'):
        b = plaintext1[i-1] 
        plaintext1 = plaintext1.replace('B', '4') # replace 'B' in cipher text to 4 to skip confusion

    # to condition
    if(plaintext1[i] == 'T' and plaintext1[i + 2] == ' ' and plaintext1[i-1] == ' '):
        o = plaintext1[i + 1]
        plaintext1 = plaintext1.replace('O', '5')

    # that condition
    if(plaintext1[i] == 'T' and plaintext1[i + 1] == 'H' and plaintext1[i + 3] == 'T'and plaintext1[i + 4] == ' '):
        a = plaintext1[i + 2]
        plaintext1 = plaintext1.replace('A', '6')
    # all condition
    elif(plaintext1[i + 1] == plaintext1[i + 2] and plaintext1[i-1] == ' ' and plaintext1[i + 3] == ' '):
        a = plaintext1[i]
        l= plaintext1[i + 1]
        plaintext1 = plaintext1.replace('A', '6')
        plaintext1 = plaintext1.replace('L', '7')

    # with condition
    if(plaintext1[i] == 'T' and plaintext1[i + 1] == 'H' and plaintext1[i + 2] == ' ' and plaintext1[i - 3] == ' '): 
        w = plaintext1[i-2] 
        ii=plaintext1[i - 1]
        plaintext1 = plaintext1.replace('W', '#')
        plaintext1 = plaintext1.replace('I', '$')

plaintext1 = plaintext1.replace(b, 'B')
plaintext1 = plaintext1.replace(o, 'O')
plaintext1 = plaintext1.replace(a, 'A')
plaintext1 = plaintext1.replace(l, 'L')
plaintext1 = plaintext1.replace(w, 'W')    
plaintext1 = plaintext1.replace(ii, 'I') 

for i in range(len(plaintext1)-4):
    # and condition 
    if(plaintext1[i] == 'A' and plaintext1[i + 3] == ' ' and plaintext1[i-1] == ' ' and plaintext1[i + 1] != plaintext1[i + 2]):   
        n =  plaintext1[i + 1] 
        d =  plaintext1[i + 2]

        plaintext1 = plaintext1.replace('N', '9')
        plaintext1 = plaintext1.replace('D', '!')   
    

    # of condition
    if(plaintext1[i] == 'O' and plaintext1[i + 2] == ' ' and plaintext1[i-1] == ' '):
        f = plaintext1[i + 1]
        plaintext1 = plaintext1.replace('F', '8')

    # these condition
    if(plaintext1[i] == 'T' and plaintext1[i + 1] == 'H' and plaintext1[i + 2] == 'E' and plaintext1[i + 4] == 'E' and plaintext1[i + 5]==' ' and plaintext1[i - 1]==' '):
        s = plaintext1[i + 3]
        plaintext1 = plaintext1.replace('S', '%')

    # this condition
    elif(plaintext1[i] == 'T' and plaintext1[i + 1] == 'H' and plaintext1[i + 2] == 'I' and plaintext1[i + 4] == ' ' and plaintext1[i - 1] == ' '):
        s = plaintext1[i + 3]
        plaintext1 = plaintext1.replace('S', '%')
        
    #is condition
    elif(plaintext1[i] == 'I' and plaintext1[i + 2] == ' ' and plaintext1[i-1] == ' '):
        s = plaintext1[i + 1]
        plaintext1 = plaintext1.replace('S', '%')


    #s condition use tions 
    elif(plaintext1[i] == 'T' and plaintext1[i + 1] == 'I' and plaintext1[i+2] == 'O' and plaintext1[i+3] != ' '):
        s = plaintext1[i + 4]
        plaintext1 = plaintext1.replace('S', '%')



plaintext1 = plaintext1.replace(n, 'N')
plaintext1 = plaintext1.replace(d, 'D')
plaintext1 = plaintext1.replace(f, 'F')     
plaintext1 = plaintext1.replace(s, 'S')    


for i in range(len(plaintext1)-3):
    # but condition 
    if(plaintext1[i] == 'B' and plaintext1[i + 2] == 'T' and plaintext1[i-1] == ' ' and plaintext1[i + 3] == ' '):   
        u = plaintext1[i + 1] 
        plaintext1 = plaintext1.replace('U', '^')

    # there condition
    if(plaintext1[i] == 'T' and plaintext1[i + 1] == 'H' and plaintext1[i + 2] == 'E' and plaintext1[i + 4] == 'E' and plaintext1[i + 3]!='S'):
        r = plaintext1[i + 3]
        plaintext1 = plaintext1.replace('R', '@')
    # for condition
    if(plaintext1[i] == 'F' and plaintext1[i + 1] == 'O' and plaintext1[i + 3] == ' ' and plaintext1[i -1] == ' '):
        r = plaintext1[i + 2] 
        plaintext1 = plaintext1.replace('R', '@')




plaintext1 = plaintext1.replace(u, 'U') 
plaintext1 = plaintext1.replace(r, 'R') 


myItem1 = "ETHBOALFNDRWISU" #The characters we found
myItem2 = "CGJKMPQVXYZ" #The characters are guessed
myItem3 = "123456789!@#$%^&CGJKMPQVXYZ" #Symbols that are replaced by letters
plaintext2 = plaintext1
 


for i in range(len(myItem3)):
    if myItem3[i] in plaintext2: 
        plaintext2 = plaintext2.replace(myItem3[i], myItem2[random.randrange(0, len(myItem2), 1)])# randrange(start, stop, step)
        
print(plaintext2+"\n")

        

end = time.time()
print(end - start)


'''
------ big o 
11120-----.09 + .08 + .09   = .86 
5560-----.030 + .029 + .034 = .031
2219-----.009 + .011 + .009 = .01
1605-----.008 + .007 + .008 = .0075
939------.005 + .005 + .006 = .0055
------

'''



'''
RESOURSES

ALGORTHEM FOR COUNT LATTER :
https://www.geeksforgeeks.org/python-frequency-of-each-character-in-string/

INFORMATION ABOUT MONOCIPGER :
https://www.ti89.com/cryptotut/mono_crack.htm

CONVERT TO CABITAL :
https://convertcase.net/

ENCR TOOL :  
https://www.cryptool.org/en/cto-ciphers/monoalpha

'''
