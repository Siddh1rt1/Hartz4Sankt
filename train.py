import openpyxl
from pathlib import Path
import csv
main_file = Path('computed','main.xlsx')
main_obj = openpyxl.load_workbook(main_file)
main_sheet = main_obj["1. Kürzung"]


datum=2201
xlsx_file = Path('data','22Dez.xlsx')
wb_obj = openpyxl.load_workbook(xlsx_file)
sheet = wb_obj["1. Kürzung"]
x=14
for x in range(14,469):
    x=str(x)
    a=(sheet[("C"+x)].value)
    x=int(x)
    x=x-12
    x=str(x)
    main_sheet["C"+x].value=a
    print(main_sheet["C"+x].value)
    x=int(x)+13
    print(x)
main_obj.save(filename = 'computed/main.xlsx')
