import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import pickle


# loading the csv file
df=pd.read_csv("insurance.csv")

# select independent and dependent variables
x = df[['age', 'bmi', 'children', 'smoker', 'region', 'sex', 'Avg_charges_Per_sex', 'Avg_charges_Per_no_of_children', 'Avg_charges_Per_smoker']]
y = df['charges']


#split the dataset into train and test
x_train,x_test,y_train,y_test=train_test_split(x, y, test_size=0.2, random_state=15)

#convert categorical value to numerical labels
print(df.head())

#model building
regressor = RandomForestRegressor(n_estimators=100)
regressor.fit(x_train, y_train)

#Make pickle file of our model
pickle.dump(regressor,open("model.pkl", "wb"))