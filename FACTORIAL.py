def factorial(numbers):
    if numbers==1:
        return 1
    else:
        return numbers*factorial(numbers-1)
res=factorial(6)
print(res)