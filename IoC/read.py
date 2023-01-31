# Python 3.10.4
import os, datetime, hashlib

def GetFileHash(file):
    with open(file, "rb") as f:
        hash_data = f.read()

    md5 = hashlib.md5(hash_data).hexdigest()
    sha1 = hashlib.sha1(hash_data).hexdigest()

    return md5, sha1

def GetFileInfo(all_files):
    # st_mode, st_ino, st_dev, st_nlink, st_uid, st_gid, st_size, st_atime, st_mtime, st_ctime
    print(all_files)
    f = open("result.txt", "w")
    for file in all_files:
        stat_info = os.stat(file)

        strings = file + "\t"
        strings += str(datetime.datetime.fromtimestamp(stat_info.st_ctime)) + "\t"
        strings += str(datetime.datetime.fromtimestamp(stat_info.st_mtime)) + "\t"
        strings += str(datetime.datetime.fromtimestamp(stat_info.st_atime)) + "\t"
        get_md5, get_sha1 = GetFileHash(file)
        strings += str(get_md5) + "\t"
        strings += str(get_sha1) + "\t"
        strings += str(stat_info.st_size) + "\t"
        strings += str(stat_info.st_uid) + "\t"
        strings += "\n"
        
        print(strings)
        
        f.writelines(strings)
    f.close()

if __name__ == "__main__":

    all_files = []
    with open("path.txt","r") as f:
        temp = f.read().splitlines()

    for file in temp:
        all_files.append(file.replace('\\', '/'))

    GetFileInfo(all_files)