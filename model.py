from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
import numpy as np
import pandas as pd
from utils import feature_engineering

from data import get_sample_data

def train_model():
    df = get_sample_data()
    df = feature_engineering(df)

    scaler = StandardScaler()
    df[['amount_log', 'hour']] = scaler.fit_transform(df[['amount_log', 'hour']])

    model = IsolationForest(n_estimators=100, contamination=0.1, random_state=42)
    model.fit(df[['amount_log', 'hour']])

    return model, scaler

def detect_suspicious_transaction(transaction_data):
    model, scaler = train_model()
    transaction_data[['amount_log', 'hour']] = scaler.transform(transaction_data[['amount_log', 'hour']])

    prediction = model.predict(transaction_data[['amount_log', 'hour']])

    if prediction[0] == -1:
        return True, 'Flagged by ML model'
    return False, 'No suspicious activity detected'
