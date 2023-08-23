#Strong password checker
#Must have at least 1 uppercase letter
#Must have at least 1 lowercase letter
#Must have at least 1 special character
#Must  be at least 8 characters long and at most 16 characters long
#Must have  at  least 1 number
#Must not have two consecutive characters that are same

password = input("Enter the password: ")
result = []

if 8 <= len(password) <= 16:
    result.append(True)
else:
    result.append(False)

uppercase = False

for i in password:
    if i.isupper():
        uppercase = True
result.append(uppercase)
lowercase = False

for i in password:
    if i.islower():
        lowercase = True
result.append(lowercase)
digit = False

for i in password:
    if i.isdigit():
        digit = True
result.append(digit)
spe_char = False

for i in password:
    if i == '@' or i == '$' or i == '_':
        spe_char = True
result.append(spe_char)

consecutive_char = True

for i in password:
    if i * 2 in password:
        consecutive_char = False
result.append(consecutive_char)

if all(result):
    print("Strong Password")
else:
    print("Weak Password")

print(result)






