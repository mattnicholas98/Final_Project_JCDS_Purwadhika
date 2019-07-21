import numpy as np
import pandas as pd

dataHeart = pd.read_csv('./datasets/heart.csv',)
# print(dataHeart)
# print(dataHeart.isnul().sum())

dataX = dataHeart.drop(['target'], axis='columns') 
# print(dataX.columns.values)
dataY = dataHeart['target']

# splitting for training and testing
from sklearn.model_selection import train_test_split

xtrain, xtest, ytrain, ytest = train_test_split(
    dataX,
    dataY,
    test_size = 0.1
)

from sklearn.linear_model import LogisticRegression

# using LogisticRegression for this particular dataset since it is the most popular and accurate
model = LogisticRegression(solver='liblinear', multi_class='auto')
model.fit(xtrain, ytrain)

print(round(model.score(xtest, ytest) * 100, 2), '%')

# jadiin file joblib
import joblib
joblib.dump(model, 'heartModel')