import numpy as np

data1 = [[6, 7, 8, 10, 1], [2, 3, 4, 5, 7], [1, 2, 3, 4, 5]]
num1 = np.array(data1)
num2 = num1.reshape(5, 3)
print("num2.dtype-----", num2.dtype)
print("num2.shape------", num2.shape)
print("num2.ndim------", num2.ndim)

num2 = np.zeros([2, 6, 3])
print("num2---", num2.ndim)

num3 = np.eye(3)
print("num3---", num3)

num4 = np.random.randint(2, 10, size=[2, 5])
print("num4---", num4)

num5 = [0, 2, 3, 4, 5, 6, 7, 8]
num6 = np.array(num5).reshape(2, 4)
print("num6---", num6)
