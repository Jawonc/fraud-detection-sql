# 📊 Fraud Detection Data Dictionary

## 🏛️ Database Structure
| Table Name  | Description |
|------------|-------------|
| transactions | Contains all financial transactions with fraud indicators |
| customers   | Stores customer details linked to transactions |
| merchants   | Information on merchants where transactions occur |
| fraud_cases | Historical fraud cases for training fraud detection models |

## 🗄️ Column Details
| Table | Column | Data Type | Description |
|--------|---------|----------|-------------|
| transactions | transaction_id | INT | Unique identifier for each transaction |
| transactions | customer_id | INT | Foreign key linking to customers table |
| transactions | amount | DECIMAL | Amount spent in the transaction |
| transactions | transaction_date | DATE | Date of transaction |
| transactions | is_fraud | BOOLEAN | Indicates whether the transaction was fraudulent |
| customers | customer_id | INT | Unique ID of a customer |
| customers | name | VARCHAR | Name of the customer |
| merchants | merchant_id | INT | Unique ID for a merchant |
| merchants | merchant_name | VARCHAR | Name of the merchant |
| fraud_cases | case_id | INT | Unique ID for fraud case |
| fraud_cases | transaction_id | INT | Foreign key linking to transactions |
| fraud_cases | fraud_reason | TEXT | Explanation of the fraud detection reason |
