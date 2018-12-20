import math
letters = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
letters = letters.split(' ')
def index(l):
    global letters
    return letters.index(l)

def xor(a,b):
    a_asc = index(a)+65
    b_asc = index(b)+65
    res = hex(a_asc ^ b_asc).split('0x',1)[1]
    res = '0' + res if len(res)==1 else res
    return res

#==============================================================

key = input()
plain = input()
one_time = "YES" if (len(key)==len(plain)) else "NO"
ratio = math.ceil(len(plain)/len(key))
key = (key * ratio )[0:len(plain)]
vig = ''
vernam = ''
for n in range(len(plain)):
    vig_i = ( index(plain[n]) + index(key[n]) ) % 26
    vig = vig + letters[vig_i]
    vernam+=xor(key[n],plain[n])
print ("Vigenere: "+vig)
print ("Vernam: "+vernam.upper())
print ("One-Time Pad: "+one_time)