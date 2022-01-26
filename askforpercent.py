import openpyxl
from pathlib import Path
import csv
main_file = Path('computed','quote2018.xlsx')
main_obj = openpyxl.load_workbook(main_file)
main_sheet = main_obj["1. Kürzung"]
month = 1701
char="C"
charadd=""
print(char)
month_sheet="3.1 eLb insg"
Monat=['Jan','Feb','Mär','Apr','Mai','Jun','Jul','Aug','Sep','Okt','Nov','Dez']
h=0
while (month >=1701) and (month<=2109) :
    if month==1901:
        
        print("delete")
    if month==1707:
        month_sheet="3.1 ELB insg"
    strmonth=str(month)
    title="sanktionen-d-0-20"+strmonth+"-xlsx.xlsx"
    xlsx_file = Path('datensatz',title)
    wb_obj = openpyxl.load_workbook(xlsx_file)
    start_cell=11
    print(charadd+char+str(month))
    sheet = wb_obj[month_sheet]
    x=start_cell
    print("charadd "+charadd)
    d=x-2
    main_sheet[str(charadd)+str(char)+str(1)].value=str(month)+" |"+Monat[h]
    h=h+1
    if h==12:
        h=0
    for x in range(start_cell,456):
 
        a=(sheet[("I"+str(x))].value)
        x=x-d
        main_sheet[str(charadd+char+str(x))].value=a
        x=x+d+1
    main_obj.save(filename = 'computed/main_full_percent.xlsx')
    month=month+1
    if (int(month) == 1913) or (int(month) == 2013)or (int(month) == 1813)or (int(month) == 1713):
        month=month+88
    if char=="Z":
        print("i am in")
        if charadd=="A":
            charadd="B"
        else: 
            charadd="A"
        char=str(chr(ord("A")-1))
        print("charadd"+charadd+" char+"+char)
    print("1"+char)
    char=str(chr(ord(char)+1))
    print("2"+char)    


