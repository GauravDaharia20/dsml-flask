import pytest

from app import app 

@pytest.fixture   # Creates object to test our api
def client():
    return app.test_client()

def test_ping(client):
    response = client.get('/ping')
    assert response.status_code == 200
    assert response.json == {'message':'aise hi mja aara hai likh diye code !!'}

def test_predict(client):
    test_data = {
    "gender" : "Male", 
    "married":"Married",
    "applicant_income":79533,
    "loan_amount" : 200000,
    "credit_history":"Cleared Debts" 
    }
    response = client.post('/predict',json=test_data)

    assert response.status_code == 200
    assert response.json == {"loan_approval_status : ":'rejected'}
