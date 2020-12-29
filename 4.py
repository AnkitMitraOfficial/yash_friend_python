# Task:
# To check a given number is prime

prime_number = int(input('Write down a number to find whether it is prime or not!: ')) 

def find_prime(n=prime_number):
    if n % 2 == 0:
        print(f'Number {n} is a prime number :)')
    else:
        print(f'Number {n} is not a prime number :(')


find_prime()