
from flask import Flask, request, url_for, redirect, render_template
import pickle
import numpy as np

flask_app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))
@flask_app.route('/')

def hello_world():
    return render_template('index.html')

@flask_app.route("/predict", methods =["POST"])
def predict():
    age=request.form['age']
    sex=request.form['sex']
    BMI=request.form['bmi']
    Childrens=request.form['children']
    smoke=request.form['smoker']
    Region =request.form['region']
    # features = [np.array([age,sex,BMI,Childrens,smoke,Region])]

    charge_per_smoker=0
    if(smoke==1):
        charge_per_smoker=32050.231832
    else:
        charge_per_smoker=8434.268298

    charge_per_sex=0
    if(sex==1):
        charge_per_sex=13956.751178	
    else:
        charge_per_sex=12569.578844	

    charge_per_children=0
    if(Childrens==0):
        charge_per_children=12365.975602
    elif(Childrens==1):
        charge_per_children=12731.171832
    elif(Childrens==2):
        charge_per_children=15073.563734
    elif(Childrens==3):
        charge_per_children=15355.318367	
    elif(Childrens==4):
        charge_per_children=13850.6563112
    elif(Childrens==5):
        charge_per_children=8786.03524722222
    features = [np.array([age, sex, BMI, Childrens, smoke, Region, charge_per_sex, charge_per_children, charge_per_smoker])]


    prediction = model.predict(features)

    return render_template("index.html", prediction_text ="The insurance cost is {}".format(prediction))

if __name__ == "__main__":
    flask_app.run(debug=True)