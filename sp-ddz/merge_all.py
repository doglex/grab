from parse_page import column_order
import pandas as pd
from os import listdir
from datetime import datetime

dir_from = "store"
files = listdir(dir_from)

df_collector = []
for i, filename in enumerate(files[:]):
    print(f"{datetime.now()} => {i+1}/{len(files)}: {filename}")
    if not filename.endswith(".csv"):
        continue
    df = pd.read_csv(f"{dir_from}/{filename}", header=None, names=column_order)
    # print(df)
    df_collector.append(df)



df_all = pd.concat(df_collector, axis=0)
print(df_all)
shape = df_all.shape[0]
size = 65530
for i, step in enumerate(range(0, shape, size)):
    print(f"write part {i+1}")
    df_tmp = df_all.iloc[step:step+size]
    df_tmp.to_excel(f"蛋蛋赞总索引_part_{i+1}.xlsx", engine="xlsxwriter")
print("done!")
