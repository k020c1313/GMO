import pandas as pd
import csv

data_df = pd.read_csv("../data/continuityDeleteData.csv", sep=",")
data_list = data_df.values.tolist()

for i in data_list:
    yyyymmdd = i[2]
    hhmmss = i[3]
    yyyymmdd_split = yyyymmdd.split("-") 
    hhmmss_split = hhmmss.split(":")
    i.insert(4, yyyymmdd_split[0])
    i.insert(5, yyyymmdd_split[1])
    i.insert(6, yyyymmdd_split[2])
    i.insert(7, hhmmss_split[0])
    i.insert(8, hhmmss_split[1])
    i.insert(9, hhmmss_split[2])
    
    try:
        seconds = int(hhmmss_split[0]) * 3600 + int(hhmmss_split[1]) * 60 + int(hhmmss_split[2])
        i.insert(10, seconds)
    except:
        seconds = int(hhmmss_split[0]) * 3600 + int(hhmmss_split[1]) * 60
        i.insert(10, seconds)
        
    
with open("../data/timeDatailSplitData.csv", "w") as file:
    writer = csv.writer(file, lineterminator="\n")
    writer.writerows(data_list)
 
    