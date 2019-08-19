import os
from os import listdir
from os.path import isfile, join
import glob
import re
# read_files = glob.glob("test/*.ann")
path="/Users/valarmathipukuraj/Documents/PythonTask/test"
# read_files = glob.glob("*.ann")
file_list = os.listdir(path)
# file_list = [f for f in listdir(path) if isfile(join(path, f)) and f.split('.')[1] == 'ann']

print(file_list)
ID=[]
other=[]
# with open("result.txt", "wb") as outfile:
for f in file_list:
    # print(f)
    #   infile=glob.glob(f)
    with open(join(path, f), "rb") as inputfile:
       data = inputfile.readlines()
    #    print(data)
       for lines in data:
        # content = infile.readlines()
            # print(lines)
            a=re.search(r'\b(ID)\b',lines)
            if a:
                ID.append(lines)
            else:
                other.append(lines)
with open('result.txt', 'w') as fileout:
                    for item in ID:
                        fileout.write("%s" % item) 
# with open('result.txt', 'w') as fileout:
                    for item in other:
                            fileout.write("%s" % item)
 
            