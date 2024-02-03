from flask import Flask, request
import pickle

app = Flask(__name__) # name of application

with open('classifier.pkl','rb') as f:
    model = pickle.load(f)

# command  -> flask --app app.py run
# base url
    
@app.route('/ping',methods=['GET'])
def ping():
    return "aise hi mja aara hai likh diye code !!"

# gender, married, credit_history , applicant_income, loan_amount 
@app.route('/predict',methods=['POST'])
def predict():
    """
    returns the loan approved or not
    
    """
    loan_request = request.get_json()

    if(loan_request['gender']=='Male'):
        gender=0
    else:
        gender = 1
    
    if(loan_request['married']=='Unmarried'):
        marital_status = 0
    else:
        marital_status = 1
    
    if(loan_request['credit_history']=='Unclear Debts'):
        credit_history = 0
    else:
        credit_history = 1
    
    applicant_income = loan_request['applicant_income']
    loan_amount = loan_request['loan_amount']

    result  = model.predict([[gender, marital_status, credit_history , applicant_income, loan_amount]])
    
    if(result == 0):
        pred = 'rejected'
    else:
        pred = 'approved'
    return {"loan_approval_status : ":pred}


# {
# "gender" : "Male", 
# "married":"Married",
# "applicant_income":"79533",
# "loan_amount" : "200000",
# "credit_history":"Cleared Debts" 
# }