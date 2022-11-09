import os, re
import tailer

## make result directory
print("[*] Make Directory for work")
dir_path = "IP_PARSE/"
if os.path.isdir(dir_path) == False:
    os.makedirs(dir_path)

## split to each IP
print("[*] Working to Log Parse about each IP")
file_path = 'Apache-log/access.log'
with open(file_path, "r") as f:
    for lines in f:
        index = lines.find(' ')
        ip = lines[:index].strip()
        with open(dir_path + ip, 'a') as f:
            f.write(lines)

## Parse First Access and Last Access
print("[*] Parse First access and Last Access")
## make result directory
ip_result_path = dir_path + 'IP_FIRST_LAST/'
ip_result_file_name = 'ip_first_last_access'
print("[*] Make Directory for Parsing IP Access Time")

if os.path.isdir(ip_result_path) == False:
    os.makedirs(ip_result_path)

folder_list = os.listdir(dir_path)
for ip in folder_list:
    if ip == "":
        break
    first_lines = tailer.head(open(dir_path + ip), 1)
    last_lines = tailer.tail(open(dir_path + ip), 1)
    first_time = re.findall(r"\d{2}/\w{3}/\d{4}:\d{2}:\d{2}:\d{2}", str(first_lines))
    last_time = re.findall(r"\d{2}/\w{3}/\d{4}:\d{2}:\d{2}:\d{2}", str(last_lines))
    result = ip, first_time[0], last_time[0]
    result = "\t".join(result)
    with open(ip_result_path + ip_result_file_name, "a") as f:
        f.write(str(result)+"\n")
