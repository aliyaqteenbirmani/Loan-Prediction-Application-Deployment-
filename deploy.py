from flask import Flask, render_template, request
import pickle


app = Flask(__name__) 
model = pickle.load(open('savedmodel.sav', 'rb'))


@app.route('/')
def home():
    result = ' '
    return render_template('index.html',**locals())



@app.route('/predict',methods=['POST','GET'])
def predict():
    Gender	= float(request.form['Gender'])
    Married	= float(request.form['Married'])
    Dependents = float(request.form['Dependents'])
    Education = float(request.form['Education'])
    Self_Employed = float(request.form['Self_Employed'])
    ApplicantIncome	= float(request.form['ApplicantIncome'])
    CoapplicantIncome = float(request.form['CoapplicantIncome'])
    LoanAmount = float(request.form['LoanAmount'])
    Loan_Amount_Term = float(request.form['Loan_Amount_Term'])
    Credit_History = float(request.form['Credit_History'])
    Property_Area = float(request.form['Property_Area'])
    result = model.predict([[Gender, Married, Dependents,	Education,	Self_Employed,	ApplicantIncome,	CoapplicantIncome,	LoanAmount,	Loan_Amount_Term,	Credit_History,	Property_Area]])[0]
    return render_template('index.html',**locals())





if __name__ == '__main__':
    app.run()