import pandas as pd
import csv

data_df = pd.read_csv("../data/timeFormatChangeData.csv", sep=",")
data_list = data_df.values.tolist()

for i in range(len(data_list) - 1, 1, -1):
    back_userID = data_list[i - 1][5]
    forward_userID = data_list[i][5]
    if (back_userID == forward_userID): data_list.pop(i)
      
with open("../data/continuityDeleteData.csv", "w") as file:
    writer = csv.writer(file, lineterminator="\n")
    writer.writerows(data_list)
