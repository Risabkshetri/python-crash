# from matplotlib import pyplot as plt

# x = [1,2,3,4,5]
# y = [90,100,60,80,50]
# plt.plot(x, y, linewidth=1)
# plt.xlabel("students")
# plt.ylabel("percentage")
# plt.title("Student Marks")
# plt.show()

# y = [35,25,25,15]
# mylabels = ["Apples","Bananas","Cherries","Dates"]
# plt.pie(y, labels = mylabels)
# plt.legend(title ="Four Fruits:")
# plt.show()

# x1 = [4,8,12]
# y1 = [19,11,7]
# x2 = [7,10,12]
# y2 = [8,18,24] 
# plt.scatter(x1, y1, color='b')
# plt.scatter(x2, y2, color='g')
# plt.title('Epic Info')
# plt.ylabel('Y axis')
# plt.xlabel('X axis') 
# plt.show()


# dataframes and series

import pandas as pd
import numpy as np

# arr = np.array([10,20,30,40])
# index = ['a','b','c','d']
# data = pd.Series(arr, index=index)
# print(data)

# data = {
#     "Name":["Rishab", "Bishal", "Aatif"],
#     "age":[19,21,20],
#     "City":["kathmandu", "Butwal", "Delhi"]
# }

# print(pd.DataFrame(data))  


filepath = 'data/mock_data.csv'
print(pd.read_csv(filepath))