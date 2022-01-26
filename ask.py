import openpyxl
from pathlib import Path
import csv
import pandas as pd

with open("data_dos_point.txt", "r", encoding="UTF-8") as fp:
    lines = fp.readlines()
testmain = "Dresden"
print(lines)
x=0
for line in lines:
    if str(testmain) in str(line):
        t=x 
        break
    else :
        x=x+1 

print(x)
print("this is"+lines[x])    


str=(lines[2])
b=str.split()
print(b)