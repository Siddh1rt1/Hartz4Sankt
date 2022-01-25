import openpyxl
from pathlib import Path
import csv
main_file = Path('computed','main_full_percent.xlsx')
main_obj = openpyxl.load_workbook(main_file)
main_sheet = main_obj["1. Kürzung"]
month = 1910
char="C"
print(char)

while (month >=1901) and (month<=2109) :
    strmonth=str(month)
    title="sanktionen-d-0-20"+strmonth+"-xlsx.xlsx"
    xlsx_file = Path('datensatz',title)
    wb_obj = openpyxl.load_workbook(xlsx_file)
    month_sheet="3.1 ELB insg"
    start_cell=11
    print(char+str(month))
    sheet = wb_obj[month_sheet]
    x=start_cell

    d=x-2
    main_sheet[str(char)+str(1)].value=str(month)
    for x in range(start_cell,469):
 
        a=(sheet[("I"+str(x))].value)
        x=x-d
        main_sheet[str(char+str(x))].value=a
        x=x+d+1
    main_obj.save(filename = 'computed/main_full_percent.xlsx')
    month=month+1
    if (int(month) == 1913) or (int(month) == 2013):
        month=month+88

    char=str(chr(ord(char)+1))


