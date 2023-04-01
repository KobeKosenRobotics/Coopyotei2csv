import pandas as pd
import re
import tabula


def convert(pdffile_path):
    condata = tabula.read_pdf(pdffile_path, stream=True,pages="1")
    df=pd.DataFrame(condata[0])
    df2=df.iloc[0:,[2,3]]       #営業時間部分を抽出

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