## Numpy Practice

# > import numpy

import numpy as np

# > convert a list into a numpy array

lst = [1, 2, 3, 4, 5]
arr = np.array(lst)
type(arr)

# > convert multiple list into a multidimensional array

list1 = [1, 2, 3, 4, 5]
list2 = [2, 3, 4, 5, 6]
list3 = [3, 4, 5, 6, 7]
arr1 = np.array([list1, list2, list3])
arr1

# > shape -> It is used to find the size of output or a array

arr1.shape
arr

# > It is used to print the output

print(arr[3])

# > This is indexing in array

arr[:]
arr[1:3]
arr[::]

# > It is used to take step in continuous series

arr[::3]
arr1
arr1[:, 1]
arr1
arr1[1:, 1:3]
arr1[1:, 3:5].shape
arr[arr < 2]
arr1

# > To this function we can reshape the rows and columns and we can reshape only in multiple of row and column is equal to total elements.

arr1.reshape(5, 3)
arr1.reshape(1, 15)

# > This fuction is used to take elements in the range

np.arange(1, 20, 2)
np.arange(1, 20, 2).reshape(2, 5)

# > We can do all airthmetic operation on this array

arr * arr
arr + arr

# > This function is used to define a array of zeroes

np.zeros((5, 3))

# > This function is used to define a array of ones

np.ones((5, 3))

# > These functions is used to initialize the random elements

np.random.randint(10, 50, 4).reshape(2, 2)
np.random.randn(5, 6)
np.random.random_sample((5, 6))
arr1

# > It is used to make a array of same element

np.full((2, 2), 7)

# > It is used to make an identitical array

np.eye(4)

# > It is used to find total no. of elements in array

arr.size

# > It is used to what type of array is this 1d 2d 3d

arr.ndim
arr1.ndim

# > It is used to find the type of elements in the array

arr.dtype

# > It is used to change the data type of existing elements of array

arr.astype("float")
arr.astype("str")

# > The following aggregration functions are used to calculate some results

print(np.sum(arr))
print(arr.sum())
print(arr.min())
print(arr.max())
print(arr.mean())
print(arr.std())
print(arr.var())
print(arr.max())
arr[[0, 3]]
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
arr_2d

# > convert multidimensional array into 1d array -> view - its affect original array

print(arr_2d.ravel())

# > convert multidimensional array into 1d array -> copy - its doesn't affect original array

print(arr_2d.flatten())

# > insert a element in the array but ye dusre array me store krega existing array me changes nhi krega

arr2 = np.insert(arr, 2, 100)
arr2
arr2d = np.array([[1, 2], [3, 4]])
arr2d

# > insert a row or column in an 2d array

arr2dnew = np.insert(arr2d, 1, [5, 6], axis=1)
print(arr2dnew)
arr2dnew = np.insert(arr2d, 1, [5, 6], axis=0)
print(arr2dnew)
arr2dnew = np.insert(arr2d, 1, [5, 6], axis=None)
print(arr2dnew)

# > append - add elements in the end of array

new_arr = np.append(arr, [9, 8])
print(new_arr)

# > concatenate - 2 or 2 se jyada array ko jodna

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
temp = np.concatenate((arr1, arr2))
temp

# > delete - remove element in the array

new_arr = np.delete(arr1, 1)
print(new_arr)

# > 2d array me kaise delete kre   --- axis = 0 means row  && axis = 1 means column

arr2d = np.array(([1, 2, 3], [4, 5, 6]))
new_2darr = np.delete(arr2d, 0, axis=0)
print(new_2darr)

# > stacking -- vertically or horizontally -- vstack() is used for vertical stacking and hstack() is used for horizontal stacking

a1 = np.array([1, 2, 3])
a2 = np.array([4, 5, 6])
print(np.vstack((a1, a2)))
print(np.hstack((a1, a2)))

# > splitting -- np.split() -> equally split  && np.hsplit() -> horizontally split  && np.vsplit() -> vertically split

aa1 = np.array([10, 20, 30, 40, 50, 60])
print(np.split(aa1, 2))
aaa1 = np.array(([1, 2, 3, 4], [5, 6, 7, 8]))
print(np.vsplit(aaa1, 2))
print(np.hsplit(aaa1, 2))

# > Broadcasting -- it expand the smaller array into larger array

prices = np.array([100, 200, 300])
discount = 10

new_prices = prices - (prices * discount / 100)
print(new_prices)
a = np.array([100, 200, 300])
print(a * 2)

# > It show error because arrays are not same size

ar = np.array([[1, 2, 3], [4, 5, 6]])
ar2 = np.array([1, 2])
print(ar + ar2)
matrix = np.array([[1, 2, 3], [4, 5, 6]])
vector = np.array([10, 20, 30])
result = vector + matrix
print(result)

# > Vectorization -> array ke elements ke sath operations perform krna  // array pe operations perform krna

a1 = np.array([10, 20, 30])
a2 = np.array([40, 50, 60])
print(a1 + a2)
print(a1 * 3)

# > Handing a missing values

# > isnan() --> this function is used to find out there nan (not a number) is persent or not
arr3 = np.array([1, 2, np.nan, 4, np.nan, 6])
print(np.isnan(arr3))
# > we don't comapre the nan to nan  eg. print(np.nan == np.nan)
# > nan_to_num() - ye missing value ki jghh specific no. daldeta h   by default 0 se krta h change
print(np.nan_to_num(arr3))
print(np.nan_to_num(arr3, nan=69))
# > np.isinf()  --> ye true return krega agr koi element infinity hoga toh
arr4 = np.array([1, 2, np.inf, 4, -np.inf, 6])
print(np.isinf(arr4))
# > infinity value ko kisi finite value se change krna
print(np.nan_to_num(arr4, posinf=100, neginf=200))
