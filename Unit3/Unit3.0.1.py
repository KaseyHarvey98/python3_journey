passwords = {'smith':'apple', 'jones':'a34xx', 'brown':'zzzz'}
username = input('username: ')
password = input('Password: ')
if password == passwords[username]:
    print('You are logged in.')
else:
    print('Bad password.')
