import os
from os import listdir
from os.path import isfile, join
import glob
import re
import csv
import itertools


path="/Users/valarmathipukuraj/Documents/August/PythonTask1/test"

file_list = os.listdir(path)
values = []
for f in file_list:
    with open(join(path, f), "r") as inputfile:
      for line in csv.reader(inputfile, delimiter=' '):
        values.append(map(str, line.split('\t')))
        # l = [ map(str,line.split('\t')) for line in f ]

print ("rows:", values)
print ("columns")
for column in values:
    print (column)
