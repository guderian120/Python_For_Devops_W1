# This project will create a script that monitors cpu and memory usage every 5 seconds for 1 minute
# And save it to a log file
# This project will be split into two



#PHASE ONE - LOG PARSER
log_dir = "/var/log/syslog"
error_lst = []
        
with open(log_dir, "r") as log_file: #Opening and reading the log file line by line
    for line in log_file:
        if "ERROR" in line: # extracting all lines with errors and  appending to our error list
            error_lst.append(line)

with open("files/error_output.txt", "w") as error_file: #opening our error output file
    error_file.writelines("\n".join(error_lst)) # writing errors to error output file

print(f"{len(error_lst)} - Errors Caught and Dumped to Output File")





#PHASE TWO - MONITORING SYSTEM INFORMATION
import time # this module will help us keep track of the time
import psutil # this module gives us functionality to monitor system resources
from datetime import datetime

for i in range(12): # we will have a wait time of 5 seconds, so looping 12 times will give us the one minute 12 * 5 = 60
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cpu_usage = psutil.cpu_percent(interval=1) # get the cpu usage every one second
    mem_info = psutil.virtual_memory().percent # get the memory usage as a percentage

    # writing the output to file 
    with open("files/logs/system_log.log", "a") as log_file: # using the "a" to append to existing log files
        log_file.writelines("\n" + timestamp + str(cpu_usage) + "|" + str(mem_info))


    print(f"CPU USAGE: {cpu_usage}  |  MEM_INFO: {mem_info}  > Written to log")
    time.sleep(5)

