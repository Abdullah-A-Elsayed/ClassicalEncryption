def coordinates (my_str, my_chr):
    index = my_str.index(my_chr)
    row = int(index / 5 )
    colum = index % 5
    return (row,colum)

def letter (my_str, x, y):
    return my_str[x*5+y]

letters_str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
key = input()
key+=letters_str
key = key.replace('J','I')
#remove dups
new_key=''
for l in key:
    if l in new_key:
        pass
    else:
        new_key+=l
key = new_key
## wrong -> replace it with I before removing duplicates
#remove j
# j_index=key.index("J")
# key = key[0:j_index]+key[j_index+1:]
############# key str is ready ###############
plain = input()
# j replacing
plain = plain.replace("J","I")
new_plain = ''
i=0
while i < len(plain):
    sub = ''
    sub+= plain[i]
    # 
    second_chr = ''
    if (i==(len(plain)-1)):
        second_chr = 'X'
    else:
        second_chr = plain[i+1]
    # 

    if(sub!=second_chr):
        sub+=second_chr
        i+=2
    elif (sub == "X"):
        sub += "Q"
        i+=1
    else:
        sub += "X"
        i+=1
    #
    new_plain += sub
plain = new_plain
# print (plain+" ## len= "+str(len(plain)))
# print(key+" ## len= "+str(len(key)))
############# plain str is ready ###############
cipher = ''
i=0
while i<len(plain):
    a = plain[i]
    b = plain[i+1]
    a_x , a_y = coordinates(key,a)
    b_x , b_y = coordinates(key,b)
    # co-ordinates ready
    if (a_x == b_x):
        c_x, d_x = a_x , b_x
        c_y = (a_y+1)%5
        d_y = (b_y+1)%5
    elif (a_y == b_y):
        c_y, d_y = a_y , b_y
        c_x = (a_x+1)%5
        d_x = (b_x+1)%5
    else:
        c_x, d_x = a_x , b_x
        c_y = b_y
        d_y = a_y
    cipher+= letter (key,c_x,c_y)
    cipher+= letter (key,d_x,d_y)
    # 
    i+=2
print (cipher)