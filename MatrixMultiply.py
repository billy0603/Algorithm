import random
print('請輸入矩陣A的維數(M,N): ')
M=int(input('M= '))
N=int(input('N= '))
A=[[random.randint(1,10)for row in range(N)]  for row in range(M)]
print(A)

print('請輸入矩陣B的維數(M,N): ')
N=int(input('N= '))
P=int(input('P= '))
B=[[random.randint(1,10)for row in range(P)]  for row in range(N)]
print(B)

C=[None]*M*P #宣告大小為NxP的串列C
print(C)

def MatrixMultiply(arrA, arrB,arrC,M,N,P):
    global C
    if M<=0 or N<=0 or P<=0:
        print('[錯誤:維數M,N,P必須大於0]')
        return
    for i in range(M):
        for j in range(P):
            Temp=0
            for k in range(N):
                Temp = Temp + int(arrA[i*N+k])*int(arrB[k*P+j])
            arrC[i*P+j] = Temp

MatrixMultiply(A,B,C,M,N,P)
print('[AxB的結果是]')
for i in range(M):
    for j in range(P):
        print('%d' %C[i*P+j], end='\t')
    print()
