# vestigium
def printDiagonalSums(mat, n): 
    d_sum = 0
    for i in range(0, n):  
        d_sum += mat[i][i]
    return d_sum

from collections import Counter
tc = int(input())
tmp_tc = tc
mat = []
m = 1
while(tmp_tc > 0):
    n = int(input())    # size
    tmp_n = n
    while tmp_n > 0:
        inp = input().split(" ")
        mat.append([int(i) for i in inp])
        tmp_n -= 1
    r_c = 0
    for each in mat:
        if len(set(each)) != len(each):
            r_c += 1
    c_c = 0
    for i in range(n):
        tmp = [c[i] for c in mat]
        print(tmp)
        if len(set(tmp)) != len(tmp):
            c_c += 1
    d_sum = printDiagonalSums(mat, n)
    print("Case #" + str(m) + ": " + str(d_sum) + " " + str(r_c) + " " + str(c_c))
    m += 1
    tmp_tc -= 1
