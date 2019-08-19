import os
from os import listdir
from os.path import isfile, join
import glob
import re

path="/Users/valarmathipukuraj/Documents/August/PythonTask1/test"

file_list = os.listdir(path)

ID=[]
other=[]
for f in file_list:
    with open(join(path, f), "r") as inputfile:
        data = inputfile.readlines()
        for lines in data:
             a=re.search(r'\b(ID)\b',lines)
             months=re.search(r'\b(January)\b',lines)
             if a:
                 ID.append(lines)
                 if months:
                    other.append(lines)
             else:
                 pass
        with open('result.csv', 'a') as fileout:
                    for item in ID:
                        # if not item.strip():
                        # item.rstrip('?')
                        item = re.sub('[?]', '', item)
                        if not item.strip(): continue 
                        fileout.write("%s" % item) 
# with open('result.txt', 'w') as fileout:
                    for item in other:
                        # if not item.strip():  
                        # item.rstrip('?')
                        item = re.sub('[?]', '', item)
                        if not item.strip(): continue   
                        fileout.write("%s" % item)
        ID=[]
        other=[]


