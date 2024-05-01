# There's a string with email address.
# Print True if the string is a valid address, otherwise False.
# Valid address is considered:
# - '@' comes before '.'
# - the string does not start with '@' and does not end with '.'
# - symbols except '@' and '.' should be letters and decimal digits
# - containing only one '@' and only one '.'
# Specify strings for testing your code in comments.
# DO NOT use regular expressions.

email = "aaa@bbb.ccc"  # True


def email_validator(email):
    if email.find('@') == -1 or email.find('.') == -1 or email.find('@') > email.rfind('.'):
        return False
    if email.startswith('@') or email.endswith('.'):
        return False

    for el in email:
        if not el.isalnum() and el != '@' and el != '.':
            return False

    if email.count('@') != 1 or email.count('.') != 1:
        return False
    return True

print(email_validator(email))
# strings for testing your code in comments.
# "max@gmail.com"
# 'max@gmail'
# 'max@gmail@com'
# '@max.com'
# 'max.com'
# 'max@com.'
# 'max@com'
# 'max@gmail..com'
