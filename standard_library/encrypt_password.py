import bcrypt

#Hash a password
#signup
passowrd=b'mysecretepassword'
hashed_password=bcrypt.hashpw(passowrd,bcrypt.gensalt())
print(hashed_password)

#Store the hashed passsword in a database
#store in database(hashed password)

#check if a password matches a hash
#login
password_to_check=b'mysecretepassword'
stored_hashed_password=hashed_password
if bcrypt.checkpw(password_to_check,stored_hashed_password):
    print("Password is CORRECT!")
else:
    print("Password is incorrect!")
    

