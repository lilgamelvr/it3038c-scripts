Step 1: Install NumPy

Do it using 

```python
pip install numpy
```
In your Command Line. (Virtualenv is optional)

Step 2: Make an array

Run this code.

```python
import numpy as np
arr = np.array([[1, 2, 3],
                [4, 5, 6]])
```
The array can be changed.

Step 3: Run print commands

To show the array and a modified version of it run

```python
print('array: ', arr)
print('array plus 1:', arr + 1)
```

Step 4: Invoke slicing method

Invoke Array slicing method with

```python
sliced_arr = arr[:2, ::2]
```
Step 5: Print sliced array

After invoking and labeling the sliced array, print results using

```python
print("Array with alternate columns(0 and 2): ", sliced_arr)
```

Disable virtualenv if you enabled it and you are done.


