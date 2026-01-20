import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/student_data.csv", sep=";")

print(df.head())

print("Shape of dataset:", df.shape)
print("\nColumn names:\n", df.columns)
print("\nFirst 5 rows:\n", df.head())
print("\nMissing values:\n", df.isnull().sum())

df["average_score"] = (df["G1"] + df["G2"] + df["G3"]) / 3
print(df["average_score"])

plt.figure()
plt.scatter(df["studytime"], df["G3"])
plt.xlabel("Study Time")
plt.ylabel("Final Grade (G3)")
plt.title("Study Time vs Final Grade")
plt.show()