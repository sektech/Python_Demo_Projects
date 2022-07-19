email = input("Enter you email id : \n")
username = email.split("@")[0]
domain = email.split("@")[1]
print(f'your user name is : {username}')

print(f'your domain name is : {domain}')