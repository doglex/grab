from parse_page import column_order
import pandas as pd
from os import listdir
from datetime import datetime

dir_from = "store"
files = listdir(dir_from)

df_collector = []
for i, filename in enumerate(files[:10]):
    print(f"{datetime.now()} => {i+1}/{len(files)}: {filename}")
    if not filename.endswith(".csv"):
        continue
    df = pd.read_csv(f"{dir_from}/{filename}", header=None, names=column_order)
    # print(df)
    df_collector.append(df)

df_all = pd.concat(df_collector, axis=0)
print(df_all)
df_all.to_excel("蛋蛋赞总索引.xlsx")
print("done!")
