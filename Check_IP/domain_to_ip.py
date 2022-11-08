import os, re

# 최종 결과 담을 변수 리스트
all_ip = []

# 명령어 조합
nslookup = 'nslookup '
location = []

# 위치(도메인) 불러오기
with open("location.txt","r") as f:
    for line in f:
        location.append(line.strip())

for domain in location:
    line = os.popen(nslookup + domain).read()
    ip_candidates = re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", line)
    print(ip_candidates)
    all_ip.append(ip_candidates)

print(all_ip)

with open("all_ip", "w") as f:
    for ip in all_ip:
        for node in ip:
            print(node)
            f.write(node.strip()+"\n")