#Task:
# 22. print all numbers which are divisible by 2 and 7 in the range of 1 to 200

for nums in range(1,201):
    if nums % 2 == 0 and nums % 7 == 0:
        print('The numbers are:-', nums)
    else:
        pass
