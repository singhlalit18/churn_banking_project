import pandas as pd

df = pd.read_csv(r"C:\Users\hp\Desktop\churn_banking_project\data\European_Bank.csv")

# KPI 1: Overall Churn Rate
overall_churn = (
    df["Exited"].mean()
    *100
)
print(
    "Overall Churn:",
    round(overall_churn,2),
    "%"
)

# KPI 2: Segment Churn Rate
df["Age_Group"] = pd.cut(
    df["Age"],
    bins=[18, 30, 40, 50, 60, 100],
    labels=["18-30", "31-40", "41-50", "51-60", "60+"]
)
segment_churn = (
    df.groupby("Age_Group")["Exited"]
      .mean()
      * 100
)

print(segment_churn)

# KPI 3: Geographic Risk Index
geo_risk = (
    df.groupby("Geography")
    ["Exited"]
    .mean()
    *100
)
print(geo_risk)


# KPI 4: Engagement Drop Indicator
engagement = (
    df.groupby("IsActiveMember")
    ["Exited"]
    .mean()
    *100
)

print(engagement)