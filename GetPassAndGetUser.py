# A simple Python program to demonstrate
# getpass.getpass() to read security question
import getpass

p = getpass.getpass(prompt='Your favorite flower? ')

if p.lower() == 'rose':
    print('Welcome..!!!')
else:
    print('The answer entered by you is incorrect..!!!')e