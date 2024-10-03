import random
import string
lower="abcdefghijklmnopqrstuvwxyz"
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number="1234567890"
symbols="#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
all_chars=lower+upper+number+symbols
length=16 #password generate
password=''.join(random.sample(all_chars,length))
print("Generated Password is : ", password)