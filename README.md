# Real-Time Anti-Money Laundering (AML) Detection Model

This project implements a real-time Anti-Money Laundering (AML) detection system for financial transactions using a combination of machine learning and rule-based checks.

## Getting Started

These instructions will help you set up and run the project locally.

### Prerequisites

- Python 3.x
- pip (Python package manager)

### Installing Dependencies

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/your-username/aml-detection.git
   cd aml-detection

   ```

2. Create a virtual environment (recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scripts\activate

   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

1. Run the Flask server:

   ```bash
   python app.py

   ```

2. The server will start running at http://127.0.0.1:5000/.

### API Endpoint

The system exposes a POST API to evaluate transactions:

- **Endpoint:** `/api/transaction`
- **Method:** POST

#### Request Body:

````json
{
    "transaction_id": "T001",
    "amount": 100,
    "sender_account": "S1",
    "receiver_account": "R1",
    "time": "2025-03-18 10:00:00",
    "country": "US"
}


### Example cURL Request

```bash
curl -X POST http://127.0.0.1:5000/api/transaction \
-H "Content-Type: application/json" \
-d '{
   "transaction_id": "T006",
   "amount": 12000,
   "sender_account": "S6",
   "receiver_account": "R6",
   "time": "2025-03-18 12:00:00",
  "country": "US"
}'

````
