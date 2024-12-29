# write a program to show the concept of destructor in python

# class listHandler:
#     def __init__(self):
#         self.list = [1, 2, 3, 4, 5]
#         print("List created")

#     def __del__(self):
#         print("Destructor called, list deleted")

# myList = listHandler()
# del myList

class listHandler:
    def __init__(self):
        self.list = [1,2,3,4,5]
        print("list created.")
    
    def __del__(self):
        print("list deleted, Destructor called!")

mylist = listHandler()
del mylist


# program to demonstrate the use of method overloading in python

class Calculator:
    def add(self, a, b=10):
        return a+b
    
calc = Calculator()
print("sum = ", calc.add(20))
print("sum = ", calc.add(10.5, 20.5))


# write a program in numpy to resize an image
import numpy as np

arr = np.random.randint(0, 255, (200, 200,3))
resized_arr = np.resize(arr, (100, 100, 3))
print("Original array shape: ", arr.shape)
print("Resized array shape: ", resized_arr.shape)


# # write a program to convert the particular image to grayscale image
# import cv2
# image = cv2.imread("image.jpg")
# gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# cv2.imwrite("gray_image.jpg", gray_image)


# write a program in numpy to add two matrices
import numpy as np

arr1 = np.array([[1,2], [3,4]])
arr2 = np.array([[5,6], [7,8]])
arr3 = np.add(arr1, arr2)
print("Sum: \n", arr3)


# write a program in numpy to multiply two matrices
arr1 = np.array([[1,2], [3,4]])
arr2 = np.array([[5,6], [7,8]])
arr3 = np.dot(arr1, arr2)
print("Multiplication: \n", arr3)


# write a program in numpy to inverse of a matrice.
arr = np.array([[1,2], [3,4]])
arr_inv = np.linalg.inv(arr)
print("Inverse: \n", arr_inv)


# write a program in numpy to implement linear search.

arr = np.array([1,2,3,4,5])
target = 3
for i in range(len(arr)):
    if arr[i] == arr[target]:
        print("Element found at index: ", i)
        break
else:
    print("Element not found")


