from cryptography.fernet import Fernet

# #Creating encryption key
# key = Fernet.generate_key()  

# with open('mykey.key', 'wb') as mykey:    #to see the key
#     mykey.write(key)    


#To load encryption key someone shared whic is also called mykey.key 
with open('mykey.key', 'rb') as mykey:
    key = mykey.read()

print(key)  #just to check we have same key as in mykey.key file 

#encrypt a file using key
# f = Fernet(key)

# with open('grades.csv', 'rb') as original_file:
#     original = original_file.read()

# encrypted = f.encrypt(original)

# with open('enc_grades.csv', 'wb') as encrypted_file:
#     encrypted_file.write(encrypted)

#Decrypting file to its original form 
f = Fernet(key)

with open('enc_grades.csv', 'rb') as encrypted_file:
    encrypted = encrypted_file.read()

decrypted = f.decrypt(encrypted)

with open('dec_grades.csv', 'wb') as decrypted_file:
    decrypted_file.write(decrypted)
