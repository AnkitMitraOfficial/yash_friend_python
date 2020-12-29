# Task:
# print all prime numbers between 23 to 79


def print_prime_numbers():
    for numbers in range(23,80): # If we write 79 it will be excluded
        if numbers % 2 ==0:
            print(f'{numbers} is a  Prime Number')
        else:
            pass # We do not want to print, if the number is not a prime number

print_prime_numbers()
