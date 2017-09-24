#生成随机码，包含字母和数字

import random
import string

#ulist = [] 旧版本

#for i in range(10):
#    password = "".join(random.choice(string.digits+string.ascii_letters)for i in range(30))
#    ulist.append(password)

#for i in ulist:
#    print(i)


def getrandom():
    return "".join(random.choice(string.digits+string.ascii_letters)for i in range(4))

for i in range(10):
    print("-".join(getrandom() for i in range(4)))
