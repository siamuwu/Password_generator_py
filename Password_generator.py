import random
import string

x = int (input("How long your password will be? : "))
while x>8:
    print ('Password is too long')
    x = int (input("How long your password will be? : "))


set_char = string.ascii_letters + string.digits + string.punctuation
#print (set_char)

char = ""

for i in range (x):
    char += random.choice (set_char)

print ("Your password is ", char)