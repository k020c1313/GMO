import pandas as pd
from pytz import timezone
from dateutil import parser
import csv

data_df = pd.read_csv("../data/data.csv", sep=",")
data_list = data_df.values.tolist()

for i in data_list:
    jstTime = parser.parse(i[0]).astimezone(timezone("Asia/Tokyo"))
    jstTime_str = str(jstTime)
    jstTime_str = jstTime_str[:jstTime_str.find(".")]
    i.insert(1,jstTime_str)
    
    splitTime = jstTime_str.split()
    i.insert(2,splitTime[0])
    i.insert(3,splitTime[1])
    
    i.insert(4,int(jstTime.timestamp()))
    
with open("../data/timeFormatChangeData.csv", "w") as file:
    writer = csv.writer(file, lineterminator="\n")
    writer.writerows(data_list)
