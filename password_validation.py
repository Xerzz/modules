from getpass import getpass


def _has_numbers(input_string):
    return any(char.isdigit() for char in input_string)


def _has_upper(input_string):
    return any(char.isupper() for char in input_string)


def validate_password(min_password_len=6, max_password_len=20, should_have_digit=True, should_have_upper=True):
    account_created = False
    print('Password should have between', min_password_len, 'and', max_password_len, 'characters')
    if should_have_digit: print('At least one digit')
    if should_have_upper: print('And at least one upper')

    while not account_created:
        # print()
        password_v1 = getpass('Enter password: ')

        if len(password_v1) < min_password_len:
            print('Password should be at least', min_password_len, 'characters long')
            continue
        elif len(password_v1) > max_password_len:
            print('Password should have maximum 20 characters')
            continue
        if should_have_digit and not _has_numbers(password_v1):
            print('Password should have at least one digit')
            continue
        if should_have_upper and not _has_upper(password_v1):
            print('Password should have at least one uppercase letter')
            continue
        password_v2 = getpass('Confirm password: ')
        if password_v1 != password_v2:
            print('Passwords do not match!')
            continue
        else:
            account_created = True
            del password_v2
            return password_v1
