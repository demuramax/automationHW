# The user enters a string. Print True if the string is a palindrome, otherwise False.
# A palindrome is a string that reads the same way from the left and from the right.
# If there are leading or trailing spaces in the line, they should not be taken into account.
# The check must be case-insensitive.
# Solve at least in TWO ways.


def palindrome_check(str_name):
    str_name = str_name.lower().replace(' ', '')
    if str_name == str_name[::-1]:
        print('The string is a palindrome')
    else:
        print('False')



a = input('Enter a string: ')
palindrome_check(a)

def palindrome_check_2(a: str):
    a = a.lower().replace(' ', '')
    a_len = len(a)
    if a[:a_len // 2] == a[a_len // 2 + 1:][::-1]:
        return 'True'
    return 'False'


print(palindrome_check_2(a))


