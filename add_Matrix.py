import random


def add_Matrix():
    arr_len=int(input('設定 幾乘幾 的二維陣列:'))
    A=[[random.randint(1,10)for row in range(arr_len)]  for row in range(arr_len)]
    B=[[random.randint(1,10)for row in range(arr_len)]  for row in range(arr_len)]
    C=[[None]*arr_len  for row in range(arr_len)]
    for i in range(len(A)):
        for j in range(len(A)):
            C[i][j] = A[i][j] + B[i][j] #矩陣相加
    print('矩陣A =>',A)
    print('矩陣B =>',B)
    print('矩陣相加後結果:')
    print('--------------')
    for i in range(len(A)):
        for j in range(len(A)):
            print('%d' %C[i][j],end='\t')
        print()
        
add_Matrix()