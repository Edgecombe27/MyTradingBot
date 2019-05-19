import time
import datetime
import os

now = datetime.datetime.now()
timestamp = str(now.hour)+'-'+str(now.minute)+'-'+str(now.second)
log_file = open('log-'+timestamp, 'w')

def log(obj) :
    global log_file
    log_file.write(str(obj))
    log_file.write('\n')
    log_file.flush()
    os.fsync(log_file.fileno())

def minutes(value):
    return 60 * value

def hours(value):
    return 60 * 60 * value