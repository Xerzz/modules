from getpass import getpass
import modules.hashing_passwords as h
import modules.CSV_read_headers as My_CSV
import CSV_config as Cfg
import modules.password_validation as pv

column = My_CSV.read_csv_headers(Cfg.filename, Cfg.delimiter)
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

password = pv.validate_password()
hashed_password = h.hash_password(password)
del password

if len(ids) == 0:
    user_id = 0
else:
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
