import pandas as pd

df = pd.DataFrame([[1,2,3], [4,5,6], [7,8,9], [10,11,12]],
                  columns=["A", "B", "C"],
                  index=["x", "y", "z", 'zz'])

print(df.head(2))
print("---")
print(df.tail(2))
print("---")
print(df.columns)
print("---")
print(df.index)
print("---")
print(df.info())
print("---")
print(df.describe())
print("---")
print(df.nunique())
# df.shape là một tuple, không phải list hay array.
# trả về dòng trước cột sau
print(df.shape)