import os
import subprocess
'''
IP-fist-Last
--------------
1. 파일 입력 받기(로그파일-시간이 정렬된) - 마우스 드래그앤 드롭으로 하기
2. 찾고자 하는 IP리스트(개행구분) 파일 입력 받기 - 마우스 드래그앤 드롭으로 하기
3. head -1, tail -1 값 가져오기
4. IP, head-1, tail -1 탭으로 구분 짓고 파일 쓰기 - Result-FL.txt 떨구기
'''

cmd_date = '%SYSTEMROOT%\System32\WindowsPowerShell\\v1.0\powershell.exe Get-Content access-all.log | select-string -Pattern '
cmd_date = 'powershell.exe Get-Content access-all.log '
file_name = ''
find_str = 'findstr '
first_time = 'select -first 1'
last_time = 'select -last 2'
ip_list = []

def Input_IP_File():
    # 찾고자 하는 IP 리스트로 저장하기
    with open("Apache-log/ip_list.txt") as f:
        ip_list = [line.rstrip() for line in f]

    with open('first_cmd.txt', 'w') as f:
        for line in ip_list:
            first_str = cmd_date + '| ' + find_str + '\'' + line + '\'' + ' | ' + first_time + ' >> ' + 'first_time.txt'
            f.write(first_str+'\n')

    with open('last_cmd.txt', 'w') as f:
        for line in ip_list:
            last_str = cmd_date + '| ' + find_str + '\'' + line + '\'' + ' | ' + last_time + ' >> ' + 'last_time.txt'
            f.write(last_str+'\n')

if __name__ == '__main__':
    Input_IP_File()