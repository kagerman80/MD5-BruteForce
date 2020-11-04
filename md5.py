""" Given is a md5 hash of a five digits long PIN. It is given as string.
    The task is to return the cracked PIN """


import hashlib

def gethash(x):
    return hashlib.md5(str(x).zfill(5).encode("utf-8"))

def findpin(hash):
    for x in range(99999):
        #print(gethash(x).hexdigest())
        if gethash(x).hexdigest() == hash:
            print("PIN has been found: ", str(x).zfill(5))
            break
        else: continue

findpin("05237ace2c45a84c5de58fec1a099127")