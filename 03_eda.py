import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\hp\Desktop\churn_banking_project\data\European_Bank.csv")

#Overall Churn Rate
churn_rate = df["Exited"].mean() * 100

print(
    "Overall Churn Rate:",
    round(churn_rate,2),
    "%"
)

#Churn by Country
sns.countplot(
    x="Geography",
    hue="Exited",
    data=df
)

plt.title("Churn by Country")
plt.show()

# Churn by Gender
sns.countplot(
    x="Gender",
    hue="Exited",
    data=df
)

plt.title("Churn by Gender")
plt.show()

# Age vs Churn
sns.boxplot(
    x="Exited",
    y="Age",
    data=df
)

plt.title("Age Distribution by Churn")
plt.show()

# Churn by Tenure
sns.countplot(
    x="Tenure",
    hue="Exited",
    data=df
)

plt.title("Tenure vs Churn")
plt.show()

# Churn by Products
sns.countplot(
    x="NumOfProducts",
    hue="Exited",
    data=df
)

plt.title("Products vs Churn")
plt.show()

# High Value Customer Analysis
high_value = df[df["Balance"] > 100000]

print(
    high_value["Exited"]
    .value_counts(normalize=True)
    *100
)