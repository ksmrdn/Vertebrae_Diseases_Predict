from flask import Flask, jsonify, request, render_template
from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np
import joblib
import io
import base64
import matplotlib.pyplot as plt
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'ksmrdn'
app.config['MYSQL_PASSWORD'] = '1234567'
app.config['MYSQL_DB'] = 'history_vertebrae'

mysql = MySQL(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/form', methods = ['POST', 'GET'])
def form():
    return render_template('form.html') 
    

@app.route('/predict', methods = ['POST', 'GET'])
def predict():
   if request.method == "POST":
        input = request.form
        x = np.array([input['PI'],input['PT'],input['LLA'],input['SS'],input['PR'],input['DS']])
        # print(x)
        x = np.reshape(x, (1,-1))
        # dfX = pd.DataFrame([x])
        transformasi = fit_norm.transform(x)
        prediksi = model.predict(transformasi)
        prediksinya = prediksi[0]
        prediksi_proba = model.predict_proba(transformasi)
        prediksi_proba = prediksi_proba[0]
        
        # df_Bio = pd.DataFrame({"Name": input['Name'], "Gender": input['inlineRadioOptions'], "Age": input['Age'], "Height (cm)": input['Height'], "Weight (kg)": input['Weight'], "Job": input['Job']})
        # df_Atr = pd.DataFrame({"Pelvic Incidence": input['PI'], "Pelvic Tilt": input['PT'], "Lumbar Lordosis Angle": input['LLA'], "Sacral Slope": input['SS'], "Pelvic Radius": input['PR'], "Degree Spondylolisthesis": input['DS']}, index=[0])
       
        labels = ['Hernia', 'Normal', 'Spondylolisthesis']

        plt.close()
        plt.figure(figsize=(5,5))
        plt.title('Vertebrae Disease Probability')
        plt.pie(x=prediksi_proba, explode=[0.05,0.05,0.05], autopct='%1.1f%%', pctdistance=1.2, labeldistance=1.5, shadow=True)
        plt.legend(labels)
        plt.tight_layout()

        img = io.BytesIO()
        plt.savefig(img, format='png')
        img.seek(0)
        graph_url = base64.b64encode(img.getvalue()).decode()
        graph = 'data:image/png;base64,{}'.format(graph_url)

        nama = input['Name']
        sex = input['inlineRadioOptions']
        umur = input['Age']
        tinggi = input['Height']
        bobot = input['Weight']
        pekerjaan = input['Job']
        pelin = input['PI']
        pelti = input['PT']
        lumlor = input['LLA']
        sacslo = input['SS']
        pelrad = input['PR']
        degspo = input['DS']

        cur = mysql.connection.cursor()
        query = ("INSERT INTO record(Name, Gender, Age, Height, Weight, Job, Pelvic_Incidence, Pelvic_Tilt, Lumbar_Lordosis, Sacral_Slope, Pelvic_Radius, Degree_Spondylolisthesis, Class) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
        vals = [(nama, sex, umur, tinggi, bobot, pekerjaan, pelin, pelti, lumlor, sacslo, pelrad, degspo, prediksinya)]
        cur.executemany(query, vals)
        mysql.connection.commit()
        cur.close()
               
        return render_template('result.html', data=input, pred=prediksi, graph=graph)
    
# @app.route('/record', methods = ['POST','GET'])
# def record():
#     if request.method == "POST":
#         details = request.form
#         nama = details['Name']
#         sex = details['Gender']
#         umur = details['Age']
#         tinggi = details['Height']
#         bobot = details['Weight']
#         pekerjaan = details['Job']
#         pelin = details['PI']
#         pelti = details['PT']
#         lumlor = details['LLA']
#         sacslo = details['SS']
#         pelrad = details['PR']
#         degspo = details['DS']
#         cur = mysql.connection.cursor()
#         cur.execute("INSERT INTO record(Name, Gender, Age, Height, Weight, Job, Pelvic_Incidence, Pelvic_Tilt, Lumbar_Lordosis, Sacral_Slope, Pelvic_Radius, Degree_Spondylolisthesis) VALUES(%s %s %d %d %f %s %f %f %f %f %f %f)", (nama, sex, umur, tinggi, bobot, pekerjaan, pelin, pelti, lumlor, sacslo, pelrad, degspo))
#         mysql.connection.commit()
#         cur.close()
#         return 'Success Record'

if __name__ == '__main__':
    model = joblib.load('model_svc')
    fit_norm = joblib.load('fit_ss')
    app.run(debug=True, port=2070)
