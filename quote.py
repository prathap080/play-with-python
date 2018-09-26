import os
import pyperclip
os.chdir(r'C:\Users\chintare\Desktop')
x = pyperclip.paste()
modified = ""
data = x.split('\r\n')
#print(data)
for id in data:
	mod = ""+id.strip()+","
	modified = modified+mod
	pyperclip.copy(modified)