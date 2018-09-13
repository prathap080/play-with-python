import os
import pyperclip
x = pyperclip.paste()
modified = []
data = x.split('\r\n')
#print(data)
for id in data:
	#print(id)
	modified.append(id)
#print(modified)	
dup = [i for i in modified if modified.count(i)>1]
##print(dup)
dup = set(dup)
z = "\n".join(dup)
##dup = set(z)
print(z)
pyperclip.copy(z)

