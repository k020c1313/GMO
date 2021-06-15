import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt


data_df = pd.read_csv("data.csv", sep=",")
data_list = data_df.values.tolist()

temp = pd.DataFrame(np.delete(data_list, 0, 1).astype(float))

X = temp.iloc[:, 1:6].values
Y = temp.iloc[:,0].values

plt.figure(figsize=(12, 12))
plt.xlim(0, 175)
plt.ylim(0, 130)

for i in range(100):
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, train_size = 0.7, test_size = 0.3)
    
    
    clf = linear_model.LinearRegression()
    clf.fit(X_train, Y_train)
    
    pred = clf.predict(X_test)
    print(pred)
    
    
    plt.scatter(Y_test[:1000], pred[:1000], alpha = 1, edgecolors = "red")