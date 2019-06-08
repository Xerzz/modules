# Few simple python modules

Hey, I wanna share with You my python modules,

I have for now:
* open_file
* logger
* CSV database with users and passwords
* hashing passwords
* password validation
* tictoc
* downloading files

I hope You enjoy it!

## Usage:
* logger:  

```python
import logger
log = logger.Logger()

log.info('some info')
log.debug('some info')
log.warning('some info')
log.error('some info')
log.critical('some info')
```

Sample log file line:

`2019-03-27 20:52:27,471 - INFO - some info`

log file has default name same as file name, but in quotes and with .log.
Also it is in new folder called 'logs'  
Example: python_file.py -> 'python_file.py'.log in new 'logs' folder

* CSV modules:

I'am using CSV_users.csv as database. There is one account created for You:  
Login - Admin  
Password - Admin1

Just use CSV_login file to login, CSV_new_user to create new user.  
Changing password is still in progress  

My delimiter is ' ; ' because of Microsoft.

* tictoc:

```python
import tictoc as t

t.tic()
t.toc()
# more code
t.toc()

t.tic()
t.toc()
```
You can use toc multiple times, it will count since last `tic()` function

toc() output:
`Elapsed time: 2.562 seconds.`

Edit:
I created class with this functionality, You can have now multiple timers.
```python
import tictoc
t = tictoc.TicToc()
t.tic()
t.toc()
```

Take a look for documentation in file ;)

* hashing passwords

Two functions:
```python
import hashing_passwords as h
hashed = h.hash_password('Pa$$w0rd')
# store it somewhere!

h.validate_hashed_password('Pa$$w0rd', hashed)
# returns True or False
```
It's simple and secure 

* password validation

```python
import password_validation as p
password = p.validate_password()
```
in `password` variable You have user password from keyboard.   
It was taken by getpass so it wasn't visible for others (just like in linux)  

I recommend to use it with hashing_password, 
do not store passwords in plain text!

* download_file

```python
import downloading_file as d

url1 = 'http://example.com/text.txt'
url2 = 'http://example.com/zipfile.zip'

d.download(url1)
d.download_zip(url2)
```

You can simply download any file from web giving url only.  
Zip default will be unpacked to folder (with same name as package) and deleted, 
of course You can change it
