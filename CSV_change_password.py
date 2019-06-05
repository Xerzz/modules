import modules.CSV_read_headers as My_CSV
import modules.hashing_passwords as h
import modules.CSV_config as Cfg
import modules.CSV_login as CSV_login
import modules.password_validation as pv
from getpass import getpass

column = My_CSV.read_csv_headers(Cfg.filename, Cfg.delimiter)
users = column['user']
passwords = column['password']

user_info = CSV_login.get_user_info()  # logging in
user_id = user_info[0]
old_password = passwords[user_id]

print()
print('You are about to change Your password')
print('Please, confirm your current password again')

user_authorised = False
for attempt in range(Cfg.login_max_attempts):
    old_password = getpass()
    if h.validate_hashed_password(old_password, passwords[user_info[0]]):
        user_authorised = True
        break
    else:
        print('Password is incorrect!')

if not user_authorised:
    raise NameError('Wrong password!')

new_password = pv.validate_password()
if new_password == old_password:
    raise NameError("Passwords shouldn't be the same!")

print('Success! Password changed')
new_hashed_password = h.hash_password(new_password)
del new_password
passwords[user_id] = new_hashed_password
# TODO: write this dict to csv file keeping order
