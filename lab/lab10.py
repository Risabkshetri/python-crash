## 1. To create series and dataframes
import pandas as pd
data = [1, 2, 3, 4, 5] 

series = pd.Series(data) 
print("Series:\n", series)

df = pd.DataFrame(data) 
print("DataFrame: \n", df)
## 2. python code to perform following operations in dataframes---
# a) indexing b) handling missing data c) analyzing data d) Normalizing data
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

# Creating a DataFrame with missing values
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, np.nan, 22, 32],
    'City': ['New York', 'Los Angeles', 'Chicago', np.nan],
    'Salary': [70000, 80000, 55000, 90000]
}
df = pd.DataFrame(data)

# 1. Indexing - Setting 'Name' as the index
df.set_index('Name', inplace=True)

print("DataFrame with 'Name' as index:\n", df)

# 2. Handling Missing Data - Filling missing values with 'Unknown' for 'City' and the mean for 'Age'
df['City'].fillna('Unknown', inplace=True)
df['Age'].fillna(df['Age'].mean(), inplace=True)

print("\nDataFrame after handling missing values:\n", df)

# 3. Analyzing Data - Descriptive statistics and grouping by 'Age'
print("\nDescriptive statistics:\n", df.describe())

grouped = df.groupby('Age').mean()
print("\nGrouped by 'Age' with mean values:\n", grouped)

# 4. Normalizing Data - Normalizing 'Age' and 'Salary' columns
scaler = MinMaxScaler()
df[['Age', 'Salary']] = scaler.fit_transform(df[['Age', 'Salary']])

print("\nNormalized DataFrame:\n", df)


# 3. Plot different types of Graph using matplotlib
import matplotlib.pyplot as plt
#line plot
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

plt.plot(x, y, marker='o')
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Line Plot")
plt.show()
# scatter plot
x = [5, 7, 8, 7, 2, 17, 2, 9]
y = [99, 86, 87, 88, 100, 86, 103, 87]

plt.scatter(x, y, color='blue')
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Scatter Plot")
plt.show()

# Bar plot
categories = ['A', 'B', 'C', 'D']
values = [5, 7, 3, 8]

plt.bar(categories, values, color='green')
plt.xlabel("Categories")
plt.ylabel("Values")
plt.title("Bar Plot")
plt.show()
# histogram
import numpy as np

data = np.random.randn(1000)
plt.hist(data, bins=30, color='purple', edgecolor='black')
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Histogram")
plt.show()

# pie chart
labels = ['Category A', 'Category B', 'Category C', 'Category D']
sizes = [15, 30, 45, 10]
colors = ['gold', 'lightcoral', 'lightskyblue', 'lightgreen']
explode = (0, 0.1, 0, 0)  # "explode" the 2nd slice (i.e. 'Category B')

plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.title("Pie Chart")
plt.show()

#Box plot
data = [np.random.normal(0, std, 100) for std in range(1, 4)]

plt.boxplot(data, vert=True, patch_artist=True)
plt.xlabel("Dataset")
plt.ylabel("Values")
plt.title("Box Plot")
plt.show()

# Hitman plot
import seaborn as sns
import numpy as np

data = np.random.rand(10, 10)
sns.heatmap(data, annot=True, cmap="YlGnBu")
plt.title("Heatmap")
plt.show()

#3D plot
from mpl_toolkits.mplot3d import Axes3D

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]
z = [1, 4, 9, 16, 25]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z)
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
plt.title("3D Plot")
plt.show()


#Violin plot
import seaborn as sns

data = [np.random.normal(0, std, 100) for std in range(1, 4)]
sns.violinplot(data=data)
plt.xlabel("Dataset")
plt.ylabel("Values")
plt.title("Violin Plot")
plt.show()

# Area plot
x = range(1, 6)
y = [1, 4, 6, 8, 10]

plt.fill_between(x, y, color="skyblue", alpha=0.4)
plt.plot(x, y, color="Slateblue", alpha=0.6)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Area Plot")
plt.show()



## 4. python script read an image from file and display it
#Image-Viz project

# 5. python script to make calculator using Tkinter