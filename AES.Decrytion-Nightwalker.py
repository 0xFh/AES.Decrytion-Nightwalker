#!/usr/bin/env python3
#
# This is a simple script to decrypt the flag for 'Night_Walker' CTF Challenge which is using AES[CBC Mode] Encryption.
#
# You can find the challenge f:  https://cybertalents.com/challenges/malware/night-walker
#
# 
# Before running the script, you must install pycryptodome:
#
# $ python -m pip install PyCryptodome
#
#
##################################################

from Crypto.Cipher import AES

if __name__ == '__main__':

    with open('flag.txt','rb') as flagFile:
        x=flagFile.read()

#initializing key and iv
    key = b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0A\x0B\x0C\x0D'
    pad = b'\x0E\x0F'
    iv = key + pad	#This is 'Initialization Vector' and should be 16 bytes (in binary)
    flag = str("")

    print('\nDecrypting flag.txt , Please wait ...')

    for i in range(120):
        for j in range(120):
            tmp = key+chr(i).encode()+chr(j).encode()
            cipher = AES.new(tmp, AES.MODE_CBC, iv)
            plaintext = cipher.decrypt(x)
            if b'[Window:' in plaintext:
                flag = flag + str((plaintext.decode()))


#Convert flag to List for deleting the useless strings

flag = flag.split('\n')

#This is the length of the useless string maybe different from date to date so change it if necessary
len1 = len("[Window: flag.txt - WordPad - at Mon Aug  3 04:23:16 2020] ")

for i in range(len(flag)):
    flag[i] = flag[i][len1:]

flag = flag[0:len(flag)-6]


#Convert flag to string for replacing characters "[SHIFT] [ ] -" with "{ } -"
def listToString(str1): 
    str1 = ""
    return(str1.join(flag))
flag = listToString(flag)

#replacing
flag = flag.replace("[SHIFT][","{")
flag = flag.replace("[SHIFT]]","}")
flag = flag.replace("[SHIFT]-","_")


#Print The Final Result
print("\n------------------Flag--------------------\n")
print(flag)
print("\n------------------------------------------\n")