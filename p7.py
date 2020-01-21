def companyName(email):
    return email.split('@')[-1].split('.')[0]

print('Comapany Name:', companyName(input()))