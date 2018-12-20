import math
letters = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
letters = letters.split(' ')
def index(l):
    global letters
    return letters.index(l)

def space_between(my_str):
    temp = list(my_str)
    return ' '.join(str(v) for v in temp)

def make_mat (my_str,rows,columns):
    temp = my_str.split(' ')
    mat = []
    i=0
    while(i<len(temp)):
        row = []
        for j in range(columns):
            row.append(int(temp[i+j]))
        mat.append(row)
        i+=rows
    return mat

def mult_simple_mat (a,b):
    res = []
    for row in a:
        temp = 0
        for cell_i in range(len(row)):
            temp = (temp + b[cell_i]*row[cell_i] ) %26
        res.append(temp)
    return res



def simple_mat_to_letters(mat):
    global letters
    res = ''
    for l in mat:
        letter = letters[l]
        res = res + letter
    return res



#==============================================================

key_len_temp = input()
key_len = int(math.sqrt(int(key_len_temp)))
key_str = str(input())
key = make_mat(key_str,key_len, key_len)
plain = input()
diff = len(plain)%key_len
fill = 0 if(diff == 0) else key_len - diff
plain = plain + ('X'*fill)

#========= done taking input ==============
# print_mat(key)
i = 0
cipher = ''
while (i< len(plain)):
    # 
    sub_mat_str = plain[i:i+key_len]
    sub_mat_let = list(sub_mat_str)
    sub_mat = [index(l) for l in sub_mat_let]
    # print(sub_mat)
    mul = mult_simple_mat (key,sub_mat)
    # print_mat(mul)
    cipher = cipher + simple_mat_to_letters (mul)
    # 
    i = i + key_len
print (cipher)