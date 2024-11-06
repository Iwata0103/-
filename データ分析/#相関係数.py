#相関係数
import numpy as np
import pandas as pd

df = pd.read_excel('国際経営学(1).xlsx')
col1 = df['投下金額'].tolist()
col2 = df['TVCM'].tolist()

print(np.corrcoef(col1, col2))

