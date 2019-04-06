# Few simple python modules

Hey, I wanna share with You my python modules,

I have for now:
* open_file.py
* logger.py
* tictoc.py

I hope You enjoy it.

## Usage:
> logger: \n
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

log file has default name same as file name but in quotes and with .log
also it is in new folder called 'logs'
Example: python_file.py -> 'python_file.py'.log in 'logs' folder

> tictoc:
just use
`tic()`
and
`toc()`
functions

You can use toc multiple times

toc() output:
`Elapsed time: 2.562 seconds.`
