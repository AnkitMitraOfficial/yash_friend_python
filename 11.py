# Task:
# to check palindrome.use 2 functions

# Some examples are 8, 121, 212, 12321, -454.


number = input('Enter a number to see wether it is paidrome or not: ')

# A NOTE YOU DON'T ACTUALLY NEED TWO FUNCTIONS TO FIND A PALIDROME NUMBER IT CAN BE DONE IN ONE FUNCTION
def find_palidrome(n=number):
    if n == n[::-1]:
        print('The Number you entered is palidrome')
    else:
        print('The Number you entered is not a palidrome')

find_palidrome()
