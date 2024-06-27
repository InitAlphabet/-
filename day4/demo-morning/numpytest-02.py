# 1
import numpy as np

num1 = np.zeros((2, 4))
print(num1)
num2 = np.array(num1)
# num2[2,4]=[1,1]

print(num2)

# 2
import numpy as np

num1 = np.random.randint(10, 50, size=10)

num2 = np.array(num1)
print(num2)

num3 = np.linspace(10, 49, 10)
num4 = np.array(num3)
print(num4)

num5 = np.arange(10, 50)
num6 = np.array(num5)
print(num6)

# 3
num3 = num2[::-1]
print(num3)

# 4
num1 = np.random.random(size=(10, 10))
num2 = np.array(num1)
# print(num2)
num3 = num2.max()
num4 = num2.min()
print(num3, num4)

# 5
num1 = np.zeros((10, 10))
print(num1)
num1[[0, 9]] = 1
num1[:, [0, 9]] = 1

print(num1)
num2 = np.array(num1)

# 6
num1 = [[0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4]]
num1 = [0, 1, 2, 3, 4]
num2 = np.array(num1 * 5)
num3 = num2.reshape(5, 5)
print(num3)

# 7
num1 = np.linspace(0, 1, 12)
print(num1)

# 8
num1 = np.random.random(10)
print(num1)
print(num1.argsort())
num2 = np.sort(num1)
print(num2)

# 9
num1 = np.random.randint(0, 10, size=10)
print(num1)
index_max = num1.argmax()
print(index_max)
# print(num1)
num1[index_max] = 0
print(num1)

# 10
num1 = np.random.randint(0, 10, size=(5, 5))
print(num1)
# num1[:,2]
num2 = np.argsort(num1[:, 2])
print(num2)
