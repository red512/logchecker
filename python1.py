import re
import os
import sys

from datetime import datetime

class bcolors:
    OKGREEN = '\033[92m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

#current date
now = datetime.now()
#formating the date
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

#Open and read the file and do except if file not exsit
try:
    f = open("run_log.txt")
    logFile = f.read()
    f.close()
except IOError:
    print(bcolors.FAIL + "NO RUN_LOG FILE" + bcolors.ENDC)
    sys.exit(1)

#check the modified date
mtime = os.path.getmtime("run_log.txt")
last_modified_date = datetime.fromtimestamp(mtime)

#Split the RUN_TIME value and write it to logfile
try:
    parArr = re.split('(\d+)', logFile)
    RUNTIME = parArr[1]
    f1 = open("log_file.txt", "w")
    f1.write(dt_string + " " + RUNTIME)
    f1.close
except IndexError:
    print("RUN_TIME ERROR")
    sys.exit(1)

lastModified = last_modified_date.date()
currentDate = datetime.today().date()
diff = now - last_modified_date
# diff = lastModified.strftime("%d/%m/%Y %H:%M:%S") - currentDate.strftime("%d/%m/%Y %H:%M:%S")

#for the worst case scenario
diffMinutes = diff.total_seconds()/60


#Compare the dates
if lastModified == currentDate or diffMinutes <= 5:
    if 'RUN_STATUS' not in logFile:
        print(bcolors.FAIL + "NO RUN_STATUS" + bcolors.ENDC)
    if 'RUN_TIME' not in logFile:
        print(bcolors.FAIL + "NO RUN_TIME" + bcolors.ENDC)
    if 'RUN_STATUS=OK' not in logFile:
        print(bcolors.FAIL + "RUN_STATUS FAILED" + bcolors.ENDC)
    elif 'RUN_STATUS=OK' in logFile:
        print(bcolors.OKGREEN + "run was completed successfully - RUN_STATUS OK" + bcolors.ENDC)
else:
    print(bcolors.FAIL + "RUN_LOG IS NOT UPDATED" + bcolors.ENDC)
