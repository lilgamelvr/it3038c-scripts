import numpy as np

arr = np.array([[1, 2, 3],
                [4, 5, 6]])

print('array: ', arr)

print('array plus 1:', arr + 1)

sliced_arr = arr[:2, ::2]
print("Array with alternate columns(0 and 2): ", sliced_arr)
