` This will give a deep dive on the project for this week: We will build an Automated System Health Dashboard

- The project will have Two major components
    
    - Component one (Linux): A monitoring tool that logs system health data and serves it to a web api
                     This API will provide CPU, MEMORY and DISK USAGE in json format
                     the script will run every 30 seconds
                        
                     - we will build a function that provides the health information for CPU, MEMORY and DISK USAGE first

                     



    - Component two (Web Aspect): A django dashboard which will consume the api and  display the health of our system
