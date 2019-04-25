from getpass import getpass
import modules.hashing_passwords as h
import modules.CSV_read_headers as My_CSV

filename = 'CSV_users.csv'
delimiter = ';'
max_attempts = 3


column = My_CSV.read_csv(filename, delimiter)
users = column['user']
passwords = column['password']
del column

user_found = False
while not user_found:
    username = input('Enter username: ')
    for index, user in enumerate(users):
        if username == user:
            user_found = True
            break
    if not user_found:
        print('User does not exist... Try using another username\n')

user_logged = False
for attempt in range(max_attempts):
    user_password = getpass()
    if h.validate_password(user_password, passwords[index]):
        user_logged = True
        print()
        print('Success!')
        print('Logging in...')
        break
    else:
        print('Invalid password!')
        print('You have', (max_attempts - 1) - attempt, 'attempts left')

del users, passwords

exit(0 if user_logged else 1)
