from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
import pandas as pd
import pickle

train_data = pd.read_csv("static/train.csv")

X = train_data.drop('price_range',axis=1)
y = train_data['price_range']

scaler = StandardScaler()
X = scaler.fit_transform(X)

lr= LogisticRegression()
lr.fit(X,y)

pickle.dump(lr,open('model.pkl','wb'))
print(lr.predict(scaler.transform([[1520,1,2.2,0,5,1,33,0.5,177,8,18,151,1005,3826,14,9,13,1,1,1]])))