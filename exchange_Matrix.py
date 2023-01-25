import random

def exchange_Matrix():
    arr_len=int(input('設定 幾乘幾 的二維陣列:'))
    A=[[random.randint(1,10)for row in range(arr_len)]  for row in range(arr_len)]
    B=[[None]*arr_len  for row in range(arr_len)]

    #進行矩陣轉置的動作
    for i in range(arr_len):
        for j in range(arr_len):
            B[i][j]=A[j][i]
            
    print('[矩陣的內容為]')
    for i in range(arr_len):
        for j in range(arr_len):
            print('%d' %A[i][j],end='\t')
        print()
        
    print('[轉置矩陣的內容為]')
    for i in range(arr_len):
        for j in range(arr_len):
            print('%d' %B[i][j],end='\t')
        print()

exchange_Matrix()