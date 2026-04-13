import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("student_performance_mini.csv")
print("===== FIRST 5 ROWS =====")
print(df.head())
print("\n===== DATASET INFO =====")
print(df.info())
print("\n===== MISSING VALUES =====")
print(df.isnull().sum())

# 1. BAR CHART

plt.figure(figsize=(12, 6))
plt.bar(df["name"], df["cgpa"])
plt.xlabel("Student Name")
plt.ylabel("CGPA")
plt.title("Bar Chart: Student Name vs CGPA")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()


# 2. STAIR CHART

plt.figure(figsize=(12, 6))
plt.step(df["student_id"], df["risk_score"], where='mid')
plt.xlabel("Student ID")
plt.ylabel("Risk Score")
plt.title("Stair Chart: Student ID vs Risk Score")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()


# 3. LINE CHART

plt.figure(figsize=(12, 6))
plt.plot(df["student_id"], df["attendance_percentage"], marker='o')
plt.xlabel("Student ID")
plt.ylabel("Attendance Percentage")
plt.title("Line Chart: Student ID vs Attendance Percentage")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()


# 4. PIE CHART

placement_counts = df["placement_readiness"].value_counts()

plt.figure(figsize=(7, 7))
plt.pie(placement_counts, labels=placement_counts.index, autopct='%1.1f%%', startangle=90)
plt.title("Pie Chart: Placement Readiness Distribution")
plt.show()


# 5. HISTOGRAM

plt.figure(figsize=(10, 6))
plt.hist(df["cgpa"], bins=10, edgecolor='black')
plt.xlabel("CGPA")
plt.ylabel("Frequency")
plt.title("Histogram: CGPA Distribution")
plt.tight_layout()
plt.grid(True)
plt.show()


# 6. MISSING VARIABLES

print("\n===== MISSING VALUES IN EACH COLUMN =====")
print(df.isnull().sum())

plt.figure(figsize=(10, 6))
df.isnull().sum().plot(kind='bar')
plt.xlabel("Columns")
plt.ylabel("Missing Values Count")
plt.title("Missing Values in Dataset")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# 7. OUTLIERS Boxplot for CGPA

plt.figure(figsize=(8, 6))
sns.boxplot(y=df["cgpa"])
plt.title("Boxplot: Outliers in CGPA")
plt.ylabel("CGPA")
plt.tight_layout()
plt.show()


plt.figure(figsize=(8, 6))
sns.boxplot(y=df["risk_score"])
plt.title("Boxplot: Outliers in Risk Score")
plt.ylabel("Risk Score")
plt.tight_layout()
plt.show()

print("\n===== DONE: All graphs plotted successfully =====")