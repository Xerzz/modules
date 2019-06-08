# Few simple python modules

Hey, I wanna share with You my python modules,

I have for now:
* open_file
* logger
* CSV support
* hashing passwords
* tictoc
* downloading files

I hope You enjoy it.

## Usage:
* logger:  

`import logger`  
then create logger:  
`log = logger.Logger()`  
and use it everywhere you want!
```
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
Example: python_file.py -> 'python_file.py'.log in 'logs' folder

* CSV modules:

I'am using users.csv as database. There is one account created for You:  
Login - Admin  
Password - Admin1

Just use login file to login, new_user file to create new user.  
My delimiter is ' ; ' because of Microsoft.

* tictoc:  

`import tictoc as t`
just use
`t.tic()`
and
`t.toc()`
functions

You can use toc multiple times

toc() output:
`Elapsed time: 2.562 seconds.`

Edit:
I created Class that works better for me.
```python
import tictoc
t = tictoc.TicToc()
t.tic()
t.toc()
```
Take a look for documentation in file.

* download_file

Usage:
```python
import modules.downloading_file as d

url1 = 'http://example.com/text.txt'
url2 = 'http://example.com/zipfile.zip'

d.download(url1)
d.download_zip(url2)
```