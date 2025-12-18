import pandas as pd

# print(type(pd))

# =========== SERIESSS =========


# ages = pd.Series([18, 21, 25, 30], index=['Alice', 'Bob', 'Charlie', 'David'])
# # print(ages)

# print(ages.index[0])
# print(ages["Alice"])
# print(ages[1])        

# ================= DataFrame

# data = {
#     'Name': ['Alice', 'Bob', 'Charlie', 'David'],
#     'Age': [18,21,25,26],
#     'City': ['NY', 'LA', 'Chicago', 'Houston']
# }

# df = pd.DataFrame(data)
# print(df)


# print(df['Name'])
# print(df[['Name','Age']])
# print(df.iloc[3,2])

# print(df["Age"]>20)
# df['Senior'] = df['Age'] > 24

# print(df)


# Q1. Create a Series of 5 fruits and print their labels and values.

# fruits = pd.Series(["Apple", "Banana"], index = [1,2])
# print(fruits)

# print("Lables: ", fruits.index.tolist())
# print("Values: ", fruits.values.tolist())

# Q2. Create a DataFrame with 3 columns (Name, Age, City) and 5 rows.

data = {
    'Name':['Alice',"Bob", "Aleyna", "Kathryn", "Lia"],
    'Age': [22,34,23,54,12],
    'City': ['DC', 'NY', "NJ", "LHE", 'ISL']
}

dataFrame = pd.DataFrame(data)
print(dataFrame)

# First 2 rows
print("First 2 rows:")
# print(dataFrame.head(2))
print(dataFrame.iloc[:2])


# Last 2 rows
print("\nLast 2 rows:")
# print(dataFrame.tail(2))
print(dataFrame.iloc[-2:])


# Q4. Filter the DataFrame to show only people with Age > 25.

print("AGE GREATER 25 ==============")
# print(dataFrame["Age"] > 25)
print(dataFrame[dataFrame["Age"] > 25])


# Q5. Add a new column “IsAdult” which is True if Age ≥ 18 else False.


print("ADULT ==========")

dataFrame["IsAdult"] = dataFrame['Age'] > 18
print(dataFrame)

# Q6. Save the DataFrame to a CSV file “people.csv”. Then read it back and print.

print("Saving and Reading CSV ============")

dataFrame.to_csv("people.csv", index=False)  # index=False to avoid writing row numbers

dataFrame_read = pd.read_csv("people.csv")
print(dataFrame_read)