'''
F=
    0  n=0
    1  n=1
    Fn-1+Fn-2  n=2,3,4,5,6...(n為正整數)
'''

def fib(n):
    if n==0:  #條件n=0
        return 0
    elif n==1 or n==2:  #條件n=1、2
        return 1
    else:
        return (fib(n-1)+fib(n-2))
n=int(input('請輸入要計算第幾個費氏數列:'))
for i in range(n+1):
    print('fib(%d)=%d' %(i,fib(i)))