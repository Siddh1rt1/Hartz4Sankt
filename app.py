from flask import Flask, request, render_template, jsonify, json
import openpyxl
from pathlib import Path
import csv
import pandas as pd

app = Flask(__name__)


@app.route('/')
def hello():
    print("log1")
    teno="Kiel"
    onlo= ['JC', 'Kiel,', 'Landeshauptstadt', '13102', '2.366209642', '2.308931448', '2.144977066', '1.607414704', '0.949225396', '0.489824999', '0.454054054', '0.505439904', '0.659190138', '0.489312387', '0.332944178', '0.158151386', '0.250055816', '0.478554497', '0.705776579', '0.766369381', '0.75031078', '0.63711176', '0.501820766', '0.343137255', '0.305453239', '0.304933552', '0.379506641', '0.679538851']
    bata= ['1910', '1911', '1912', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2101', '2102', '2103', '2104', '2105', '2106', '2107', '2108', '2109']
    return render_template('index.html',textname=teno, data=onlo, bata=bata)

@app.route('/', methods=['POST'])
def my_form_post():
    in_text = request.form['text']
    with open("data_dos_point.txt", "r") as fp:
        lines = fp.readlines()

    x=0
    onlo= ['JC', 'Kiel,', 'Landeshauptstadt', '13102', '2.366209642', '2.308931448', '2.144977066', '1.607414704', '0.949225396', '0.489824999', '0.454054054', '0.505439904', '0.659190138', '0.489312387', '0.332944178', '0.158151386', '0.250055816', '0.478554497', '0.705776579', '0.766369381', '0.75031078', '0.63711176', '0.501820766', '0.343137255', '0.305453239', '0.304933552', '0.379506641', '0.679538851']
    bata= ['1910', '1911', '1912', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2101', '2102', '2103', '2104', '2105', '2106', '2107', '2108', '2109']
    for line in lines:
        if str(in_text) in str(line):
            t=x 
            break
        else :
            x=x+1
            if x==444:
               return render_template('index.html',data=onlo, bata=bata) 
            

    print(x)
    stra=(lines[x])
    print(stra)
    stra.replace(',','.')
    print(stra)
    b=stra.split()

    

    stra=(lines[0])
    c=stra.split()
    del c[0]
    del c[0]
    return render_template('index.html',data=b, bata=c)


if __name__ == '__main__':
  app.run(debug=True)