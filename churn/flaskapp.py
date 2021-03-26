from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open("D:/INSAID/LMS/Model Deployments/Module 4 - Model Deployment using Flask/HandsOn/randomforest.pkl","rb"))

@app.route('/')
def main():
    return render_template('home.html')
    
@app.route('/predict', methods=['POST'])
def home():
    tenure = request.form['a']
    PS = request.form['b']
    C = request.form['c']
    PB = request.form['d']
    PM = request.form['e']
    MC = request.form['f']
    array = np.array([[tenure, PS, C, PB, PM, MC]])
    pred = model.predict(array)
    return render_template("result.html", data=pred)
    

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)