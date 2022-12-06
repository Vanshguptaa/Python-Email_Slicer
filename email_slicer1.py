email = input("Enter your Email: ").strip()
username = email[:email.index('@')]
domain = email[email.index('@')+1:]
b=domain.upper()
a=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',' ']
for i in a:
    if i in email:
        print("Invalid email")
        break
else:
    print(f"username: {username} and  domain: {b}")
