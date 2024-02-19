import pandas as pd

def test_yval():    
    df = pd.read_csv('BankNote_Authentication.csv')
    y = df['class']
    print("value of y =", y[0])
    assert y[0] == 0