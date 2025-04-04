- working with files(reading, writing and parsing logs) -

                a sample python code for reading files {

                        with open("/var/log/syslog", "r") as file: # This line opens the file in read mode, with ensures the file is properly closed after use
                            for line in file:
                                print(line.strip())
                    }

                    a sample python code for writing to a file {

                        with open("output.log", "w") as file: # "W" mode overwrites the file if it exists, "a" mode appends new data without deleting old ones
                            file.write("Log entry: System check complete. \n")
                    }



                A sample code to parse log files and extract errors {


                    errors_logs = []
                    with open("/var/log/syslog", "r") as file:
                        for line in file:
                            if "ERROR" in line:
                                errors_logs.append(line.strip())

                    #save extracted error logs

                    with open("error_logs.txt", "w") as output:
                        output.writelines("\n".join(error_logs))
                }

                - Difference between write and write lines -
                    -Write is used to write a single  string to a file eg. file.write("my name is kofi")
                    
                    -writelines is used to write multiple lines(a list of strings to a file) eg [
                                lines = [" first line \n", "second line \n"]
                                file.writelines(lines)
                    ]



- interacting with OS processes (subprocess, os modules) -
    - Python provides the os and subprocess modules to interact with system process

    a sample python code to list running process {

        #linux / macos
        import os
        os.system("ps aux | head -10") # list first 10 processes

        #windows
        import os
        os.system("tasklist")
    }
     
    - running shell commands is an integral part of python for devops
        and the subprocess modeule is the most effective tool more powerful than
        the os.system()

        - a sample code to check disk usage {

            import subprocess 
            #capture_output captures the command output, text=True ensures output is returned as string
            result = subprocess.run(["df", "-h"], capture_output=True, text=True)
            print(result.stdout)
        }

        - a sample code to check CPU and Memory Usage {
            # to monitor system resources. we can use the psutil library
            #pip install psutil 

            import psutil

            cpu_usage = psutil.cpu_percent(interval=1) # CPU usage over 1 second
            mem_info = psutil.virtual_memory() # Memory details

            print(f"CPU Usage: {cpu_usage}%")
            print(f"Memory Usage: {mem_info.percent}%")
        }

ASSIGNMENT BREAK:
        - Write a script to log CPU & Memory usage every 5 seconds for 1 minute
        - save the logs to a file (sysem_monitor dot log)

        Solution {
            # first I will use the psutle library to get CPU and Memory usage 

            import psutil, time
            for r in range(12): # the script will sleep every 5 seconds so 12 times will be 1 minute (60 seconds)
                print("monitoring now")
                cpu_usage = psutil.cpu_percent(interval=1)
                mem_info = psutil.virtual_memory().percent

                with open("files/system_monitor.log", "a") as file:
                    file.writelines("\n" + cpu_usage + "\n" + mem_info)
                time.sleep(5)
        }   


In the Final Project for week one, We created a live system health monitor that sent metrics to an api consumed
by an django app and displayed on a dashboard

