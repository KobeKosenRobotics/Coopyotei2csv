import datetime
import os
import argparse
import pdf2csv

parser = argparse.ArgumentParser()

parser.add_argument('-auto', '--auto-path', action='store_true', help='Using default path to pdf and csv')
parser.add_argument('-pdf', '--pdf-path', type=str, default='', help='Path to pdf')
parser.add_argument('-csv', '--csv-path', type=str, default='', help='Path to csv')

args = parser.parse_args()

if args.auto_path == True:
    now = datetime.datetime.now()
    year = now.strftime("%Y")
    month = now.strftime("%m")
    pdf_file_path = "http://www.kobe-kosen.ac.jp/groups/coop/coopyotei" + month + ".pdf"
    csv_file_path = os.path.dirname(__file__) + "/output/csv/" + year + month + ".csv"
else:
    pdf_file_path = args.pdf_path
    csv_file_path = args.csv_path


#csvに変換して出力
print('converting...')
print('output: '+ str(csv_file_path))

pdf2csv.convert(pdf_file_path).to_csv(csv_file_path, index = False,header=False)
print('succesfull')