import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

##時間帯ごとの年齢
def func1():
    data_df = pd.read_csv("../data/supervisedData.csv", sep=",")
    data_df = data_df.iloc[:,[7,13]]
    data_list = data_df.values.tolist()
    
    count_list = [[0 for j in range(24)] for i in range(12)]

    
    for i in data_list:
        try:
            time_index = int(i[0])
            age_index = int(i[1]) // 10 - 1
            count_list[age_index][time_index] += 1
        except ValueError: pass
    
    
    df = pd.DataFrame(data = count_list)
    df = df.T
    df.plot()

##年齢ごとの使用OS
def func2():
    data_df = pd.read_csv("../data/supervisedData.csv", sep=",")
    data_df = data_df.iloc[:,[7,13,16]]
    data_list = data_df.values.tolist()
    
    
    count_list = [[0,0] for i in range(12)]
    
    for i in data_list:
        try:
            if i[2] == "iOS": os = 0
            if i[2] == "Android":os = 1
            age_index = int(i[1]) // 10 - 1
            count_list[age_index][os] += 1
        except ValueError: pass
    
    df = pd.DataFrame(data = count_list)
    df_ios = df.iloc[:,[0]].T
    df_and = df.iloc[:,[1]].T
    data_ios = df_ios.values.tolist()[0]
    data_and = df_and.values.tolist()[0]
    left = np.arange(len(data_ios))

    plt.bar(left, data_ios ,width = 0.3,align='center')
    plt.bar(left + 0.3, data_and ,width = 0.3,align='center')
    
    
func2()

