import math

def isperfectsquare(x):
    s=int(math.sqrt(x))
    return s*s==x
def isfib(n):
    return isperfectsquare(5*n*n+4)or isperfectsquare(5*n*n-4)
for i in range (2,11):
    if(isfib(i)==True):
        print(i,'is fib')
    else:
        print(i,'is not fib')


#another way
print("\n same:")
def fibonacci(n):
    if n<0:
        return 1
    elif n==0 or n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
res=fibonacci(6)
print(res)


