import os
import random

L = []

localpath = os.getcwd()
for files in os.walk('picture'):
    for file in files:  
        L.append(file)

with open('picture.txt','w') as pic:
    for each in L[2]:
        pic.write(each + '\n')
pic.close()

with open('picture.txt') as pic:
    picread = pic.read()
pic.close()

P = picread.split('\n')
print(random.choice(P))