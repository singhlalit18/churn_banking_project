import pandas as pd

df = pd.read_csv(
    r"C:\Users\hp\Desktop\churn_banking_project\data\European_Bank.csv"
)


# Remove extra spaces from column names
df.columns = df.columns.str.strip()

# Drop unnecessary columns
df.drop(
    columns=["RowNumber", "CustomerId", "Surname"],
    inplace=True,
    errors="ignore"
)

print(df.head())
print(df.columns.tolist())


# Validate Binary Columns
binary_cols = [
    "HasCrCard",
    "IsActiveMember",
    "Exited"
]

for col in binary_cols:
    print(col)
    print(df[col].value_counts())


# Create Age Groups
df["Age_Group"] = pd.cut(
    df["Age"],
    bins=[0,30,45,60,100],
    labels=[
        "Under 30",
        "30-45",
        "46-60",
        "60+"
    ]
)

print(df["Age_Group"].value_counts())


# Create Credit Score Bands
df["Credit_Band"] = pd.cut(
    df["CreditScore"],
    bins=[0,580,700,850],
    labels=[
        "Low",
        "Medium",
        "High"
    ]
)
print(df.columns)
print(df["CreditScore"].dtype)
print(df["CreditScore"].min(), df["CreditScore"].max())


# Create Balance Segments
df["Balance_Segment"] = pd.cut(
    df["Balance"],
    bins=[
        -1,
        0,
        100000,
        df["Balance"].max()
    ],
    labels=[
        "Zero Balance",
        "Low Balance",
        "High Balance"
    ]
)

print(df.head())


# Save Clean Dataset
df.to_csv(
    r"C:\Users\hp\Desktop\churn_banking_project\data\clean_churn.csv",
    index=False
)