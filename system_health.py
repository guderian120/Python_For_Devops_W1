import os, psutil, subprocess, time, requests


def get_cpu():
    cpu_usage = psutil.cpu_percent(interval=1)
    return cpu_usage

def get_memory_usage():
    mem_info = psutil.virtual_memory().percent
    return mem_info

def get_disk_usage():
    disk_usage = psutil.disk_usage("/")
    return disk_usage

def send_to_api():
    url = "http://127.0.0.1:8000/api/metrics/"
    cpu_ = get_cpu()
    memory_ = get_memory_usage()
    disk_ = get_disk_usage()
    data = {
            "CPU": cpu_,
            "MEMORY":memory_,
            "DISK": disk_,

            }
    response = requests.post(url, data=data)
    print(response)
send_to_api()

