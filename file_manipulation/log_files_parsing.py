# This is a script to iterate through log files and extract errors

error_output = [] # A list to keep track of all errors

with open("/var/log/syslog", "r") as log_file: #opening the desired log file to parse
    for line in log_file: # reading through every line in the log file
        if "ERROR" in line: # identifying lines with error messages and append them to the output list
            error_output.append(line)

with open("files/error_output.txt", "w") as output_file: # opening our file to write our errors
    output_file.writelines("\n".join(error_output)) # writing detected errors to file

print(f"{len(error_output)} - error detected and recorded") # printing to screen the number of erros


