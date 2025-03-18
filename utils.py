import pandas as pd
import numpy as np

def feature_engineering(df):
    df['hour'] = pd.to_datetime(df['time']).dt.hour
    df['amount_log'] = np.log(df['amount'] + 1)  
    return df

def preprocess_transaction(transaction_data):
    df = pd.DataFrame([transaction_data])
    df = feature_engineering(df)
    return df
