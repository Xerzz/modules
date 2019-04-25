from getpass import getpass
import modules.hashing_passwords as h
import modules.CSV_read_headers as My_CSV
import CSV_config as Cfg

column = My_CSV.read_csv(Cfg.filename, Cfg.delimiter)
ids = column['id']
users = column['user']
passwords = column['password']
del column

user_found = False
for attempt in range(Cfg.login_max_attempts):
    username = input('Enter username: ')
    if not user_found:
        for index, user in enumerate(users):
            if username == user:
                user_found = True
                break
        if not user_found:
            print('User does not exist... Try using another username.')
            print('You have', (Cfg.login_max_attempts - 1) - attempt, 'attempts left')
    if user_found:
        break


user_logged = False
for attempt in range(Cfg.login_max_attempts):
    user_password = getpass()
    if h.validate_password(user_password, passwords[index]):
        user_logged = True
        print()
        print('Success!')
        print('Logging in...')
        break
    else:
        print('Invalid password!')
        print('You have', (Cfg.login_max_attempts - 1) - attempt, 'attempts left')

del users, passwords

# exit(0 if user_logged else 1)
# exit(username)
