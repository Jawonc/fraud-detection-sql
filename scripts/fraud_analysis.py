import pandas as pd

# Load dataset
df = pd.read_csv("datasets/fraud_data.csv")

# Detect high-value transactions
high_value = df[df["amount"] > df["amount"].mean() * 3]
print("High-value transactions:\n", high_value)

# Detect rapid transactions within 10 minutes
df["transaction_date"] = pd.to_datetime(df["transaction_date"])
df["time_diff"] = df.groupby("user_id")["transaction_date"].diff().dt.total_seconds() / 60
rapid_transactions = df[df["time_diff"] < 10]
print("Rapid transactions detected:\n", rapid_transactions)

# Save results
high_value.to_csv("datasets/high_value_transactions.csv", index=False)
rapid_transactions.to_csv("datasets/rapid_transactions.csv", index=False)

