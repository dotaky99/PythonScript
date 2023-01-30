import os, datetime, hashlib, sys

# Read the path.txt
all_files = []
with open("path.txt","r") as f:
    temp = f.read().splitlines()

for file in temp:
    all_files.append(file.replace('\\', '/'))

print(all_files)

for file in all_files:
    print(os.path.getctime(file))
    create_time = os.path.getctime(file)
    modify_time = os.path.getmtime(file)
    access_time = os.path.getatime(file)
    size = os.path.getsize(file)

    with open(file, "rb") as f:
        hash_data = f.read()
    
    md5 = hashlib.md5(hash_data).hexdigest()
    sha1 = hashlib.sha1(hash_data).hexdigest()
    owner = os.stat(file).st_uid
    print(file)
    print(create_time, modify_time, access_time, size, owner)
    print(md5, sha1)
    print(owner)
    print()
    print(os.stat(file))

    strings = str(file)
    strings += str(create_time)
    strings += str(modify_time)
    strings += str(access_time)
    strings += str(size)
    
    break

def GetFileInfo(file):
    # os.stat_result(st_mode=33206, st_ino=562949953932938, st_dev=305986030, st_nlink=1, st_uid=0, st_gid=0, st_size=1221, st_atime=1675084201, st_mtime=1675084200, st_ctime=1675066108)
    stat_information = os.stat(file)
    return stat_information

def GetFileHash(file):
    with open(file, "rb") as f:
        hash_data = f.read()
    
    md5 = hashlib.md5(hash_data).hexdigest()
    sha1 = hashlib.sha1(hash_data).hexdigest()

if __name__ == "__main__":
    GetFileInfo()
    GetFileHash()
