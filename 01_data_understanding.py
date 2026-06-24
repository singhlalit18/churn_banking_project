import pandas as pd
import numpy as np

df = pd.read_csv(r"C:\Users\hp\Desktop\churn_banking_project\data\European_Bank.csv")
# Import Libraries & Load Dataset

print(df.head())
print(df.shape)
print(df.info())
print(df.isnull().sum())
print(df.duplicated().sum())
print(df.describe())