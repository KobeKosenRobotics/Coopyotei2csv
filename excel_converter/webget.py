from datetime import date
import datetime
import numpy as np
import matplotlib.pyplot as plt
import openpyxl
import os
import pandas as pd
import unicodedata
import re
import csv
import tabula

output_file_path=os.path.dirname(__file__)+"/csv/"
#output_file_path="csv/"
def webpdf_to_csv():
    dt_now = datetime.datetime.now()
    month=dt_now.month
    month_0=""
    if(month<10):
        month_0="0"
    pdffile_path="http://www.kobe-kosen.ac.jp/groups/coop/coopyotei"+month_0+str(month)+".pdf"

    condata = tabula.read_pdf(pdffile_path, stream=True,pages="1")
    df=pd.DataFrame(condata[0])
    #print(df.iloc[2,3])

    #営業時間部分を抽出
    df2=df.iloc[0:,[2,3]]


    out_list=[]
    for k in range(len(df2)):
        out_list.append(re.split('[:~]',df2.iloc[k,0])+re.split('[:~]',df2.iloc[k,1]))
    df3=pd.DataFrame(out_list)

    # Delete all but number & exception handling
    for i in range(len(df3)):
        for j in range(8):
            df3.iat[i,j] = re.sub(r'\D', '', str(df3.iat[i,j]))

            if df3.iat[i,j]=="":
                df3.iat[i,j] = "-1"
            elif int(df3.iat[i,j]) > 60:
                df3.iat[i,j] = "-2"
            
    return df3

dt_now = datetime.datetime.now()
year=dt_now.year
month=dt_now.month
#シート選択
if month<10:
    decade="0"
else:
    decade=""

file_path=output_file_path+str(year)+decade+str(month)+".csv"
print('output: '+ str(file_path))
#csvに変換して出力
webpdf_to_csv().to_csv(file_path, index = False,header=False)

