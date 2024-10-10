import numpy as np

arr = np.array(np.random.randint(-100,101,(2,3)))
print(arr)
b = arr[(arr > 0) & (arr == np.floor(arr))]

print(b)
