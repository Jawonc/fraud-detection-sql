import pandas as pd
import matplotlib.pyplot as plt

# Load the fraud dataset
df = pd.read_csv("datasets/fraud_data.csv")

# Transaction Amount Distribution
plt.figure(figsize=(10,5))
df['transaction_amount'].hist(bins=50, color='blue', alpha=0.7)
plt.xlabel("Transaction Amount")
plt.ylabel("Frequency")
plt.title("Distribution of Transaction Amounts in Fraud Data")

# Save the graph
plt.savefig("datasets/fraud_amount_distribution.png")
plt.show()
