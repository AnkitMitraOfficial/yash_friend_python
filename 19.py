# Task:
# 19. prints all the numbers from 12 to 31 except 17 and 19.using 'continue statement

def nums():
    for numbers in range(12,32): 
        if numbers == 17:
            continue
        if numbers == 19:
            continue
        print(numbers)

nums()

            