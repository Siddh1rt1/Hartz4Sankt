from flask import Flask, request, render_template, jsonify, json
import openpyxl
from pathlib import Path
import csv
import pandas as pd
from csv import reader
app = Flask(__name__)
tac=0

@app.route('/')
def hello():
    print("log1")
    teno="Kiel"
    onlo= ['JC Kiel', ' Landeshauptstadt;13102;2.628126118;2.591041946;2.408265891;2.486664575;2.346351208;2.466912053;2.553224919;2.549775714;2.673775514;2.63315859;2.722732399;2.590317627;2.587874879;2.715205149;2.739615972;2.755842063;2.607467205;2.526315789;2.454460627;2.620087336;2.693658335;2.745652717;2.572589768;2.645280484;2.624660964;2.690732849;2.727310696;2.830386764;2.713916762;2.777540746;2.658092176;2.66014966;2.45078697;2.366209642;2.308931448;2.144977066;1.607414704;0.949225396;0.489824999;0.454054054;0.505439904;0.659190138;0.489312387;0.332944178;0.158151386;0.250055816;0.478554497;0.705776579;0.766369381;0.75031078;0.63711176;0.501820766;0.343137255;0.305453239;0.304933552;0.379506641;0.679538851']
    bata= ['Ort;ID;1701 |Jan;1702 |Feb;1703 |Mär;1704 |Apr;1705 |Mai;1706 |Jun;1707 |Jul;1708 |Aug;1709 |Sep;1710 |Okt;1711 |Nov;1712 |Dez;1801 |Jan;1802 |Feb;1803 |Mär;1804 |Apr;1805 |Mai;1806 |Jun;1807 |Jul;1808 |Aug;1809 |Sep;1810 |Okt;1811 |Nov;1812 |Dez;1901 |Jan;1902 |Feb;1903 |Mär;1904 |Apr;1905 |Mai;1906 |Jun;1907 |Jul;1908 |Aug;1909 |Sep;1910 |Okt;1911 |Nov;1912 |Dez;2001 |Jan;2002 |Feb;2003 |Mär;2004 |Apr;2005 |Mai;2006 |Jun;2007 |Jul;2008 |Aug;2009 |Sep;2010 |Okt;2011 |Nov;2012 |Dez;2101 |Jan;2102 |Feb;2103 |Mär;2104 |Apr;2105 |Mai;2106 |Jun;2107 |Jul;2108 |Aug;2109 |Sep']
    return render_template('index.html',textname=teno, data=onlo, bata=bata)

@app.route('/', methods=['POST'])
def my_form_post():
    in_text = request.form['text']
    with open('main_full_percent.csv','r') as read_obj:
        csv_reader = reader(read_obj)
        for row in csv_reader:
            
            if "ID" in str(row):
                bata=row
            if str(in_text) in str(row):
                print(row)
                print("YESYES")
                dow=row
                return render_template('index.html',data=dow,bata=bata,textname=in_text)
            else:
                tac+1
    with open("data_dos_point_old.txt", "r") as fp:
        print("opened data")
        lines = fp.readlines()

    x=0
    print("log1")
    onlo= ['JC', 'Kiel,', 'Landeshauptstadt', '13102', '2.366209642', '2.308931448', '2.144977066', '1.607414704', '0.949225396', '0.489824999', '0.454054054', '0.505439904', '0.659190138', '0.489312387', '0.332944178', '0.158151386', '0.250055816', '0.478554497', '0.705776579', '0.766369381', '0.75031078', '0.63711176', '0.501820766', '0.343137255', '0.305453239', '0.304933552', '0.379506641', '0.679538851']
    bata= ['1910', '1911', '1912', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2101', '2102', '2103', '2104', '2105', '2106', '2107', '2108', '2109']
    for line in lines:
        if (str(in_text) in str(line)):

            t=x 
            break
        else :
            print("tik")
            x=x+1
            if x==446:
                print("log2")
                return render_template('index.html',data=onlo, bata=bata) 
            

    print(x)
    stra=(lines[x])
    print(stra)

    b=stra.split()

    

    stra=(lines[0])
    c=stra.split()
    del c[0]
    del c[0]
    return render_template('index.html',data=b, bata=c)


if __name__ == '__main__':
  app.run(debug=True)