import uvicorn
from fastapi import FastAPI
from BankNotes import BankNote
import pandas as pd
import numpy as np
import pickle
import warnings
warnings.filterwarnings('ignore')

app = FastAPI()
pickle_in = open('classify.pkl',"rb")
classify = pickle.load(pickle_in)

@app.get('/')
def index():
    return {'message': 'Hello GK'}

@app.post('/predict')
def predict_banknote(data:BankNote):
    data = data.dict()
    print(data)
    variance = data['variance']
    skewness = data['skewness']
    curtosis = data['curtosis']
    entropy = data['entropy']
    
    print(classify.predict([[variance,skewness,curtosis,entropy]]))
    prediction = classify.predict([[variance,skewness,curtosis,entropy]])
    if prediction <0.5:
        prediction = "Fake Note"
    else:
        prediction = "Good Note"
        
    return {
        
        'prediction': prediction
    }
    
if __name__ == '__main__':
    uvicorn.run(app,host='127.0.0.1', port = 8000)    
    
    