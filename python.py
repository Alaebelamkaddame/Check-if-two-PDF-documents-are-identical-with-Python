#importing Libraries
import hashlib
from difflib import SequenceMatcher

#Defining the hash_file Function
def hash_file(fileName1, fileName2):
    #fileName1: Name or path of the first file.
    h1 = hashlib.sha1() 
    #fileName2: Name or path of the fsecond file.
    h2 = hashlib.sha1()

    #reading the first file
    with open(fileName1, "rb") as file: 
        chunk = 0
        while chunk != b'': 
            chunk = file.read(1024) 
            h1.update(chunk) 

    #reading the second file
    with open(fileName2, "rb") as file: 
        chunk = 0
        while chunk != b'': 
            chunk = file.read(1024) 
            h2.update(chunk) 
    
    #Returning the Hashes
    return h1.hexdigest(), h2.hexdigest() 

#excecuting the function 
msg1, msg2 = hash_file("pd1.pdf ", "pd1.pdf")

#the if statement for the result
if(msg1 != msg2): 
    print("These files are not identical") 
else: 
    print("These files are identical")




    