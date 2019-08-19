import os
from os import listdir
from os.path import isfile, join
import glob
import re
# read_files = glob.glob("test/*.ann")
path="/Users/valarmathipukuraj/Documents/Tasks/August/PythonTask1/Tags"
# read_files = glob.glob("*.ann")
file_list = os.listdir(path)
# file_list = [f for f in listdir(path) if isfile(join(path, f)) and f.split('.')[1] == 'ann']

# print(file_list)
ID=[]
Date=[]
Maturityd=[]
# flagdate=[]
# flagmat=[]
# with open("result.txt", "wb") as outfile:
for f in file_list:
    # print(f)
    #   infile=glob.glob(f)
    with open(join(path, f), "r") as inputfile:
        data = inputfile.readlines()
        
        # re.sub('?', ' ', data)
    #    print(data)
        # a=re.search(r'\b(ID)\b',data)
        # if a:
        for lines in data:
        # content = infile.readlines()
            # print(lines)
            # if re.match(r'^\s*$', lines):
            #  lines.decode('utf-8')
             a=re.search(r'\b(ID)\b',lines)
             b=re.search(r'(\b(doc))|(\b(docm))',lines)
             
            #  re.sub('?', '', lines)
            #  lines.replace("?", "")
             if a: 
               if  b: 
                ID.append(lines.split("\t")[1])
                id_f=lines.split("\t")[1]
                id_doc=lines.split("\t")[2].rstrip()
                id_doc=re.sub('[?]', '', id_doc)
                for lines in data:
                  if re.search(r'\b(Date)\b',lines):
                        
                        Date.append(lines.split("\t")[2])
                        constval="-1"
                        splitdate=lines.split("\t")[1]
                        with open('NewReportFriday.txt', 'a') as fileout:
                                fileout.write("%s\t" % id_doc)
                                fileout.write("%s\t" %splitdate.split(" ")[1] )
                                fileout.write("%s" %splitdate.split(" ")[2] )
                                fileout.write("\t%s\t" % constval)
                                fileout.write("%s" % id_f)
                                fileout.write("\t%s" % lines.split("\t")[2])
                                
                                
        #       print(Date)
                        # flagdate.append(-1)
                  if re.search(r'\b(MaturityD)\b',lines):
                        # ID.append(lines)
                        Maturityd.append(lines.split("\t")[2])
                        constval="1"
                        splitdate=lines.split("\t")[1]
                        with open('NewReportFriday.txt', 'a') as fileout:
                                fileout.write("%s\t" % id_doc)
                                fileout.write("%s\t" %splitdate.split(" ")[1] )
                                fileout.write("%s" %splitdate.split(" ")[2] )
                                fileout.write("\t%s\t" % constval)
                                fileout.write("%s" % id_f)
                                fileout.write("\t%s" % lines.split("\t")[2])
                                
                        # flagmat.append(1)

                   
#         with open('parseresulttest.txt', 'a') as fileout:
#                         for item1 in ID:
#                         # if not item.strip():
#                         # item.rstrip('?')
#                                 item1 = re.sub('[?]', '', item1)
#                         # if not item1.strip(): continue 
#                                 # fileout.write("%s" % item1) 
# # with open('result.txt', 'w') as fileout:
#                                 for item2 in Date:
#                         # if not item.strip():  
#                         # item.rstrip('?')
#                         #   constval= "-1"
#                                         item2 = re.sub('[?]', '', item2)
#                                 if not item2.strip(): continue 
#                         #   fileout.write("-1\t")
#                                 fileout.write("%s" % item1)  
#                                 fileout.write("\t%s" % item2)
#                         #   fileout.write("%s\t"% constval)
#                                 for item3 in Maturityd:
#                         # if not item.strip():  
#                         # item.rstrip('?')
#                         #   constmatval="1"
#                                         item3 = re.sub('[?]', '', item3)
#                                 if not item3.strip(): continue
#                         #   fileout.write("1\t")  
#                                 fileout.write("%s" % item1)  
#                                 fileout.write("\t%s" %item2)
#                         #   fileout.write("%s\t" % constmatval)
                          
        ID=[]
        Date=[]
        Maturityd=[]
# with open('result.txt','r') as infile, open('output.txt', 'w') as outfile:
#             for line in infile:
#                 if not line.strip(): continue  # skip the empty line
#                 outfile.write(line)
          