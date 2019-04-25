from getpass import getpass
import modules.hashing_passwords as h
import modules.CSV_read_headers as My_CSV
import CSV_config as Cfg


def has_numbers(input_string):
    return any(char.isdigit() for char in input_string)


def has_upper(input_string):
    return any(char.isupper() for char in input_string)


column = My_CSV.read_csv(Cfg.filename, Cfg.delimiter)
ids = column['id']
users = column['user']

username_free = False
while not username_free:
    username = input('Enter username: ')

    if username in users:
        print('This username is already taken. Please choose another name.\n')
    else:
        if len(username) < Cfg.min_username_len:
            print('Username should be at least', Cfg.min_username_len, 'characters long')
        username_free = True

account_created = False
while not account_created:
    print()
    print('Password should have at least 6 characters, one uppercase letter and one digit')
    password_v1 = getpass('Enter password: ')

    if len(password_v1) < Cfg.min_password_len:
        print('Password should be at least', Cfg.min_password_len, 'characters long')
        continue
    elif not has_upper(password_v1):
        print('Password should have at least one uppercase letter')
        continue
    elif not has_numbers(password_v1):
        print('Password should have at least one digit')
        continue
    else:
        password_v2 = getpass('Confirm password: ')
        if password_v1 != password_v2:
            print('Passwords do not match!')
            continue
        else:
            account_created = True

hashed_password = h.hash_password(password_v1)
del password_v1
del password_v2

user_id = int(ids[-1]) + 1

with open(Cfg.filename, 'a') as f:
    f.write(str(user_id) + Cfg.delimiter + username + Cfg.delimiter + hashed_password + '\n')


# IN PROGRESS

# column['user'].append(username)
# column['password'].append(hashed_password)
#
# import csv
#
# with open(filename, 'w') as f:
    # writer = csv.writer(f, delimiter=delimiter)
    # writer = csv.DictWriter(f, ['user', 'password'], delimiter=delimiter)
    # writer.writeheader()
    # writer.writerows(column['user'])

print()
print('Success! Account created')
