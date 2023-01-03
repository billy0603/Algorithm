'''
使用array去取代數值
'''
ans=[0]*100

def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        ans[0]=0
        ans[1]=1
        for i in range(2,n+1):
            ans[i]=ans[i-1]+ans[i-2]
    return ans[n],ans

print(fib(5))