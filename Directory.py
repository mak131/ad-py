import os
w = os.walk('sms',topdown=True)
for i in w:
    print(i)