# Task:
# Write a function to print the factorial of a number

def fact(n):
    factorial_number = 1
    for i in range(1,n+1):# Why n+1, because n will be excluded if we do not write n+1
        factorial_number = factorial_number * i

    return factorial_number

number = 5

result = fact(number)

print(result)# Outputs 120 as number = 5