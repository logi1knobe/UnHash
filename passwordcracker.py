import hashlib # library for hashing
title = '''

 /$$   /$$           /$$   /$$                     /$$      
| $$  | $$          | $$  | $$                    | $$      
| $$  | $$ /$$$$$$$ | $$  | $$  /$$$$$$   /$$$$$$$| $$$$$$$ 
| $$  | $$| $$__  $$| $$$$$$$$ |____  $$ /$$_____/| $$__  $$
| $$  | $$| $$  \ $$| $$__  $$  /$$$$$$$|  $$$$$$ | $$  \ $$
| $$  | $$| $$  | $$| $$  | $$ /$$__  $$ \____  $$| $$  | $$
|  $$$$$$/| $$  | $$| $$  | $$|  $$$$$$$ /$$$$$$$/| $$  | $$
 \______/ |__/  |__/|__/  |__/ \_______/|_______/ |__/  |__/

@logi1knobe
4/10/2023
'''
print(title)
print()
# Variables
pass_found = 0 # checks if cracked


# User Inputs
hashedtext = input("Enter Hashed String: ")
hashmethod = int(input("What hashing method\n1. md5\n2. sha1\n3. sha224\n4. sha256\n5. sha384\n"))


if hashmethod == 1:
    print("Unhashing md5...")
    hash_object = hashlib.md5(hashedtext.encode()) # encodes the hash
    unhashedtext = hash_object.hexdigest() # UnHashes
    print("Unhashed: " + unhashedtext)
elif hashmethod == 2:
    print("Unhashing sha1...")
    hash_object = hashlib.sha1(hashedtext.encode()) # encodes hash
    unhashedtext = hash_object.hexdigest() # UnHashes
    print("Unhashed: " + unhashedtext)
elif hashmethod == 3:
    print("Unhashing sha224...")
    hash_object = hashlib.sha224(hashedtext.encode()) # encodes hash
    unhashedtext = hash_object.hexdigest() # UnHashes
    print("Unhashed: " + unhashedtext)
elif hashmethod == 4:
    print("Unhashing sha256...")
    hash_object = hashlib.sha256(hashedtext.encode()) # encodes hash
    unhashedtext = hash_object.hexdigest() # UnHashes
    print("Unhashed: " + unhashedtext)
elif hashmethod == 5:
    print("Unhashing sha384...")
    hash_object = hashlib.sha384(hashedtext.encode()) # encodes hash
    unhashedtext = hash_object.hexdigest() # UnHashes
    print("Unhashed: " + unhashedtext)
