# Task:
# calculate simple interest. accept P,T,R from user

rate = int(input('Enter rate of interest: '))
time = int(input('Enter year/years: '))

if time == 1:
    principal = int(input(f'Enter pricipal for {time} year at a rate of {rate}%: '))
else:
    principal = int(input(f'Enter pricipal for {time} years at a rate of {rate}%: '))

def calculate(t=time,r=rate,p=principal):
    result = t * r * p
    final_result = result/100

    if t == 1:# If the year is one
        print(f'The simple interest for {t} year at a rate of {r}% on amount of {p} is ' + str(final_result))

    else:# if year is not 1 then:
        print(f'The simple interest for {t} years at a rate of {r}% on amount of {p} is ' + str(final_result))

calculate()