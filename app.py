from flask import Flask, request, jsonify
from model import detect_suspicious_transaction
from data import get_sample_data
from utils import preprocess_transaction

app = Flask(__name__)

@app.route('/api/transaction', methods=['POST'])
def transaction():

    transaction_data = request.get_json()

    preprocessed_data = preprocess_transaction(transaction_data)

    is_suspicious, reason = detect_suspicious_transaction(preprocessed_data)

    return jsonify({
        'transaction_id': transaction_data['transaction_id'],
        'status': 'Suspicious' if is_suspicious else 'Normal',
        'reason': reason
    }), 200

if __name__ == '__main__':
    app.run(debug=True)
