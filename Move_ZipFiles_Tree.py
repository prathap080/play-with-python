import os
from pathlib import Path
import shutil
from tkinter import Tk
from tkinter.filedialog import askdirectory

mon = {	'01':'Janauary',
		'02':'February',
		'03':'March',
		'04':'April',
		'05':'May',
		'06':'June',
		'07':'July',
		'08':'August',
		'09':'September',
		'10':'October',
		'11':'November',
		'12':'December'
        }

def file_move(source, destination):
    
    for i in os.listdir(source):
        if i.endswith('.zip'):
            date = i.split('-')
            month = mon[date[1]]
            year1 = date[2].split('.')
            year = year1[0]
            Path(f'{destination}/{year}/{month}').mkdir(parents=True, exist_ok=True)
            shutil.copy(source+'/'+i, destination+'/'+year+'/'+month+'/'+i)




source = './inputdata'
source1 = askdirectory(title="Select Folder") # shows dialog box and return the path
source = os.path.normpath(source1)
##    source.split(os.sep)
destination = './adhar1'
destination = input(r'Enter output path:')
file_move(source, destination)



'''
basedir = '/Users/jeevankumar/Desktop/adhar'

for i in os.listdir(source):
    date_data = os.path.splitext(i)[0]
    date = parser.parse(date_data)
    month = date.month
    year =date.year
    print(month, year)



for i in os.listdir('/Users/jeevankumar/Desktop/inputdata'):
    if i.endswith('.zip'):
        date = i.split('-')
        month = date[1]
        year1 = date[2].split('.')
        year = year1[0]



Path(f'{basedir}/{t.year}/{t.month:02d}').mkdir(parents=True, exist_ok=True)
date_data = os.path.splitext(i)[0]
date = parser.parse(date_data)
month = date.month
year =date.year
Path(f'{destination}/{date.year}/{date.month}').mkdir(parents=True, exist_ok=True)


'''
