# Task
# 30. Input a year and check for leapyear. 

year =  int(input('Input a year to check whether it is leap year or not: '))


def check_leap_year(y=year):
    if y % 4 == 0:
        print(f'The year {y} is a leap year')
    else:
        print(f'The year {y} is not a leap year')


check_leap_year()
