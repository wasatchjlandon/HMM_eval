import pandas as pd 
import matplotlib.pyplot as plot

#exec(open('/mnt/c/Users/willl/Downloads/dx_download_out_parser.py').read())

file = '/mnt/c/Users/willl/Downloads/out.txt'
n1=[]
for i in range(3):
    n1 += ["P" + str(i)]
df = pd.read_csv(file, sep=r'\s{2,}', names=n1, engine='python')
n1=[]
for i in range(6):
    n1 += ["P" + str(i)]
df = df['P2'].str.split('/', expand=True)
df.columns = n1
df['P6'] = df['P5'].str.split(' ').str.get(1)
df['P6'] = df['P6'].str[1:30]
df['P7'] = df['P5'].str.split(' ').str.get(0)
df['P8'] = df['P1'].str.split('_').str.get(0)
df['P9'] = df['P7'].str.replace('.special_cases.HMM_CNV', '.special_cases.HMM_CNV')
df['Path to File'] = '/' + df['P1'] + '/' + df['P2'] + '/' + df['P3'] + '/' + df['P4'] + '/' + df['P9']
df['New File Name'] = df['P8'] + df['P9'].str[3:]

with pd.ExcelWriter('/mnt/c/Users/willl/Downloads/dx_download_out_parser_out.xlsx') as writer:
    df.to_excel(writer, sheet_name='te')