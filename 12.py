# Task:
# Reverse words in a long string using function

string = input('Type in a sentence, to see how it looks in the reversed manner: ')

def reverse_string(s=string):
    if len(s) < 10:
        print('Not Enough long sentence')
    else:
        print('The sentence looks this way in reverse manner')
        print(s[::-1])


reverse_string()