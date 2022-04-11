#!/usr/bin/python
#This code was provided by BeagleD,AKA Dr. Dias, SY402 instructor, and posted publicly 
import csv
import datetime
import hashlib
import os
from builtins import any as search_array #Must change from '__builtin__' to 'builtins' due to a python3 update

bad = ["/usr", "/boot", "/bin", "/etc", "/dev", "/proc", "/run", "/sys", "/tmp", "/var/lib", "/var/run"]

def main():
    if os.path.isfile("/tmp/hash_values.csv"):
        print("\n\n'hash_values.csv ' baseline file detected\n\nHashing File System & Comparing to Baseline File...")
        hash_and_compare()
        quit()
    else:
        print("\n\n'hash_values.csv' baseline file not detected\n\nHashing File System & Creating Baseline File")
        hash_baseline()
        quit()

def hash_baseline():
    f_write = open("/tmp/hash_values.csv", "w")
    for root, dirs, files in os.walk("/"):
        if root in bad:
            dirs[:]=[]
            files[:]=[]
        path = root.split(os.sep)
        for file in files:
            filepath=os.path.join(root,file)
            sha256=hashlib.sha256()
            try: 
                f=open(filepath, "rb")
            except:
                f.close()
                continue
            while 1:
                bufffer=f.read(4096)
                if not bufffer:
                    break
                sha256.update(bufffer)
            f.close()
            now=datetime.datetime.now()
            file1 = (filepath)
            hash1 = (sha256.hexdigest())
            date = (str(now))
            final_str = file1 + ',' + hash1 + ',' + date + '\n'
            f_write.write(final_str)
    f_write.close()

def hash_and_compare():
    with open('/tmp/hash_values.csv') as f:
        oldHashList = f.readlines()
    changes = list()
    f_write = open("/tmp/hash_values.csv", "w")
    for root, dirs, files in os.walk("/"):
        if root in bad:
            dirs[:]=[]
            files[:]=[]
        path = root.split(os.sep)
        for file in files:
            filepath=os.path.join(root,file)
            sha256=hashlib.sha256()
            try: 
                f=open(filepath, "rb")
            except:
                f.close()
                continue
            while 1:
                bufffer=f.read(4096)
                if not bufffer:
                    break
                sha256.update(bufffer)
            f.close()
            now=datetime.datetime.now()
            file1 = (filepath)
            hash1 = (sha256.hexdigest())
            date = (str(now))
            final_str = file1 + ',' + hash1 + ',' + date + '\n'
            if search_array(hash1 in x for x in oldHashList) == False:
                changes.append(final_str)
            f_write.write(final_str)
    f_write.close()
    print("\n\nChanges have been noticed in the following files (file,hash,time):\n")
    for i in changes:
        print (i + '\n')
main()
