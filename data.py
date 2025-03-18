import pandas as pd

# Sample dataset
def get_sample_data():
    data = [
        {'transaction_id': 'T001', 'amount': 100, 'sender_account': 'S1', 'receiver_account': 'R1', 'time': '2025-03-18 10:00:00', 'country': 'US'},
        {'transaction_id': 'T002', 'amount': 200, 'sender_account': 'S1', 'receiver_account': 'R2', 'time': '2025-03-18 10:30:00', 'country': 'US'},
        {'transaction_id': 'T003', 'amount': 5000, 'sender_account': 'S2', 'receiver_account': 'R3', 'time': '2025-03-18 10:45:00', 'country': 'IN'},
        {'transaction_id': 'T004', 'amount': 1000, 'sender_account': 'S3', 'receiver_account': 'R4', 'time': '2025-03-18 11:00:00', 'country': 'US'},
        {'transaction_id': 'T005', 'amount': 25000, 'sender_account': 'S4', 'receiver_account': 'R5', 'time': '2025-03-18 11:30:00', 'country': 'NG'},
    ]
    
    return pd.DataFrame(data)
