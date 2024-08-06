import pandas as pd
 
# サンプルデータ
data = {'Product': ['Apples', 'Oranges', 'Bananas', 'Apples', 'Bananas', 'Bananas'],
        'Salesperson': ['John', 'John', 'Claire', 'Claire', 'John', 'Claire'],
        'Units': [5, 3, 8, 7, 2, 4]}
df = pd.DataFrame(data)
 
# 集計付きのクロスタブを使用
table = pd.crosstab(df['Salesperson','Product'], df['Product'], values=df['Units'], aggfunc='sum')
print(table)