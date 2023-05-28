mynum= [1,2,3,4,5]
mypow= [2,3,4,5,6]

T = []

for n,p in zip(mynum, mypow):
    val = n**p
    T.append(val)

print(T)