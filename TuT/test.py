# import pandas as pd
# import numpy as np

# data = {
#     'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
#     'Age': [24, 22, 22, 32, 28],
#     'Department': ['HR', 'IT', 'Marketing', 'HR', 'IT'],
#     'Salary': [50000, 60000, 70000, 80000, 90000],
#     'Joining Date': ['2018-01-01', '2019-02-01', '2020-03-01', '2021-04-01', '2022-05-01'],
#     'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
# }

# df = pd.DataFrame(data)

# print('\nName column:\n', df['Name'])

# filtered_df = df[df['Age']  > 25]
# print('\nFiltered DataFrame:\n', filtered_df)

# grouped_df = df.groupby('Department').mean(numeric_only=True)
# print('\nGrouped DataFrame:\n', grouped_df)

# sorted_df = df.sort_values(by='Salary', ascending=False)
# print('\nSorted DataFrame:\n', sorted_df)

# df_drop = df.drop(columns=['Joining Date', 'City'])
# print('\nDataFrame after dropping columns:\n', df_drop)

# from PIL import Image

# img = Image.open('images/example.jpg')
# img.show()

# resized_img = img.resize((299,200))
# print("Resized Image: ", resized_img)

# new_size = (int(img.width * 0.5), int(img.height * 0.4))
# reScaled_img = img.resize(new_size)

a = 20
def chek():
    a = 10
    print(a)

chek()
print(a)