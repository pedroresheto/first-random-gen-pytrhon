import random

pass1 = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i',
         'o', 'p', 'a','s','d','f','g', 'h', 'j', 
         'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm',
         '1', '8', '9', '0']

password = ''

for x in range(16):
    password = password + random.choice(pass1)


print('Your password is: ', password)