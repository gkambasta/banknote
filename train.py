import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pickle

def run_training():
    df = pd.read_csv('BankNote_Authentication.csv')
    X = df.drop(['class'], axis = 1)
    y = df['class']
    X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = .2, random_state = 0)
    classify = RandomForestClassifier()
    classify.fit(X_train, y_train)
    y_pred = classify.predict(X_test)
    print("Accuracy =", accuracy_score(y_pred,y_test))
    pickle_out = open('classify.pkl', "wb")
    pickle.dump(classify, pickle_out)
    pickle_out.close()

if __name__ == "__main__":
    run_training()