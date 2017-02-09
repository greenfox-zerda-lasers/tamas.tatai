#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3

string_1 = 'Space jam'
string_2 = 'cap james'


def anagram(string_1, string_2):
    string_1_row = sorted(string_1.lower().replace(" ", ""))
    string_2_row = sorted(string_2.lower().replace(" ", ""))
    if string_1_row == string_2_row:
        return True
    else:
        return False

print (anagram(string_1, string_2))

##################################

from collections import Counter

string = 'space jam'

def count_letters(string):
    new_string = string.lower().replace(" ","")
    cnt = Counter(list(new_string))
    return cnt

print(count_letters(string))
