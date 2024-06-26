import numpy as np

# 创建数组
arr = np.array([1, 2, 3, 4, 5])
print("Array arr:", arr)

# 创建二维数组
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("\n2D Array arr2d:\n", arr2d)

# 使用 arange 创建等差数列
arr_range = np.arange(10)
print("\nArray using arange:", arr_range)

# 使用 linspace 创建等间隔数列
arr_linspace = np.linspace(0, 10, 11)
print("\nArray using linspace:", arr_linspace)

# 数组的索引和切片
print("\nElement at index 2 of arr:", arr[2])
print("Slice from index 1 to 3 of arr:", arr[1:3])

# 二维数组的索引
print("\nElement at row 1, column 2 of arr2d:", arr2d[1, 2])
print("Row 1 of arr2d:\n", arr2d[1, :])
print("Column 2 of arr2d (using slicing):\n", arr2d[:, 2])

# 数学运算
arr_multiply = arr * 2
print("\nArray arr multiplied by 2:", arr_multiply)

arr_add = arr + arr
print("Array arr added to itself:", arr_add)

# 广播机制
arr_broadcast = arr + np.array([1, 2, 3, 4, 5])
print("\nBroadcasting addition with arr:", arr_broadcast)

# 统计函数
print("\nMinimum value in arr:", np.min(arr))
print("Maximum value in arr2d:", np.max(arr2d))
print("Sum of all elements in arr:", np.sum(arr))
print("Mean of all elements in arr2d:", np.mean(arr2d))


# 矩阵乘法
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
C = np.dot(A, B)
print("\nMatrix multiplication of A and B:\n", C)

# 使用随机数生成器
rand_arr = np.random.rand(3, 3)
print("\nRandom array of shape (3, 3):\n", rand_arr)

# 使用随机整数生成器
rand_int_arr = np.random.randint(0, 10, size=(3, 3))
print("\nRandom integer array of shape (3, 3):\n", rand_int_arr)