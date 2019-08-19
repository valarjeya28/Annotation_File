import os
from os import listdir
from os.path import isfile, join
import glob
import re
# read_files = glob.glob("test/*.ann")
path="/Users/valarmathipukuraj/Documents/August/PythonTask1/test"
# read_files = glob.glob("*.ann")
file_list = os.listdir(path)
# file_list = [f for f in listdir(path) if isfile(join(path, f)) and f.split('.')[1] == 'ann']

# print(file_list)
ID=[]
other=[]
# with open("result.txt", "wb") as outfile:
for f in file_list:
    # print(f)
    #   infile=glob.glob(f)
    with open(join(path, f), "r") as inputfile:
        data = inputfile.readlines()
        
        # re.sub('?', ' ', data)
    #    print(data)
        for lines in data:
        # content = infile.readlines()
            # print(lines)
            # if re.match(r'^\s*$', lines):
            #  lines.decode('utf-8')
             a=re.search(r'\b(ID)\b',lines)
            #  re.sub('?', '', lines)
            #  lines.replace("?", "")
             
             if a:
                
                ID.append(lines)
                
             else:
                other.append(lines)
                   
        with open('result.txt', 'a') as fileout:
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
# with open('result.txt','r') as infile, open('output.txt', 'w') as outfile:
#             for line in infile:
#                 if not line.strip(): continue  # skip the empty line
#                 outfile.write(line)
          