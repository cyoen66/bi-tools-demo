import pandas as pd
from datetime import datetime
import pygwalker as pyg

def save_html_to_file(html_str, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(html_str)

file_path = 'MCCMBI.csv'
df = pd.read_csv(file_path);


#print(df)
#result = df.groupby('CompanyNm')['Uriage_S'].sum()
case1result = pd.crosstab(df['DateCd'], [df['CompanyNm'],df['KaishaBumonNm']], values=df['Uriage_S'], aggfunc='sum');
case2result = pd.crosstab([df['KaishaBumonNm'],df['DateCd']], df['CompanyNm'], values=df['Uriage_S'], aggfunc='sum');
case3result = pd.crosstab([df['KaishaBumonNm']], [df['DateCd'],df['CompanyNm']], values=df['Uriage_S'], aggfunc='sum');
html_str = pyg.to_html(df)
save_html_to_file(html_str, 'MCCMBI.html')
#print(case1result)
#case1result.to_csv('result1.csv', header=True)
#caseの結果をエクセルに出力
# 現在の時刻を取得してフォーマット
current_time = datetime.now().strftime('%Y%m%d_%H%M%S')

case1result.to_excel(f'case1result_{current_time}.xlsx', sheet_name='Sheet1', header=True)
case2result.to_excel(f'case2result_{current_time}.xlsx', sheet_name='Sheet1', header=True)
case3result.to_excel(f'case3result_{current_time}.xlsx', sheet_name='Sheet1', header=True)
#print(html_str)