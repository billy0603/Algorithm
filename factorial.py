def factorial(i):
    if i==0:
        return 1
    else:
        ans=i * factorial(i-1)
    return ans

print(factorial(5))