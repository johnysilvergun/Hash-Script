import hashlib
import pyfiglet
ascii_banner = pyfiglet.figlet_format("HASHER888!!")
print(ascii_banner)
hash_type = input('Enter Hash Mode: ').strip().upper()  # user input(s)
word_local = input('Enter file location: ').strip()
in_hash = input('Enter Hash: ').strip().lower()  
try:
    with open(word_local, 'r') as file:
        word_list = file.read().splitlines()
except FileNotFoundError:
    print(f"Error: File '{word_local}' not found.")
    exit()

# Hash each word and compare with input 
found = False
for word in word_list:
    if hash_type == "MD5":
        hash_obj = hashlib.md5(word.encode('utf-8'))
    elif hash_type == "SHA1":
        hash_obj = hashlib.sha1(word.encode('utf-8'))
    elif hash_type == "SHA224":
        hash_obj = hashlib.sha224(word.encode('utf-8'))
    elif hash_type == "SHA256":
        hash_obj = hashlib.sha256(word.encode('utf-8'))
    elif hash_type == "SHA384":
        hash_obj = hashlib.sha384(word.encode('utf-8'))
    elif hash_type == "SHA512":
        hash_obj = hashlib.sha512(word.encode('utf-8'))
    else:
        print('Error: Unsupported hash type')
        continue  # Skip to the next  if hash type is not there
# from this point its all outpout and debug 
    hashed = hash_obj.hexdigest().lower()
    print(f"Testing word '{word}' -> {hashed}")  

    if in_hash == hashed:
        print(f'HASH FOUND : {word}\n')
        found = True
        break  

if not found:
    print("Hash not found in the provided word list.")
