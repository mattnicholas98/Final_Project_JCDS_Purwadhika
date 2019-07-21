# importing all the main libraries
from flask import Flask, request, render_template, abort, jsonify, redirect, flash, url_for, send_from_directory
import joblib
from flask_mysqldb import MySQL
import requests
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import random

app = Flask(__name__, static_url_path='/static')
app.secret_key = 'dont tell anyone'     # used to flash messages
mysql = MySQL(app)
app.config['UPLOAD_FOLDER']='./'

# activate the SQL server to store all of the data input by the user
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'Matthew'
app.config['MYSQL_PASSWORD'] = 'Matthew1998'
app.config['MYSQL_DB'] = 'test_heart'

# home route
@app.route('/')
def home():
    return render_template('welcome.html')


# login page route
@app.route('/login')
def login():
    return render_template('login.html')


# dataset route
@app.route('/dataset')
def dataset():
    return render_template('dataset.html')


# showing personal data route
@app.route('/mydata', methods=['POST', 'GET'])
def mydata():
    if request.method == 'POST':
        userMail = request.form['userEmail']
        userPass = request.form['userPassword']

        # take all the required data in SQL to show in the next HTML
        x = mysql.connection.cursor()
        jml = x.execute(f"select * from mylogin where user_email = '{userMail}' and user_password = '{userPass}'")
        print(jml)

        if jml > 0:
            data = x.fetchall()

            allData = []
            for i in range(len(data)):
                age = data[i][2]
                sex = data[i][3]
                cp = data[i][4]
                trestbps = data[i][5]
                chol = data[i][6]
                fbs = data[i][7]
                restecg = data[i][8]
                thalach = data[i][9]
                exang = data[i][10]
                oldpeak = data[i][11]
                slope = data[i][12]
                ca = data[i][13]
                thal = data[i][14]

                datadict = {
                    "age": age,
                    "sex": sex,
                    "cp": cp,
                    "trestbps": trestbps,
                    "chol": chol,
                    "fbs": fbs,
                    "restecg": restecg,
                    "thalach": thalach,
                    "exang": exang,
                    "oldpeak": oldpeak,
                    "slope": slope,
                    "ca": ca,
                    "thal": thal
                }
                allData.append(datadict)
                print(allData)

            age1 = allData[0]['age']
            sex1 = allData[0]['sex']
            cp1 = allData[0]['cp']
            trestbps1 = allData[0]['trestbps']
            chol1 = allData[0]['chol']
            fbs1 = allData[0]['fbs']
            restecg1 = allData[0]['restecg']
            thalach1 = allData[0]['thalach']
            exang1 = allData[0]['exang']
            oldpeak1 = allData[0]['oldpeak']
            slope1 = allData[0]['slope']
            ca1 = allData[0]['ca']
            thal1 = allData[0]['thal']

            # [52.  1.    0.    125.      212.    0.      1.      168.       0.       1.       2.     2.    3]
            # age  sex   cp   trestbps   chol    fbs   restecg   thalach   exang   oldpeak   slope   ca   thal

            predictionHeart = model.predict([[
                age1, sex1, cp1, trestbps1, chol1, fbs1, restecg1, 
                thalach1, exang1, oldpeak1, slope1, ca1, thal1
            ]])

            predictionHeartProb = model.predict_proba([[
            age1, sex1, cp1, trestbps1, chol1, fbs1, restecg1, 
            thalach1, exang1, oldpeak1, slope1, ca1, thal1
            ]])

            prob = predictionHeartProb[0].max() * 100

            # replacing all the required information from integers to wordings; so that the user will be able to access easier
            # alongside with the wording, there will be some "popularity based" recommendation for some factors that contribute a lot to the target
            if int(predictionHeart) == 0:
                assumption = "You don't have a heart disease"
            else:
                assumption = "You might have a heart disease"

            if int(sex1) == 0:
                sex1 = "Female"
            else:
                sex1 = "Male"

            if int(cp1) == 0:
                cp1 = "Typical angina"
                cpRecommendation = 'Majority of patients DO NOT have heart disease caused by Typical angina. Consult with doctor regardless'
            elif int(cp1) == 1:
                cp1 = "Atypical angina"
                cpRecommendation = "Chest Pain plays a big role in this, consult with a doctor in order to resolve"
            elif int(cp1) == 2:
                cp1 = "Non-Anginal pain"
                cpRecommendation = "Chest Pain plays a big role in this, consult with a doctor in order to resolve"
            else:
                cp1 = "Asymptomatic"
                cpRecommendation = "Chest Pain plays a big role in this, consult with a doctor in order to resolve"

            if int(fbs1) == 0:
                fbs1 = "No"
            else:
                fbs1 = "Yes"
            
            if int(restecg1) == 0:
                restecg1 = "Normal"
            elif int(restecg1) == 1:
                restecg1 = "ST-T wave abnormality"
            else:
                restecg1 = "Probable/definite left ventricular hypertrophy"

            if int(exang1) == 0:
                exang1 = "No"
            else:
                exang1 = "Yes"

            if int(slope1) == 0:
                slope1 = "Upsloping"
                slopeRecommendation = "Upsloping slope may be dangerous! Consult with a doctor for further instructions"
            elif int(slope1) == 1:
                slope1 = "Flat"
                slopeRecommendation = "-"
            else:
                slope1 = "Downsloping"
                slopeRecommendation = "Downsloping slope is dangerous! Consult with a doctor for further instructions"
            
            if int(thal1) == 1:
                thal1 = "Normal"
            elif int(thal1) == 2:
                thal1 = "Fixed defect"
            else:
                thal1 = "Reversable defect"


            resultData = {
                'age': age1, 'sex': sex1, 'cp': cp1, 'trestbps': trestbps1,
                'chol': chol1, 'fbs': fbs1, 'restecg': restecg1, 'thalach': thalach1,
                'exang': exang1, 'oldpeak': oldpeak1, 'slope': slope1, 'ca': ca1,
                'thal': thal1, 'PREDICTION': assumption, 'PROB': round(prob)
            }

            return render_template('mydata.html', result = resultData, cprec = cpRecommendation, sloperec = slopeRecommendation)

        else:
            flash('Your account is not registered yet or your email/password is incorrect')
            return redirect(url_for('login'))

    else:
        return render_template('errorpage.html')        


# signup page route
@app.route('/signup')
def signup():
    return render_template('signup.html')


# checking if the account is registered or not
@app.route('/checking', methods=['GET', 'POST'])
def checking():
    if request.method == 'POST':
        userRegMail = request.form['userRegEmail']
        userRegPass = request.form['userRegPassword']

        x = mysql.connection.cursor()
        jml = x.execute(f"select * from mylogin where user_email = '{userRegMail}'")
        print(jml)

        if jml > 0:
            flash('Your account has already existed')
            return redirect(url_for('login'))
        else:
            x.execute('insert into mylogin (user_email, user_password) values (%s, %s)', (userRegMail, userRegPass))
            mysql.connection.commit()

            redirect(url_for('registering'))
            return render_template('registering.html', userRegMail = userRegMail)

    else:
        return render_template('errorpage.html')


# registering the account and all the data
@app.route('/registering', methods=['GET', 'POST'])
def registering():
    if request.method == 'POST':
        email = request.form['email']
        age = int(request.form['age'])
        sex = int(request.form['sex'])
        cp = int(request.form['cp'])
        trestbps = int(request.form['trestbps'])
        chol = int(request.form['chol'])
        fbs = int(request.form['fbs'])
        restecg = int(request.form['restecg'])
        thalach = int(request.form['thalach'])
        exang = int(request.form['exang'])
        oldpeak = float(request.form['oldpeak'])
        slope = int(request.form['slope'])
        ca = int(request.form['ca'])
        thal = int(request.form['thal'])

        x = mysql.connection.cursor()

        x.execute(f"update mylogin set age = {age}, sex = {sex},\
        cp = {cp}, trestbps = {trestbps}, chol = {chol}, fbs = {fbs},\
        restecg = {restecg}, thalach = {thalach}, exang = {exang}, oldpeak = {oldpeak},\
        slope = {slope}, ca = {ca}, thal = {thal} where user_email = '{email}'")

        mysql.connection.commit()

        jml = x.execute(f"select * from mylogin where user_email = '{email}'")
        print(jml)

        data = x.fetchall()
        allData = []
        for i in range(len(data)):
            age = data[i][2]
            sex = data[i][3]
            cp = data[i][4]
            trestbps = data[i][5]
            chol = data[i][6]
            fbs = data[i][7]
            restecg = data[i][8]
            thalach = data[i][9]
            exang = data[i][10]
            oldpeak = data[i][11]
            slope = data[i][12]
            ca = data[i][13]
            thal = data[i][14]

            datadict = {
                "age": age,
                "sex": sex,
                "cp": cp,
                "trestbps": trestbps,
                "chol": chol,
                "fbs": fbs,
                "restecg": restecg,
                "thalach": thalach,
                "exang": exang,
                "oldpeak": oldpeak,
                "slope": slope,
                "ca": ca,
                "thal": thal
            }
            allData.append(datadict)
            print(allData)

        age1 = allData[0]['age']
        sex1 = allData[0]['sex']
        cp1 = allData[0]['cp']
        trestbps1 = allData[0]['trestbps']
        chol1 = allData[0]['chol']
        fbs1 = allData[0]['fbs']
        restecg1 = allData[0]['restecg']
        thalach1 = allData[0]['thalach']
        exang1 = allData[0]['exang']
        oldpeak1 = allData[0]['oldpeak']
        slope1 = allData[0]['slope']
        ca1 = allData[0]['ca']
        thal1 = allData[0]['thal']

        predictionHeart = model.predict([[
            age1, sex1, cp1, trestbps1, chol1, fbs1, restecg1, 
            thalach1, exang1, oldpeak1, slope1, ca1, thal1
        ]])

        predictionHeartProb = model.predict_proba([[
            age1, sex1, cp1, trestbps1, chol1, fbs1, restecg1, 
            thalach1, exang1, oldpeak1, slope1, ca1, thal1
        ]])

        prob = predictionHeartProb[0].max() * 100

        # replacing all the required information from integers to wordings; so that the user will be able to access easier
        # alongside with the wording, there will be some "popularity based" recommendation for some factors that contribute a lot to the target
        if int(predictionHeart) == 0:
            assumption = "You don't have a heart disease"
        else:
            assumption = "You might have a heart disease"

        if int(sex1) == 0:
            sex1 = "Female"
        else:
            sex1 = "Male"

        if int(cp1) == 0:
            cp1 = "Typical angina"
            cpRecommendation = 'Majority of patients DO NOT have heart disease caused by Typical angina. Consult with doctor regardless'
        elif int(cp1) == 1:
            cp1 = "Atypical angina"
            cpRecommendation = "Chest Pain plays a big role in this, consult with a doctor in order to resolve"
        elif int(cp1) == 2:
            cp1 = "Non-Anginal pain"
            cpRecommendation = "Chest Pain plays a big role in this, consult with a doctor in order to resolve"
        else:
            cp1 = "Asymptomatic"
            cpRecommendation = "Chest Pain plays a big role in this, consult with a doctor in order to resolve"

        if int(fbs1) == 0:
            fbs1 = "No"
        else:
            fbs1 = "Yes"
        
        if int(restecg1) == 0:
            restecg1 = "Normal"
        elif int(restecg1) == 1:
            restecg1 = "ST-T wave abnormality"
        else:
            restecg1 = "Probable/definite left ventricular hypertrophy"

        if int(exang1) == 0:
            exang1 = "No"
        else:
            exang1 = "Yes"

        if int(slope1) == 0:
            slope1 = "Upsloping"
            slopeRecommendation = "Upsloping slope may be dangerous! Consult with a doctor for further instructions"
        elif int(slope1) == 1:
            slope1 = "Flat"
            slopeRecommendation = '-'
        else:
            slope1 = "Downsloping"
            slopeRecommendation = "Downsloping slope is dangerous! Consult with a doctor for further instructions"
        
        if int(thal1) == 1:
            thal1 = "Normal"
        elif int(thal1) == 2:
            thal1 = "Fixed defect"
        else:
            thal1 = "Reversable defect"

        resultData = {
            'age': age1, 'sex': sex1, 'cp': cp1, 'trestbps': trestbps1,
            'chol': chol1, 'fbs': fbs1, 'restecg': restecg1, 'thalach': thalach1,
            'exang': exang1, 'oldpeak': oldpeak1, 'slope': slope1, 'ca': ca1,
            'thal': thal1, 'PREDICTION': assumption, 'PROB': round(prob)
        }

        return render_template('mydata.html', result = resultData, cprec = cpRecommendation, sloperec = slopeRecommendation)

    else:
        return render_template('errorpage.html')

# 404 route
@app.errorhandler(404)
def error404(error):
    return render_template('errorpage.html')


if __name__ == '__main__':
    model = joblib.load('heartModel')
    app.run(debug = True)