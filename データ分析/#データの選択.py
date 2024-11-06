#データの選択
import numpy as np
import pandas as pd
from tabulate import tabulate
import tkinter as tk
from tkinter import filedialog

# Tkinterウィンドウを作成（非表示）
root = tk.Tk()
root.withdraw()

# ファイル選択ダイアログを表示
file_path = filedialog.askopenfilename()

# 選択したファイルを読み込む
if file_path:
    df = pd.read_excel(file_path)
else:
    print("ファイルが選択されませんでした。")

# 1行目を表示（列名を確認する）
print("1行目のデータ:")
print(df.iloc[0])

# 2. 主となるデータの選択
# 例: "ColumnA"と"ColumnB"を使用すると仮定します
main_data_column = 'ColumnA'  # 主データの列名を指定
main_data = df[main_data_column].dropna()  # 欠損値は除外

# 3. 比較対象のデータの選択
comparison_column = 'ColumnB'  # 比較データの列名を指定
comparison_data = df[comparison_column].dropna()  # 欠損値は除外

# 選択した2つのデータの表示
print("ColumnA")
print(main_data)

print("ColumnB")
print(comparison_data)
