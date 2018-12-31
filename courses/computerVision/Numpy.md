# Numpy [Numeric Python]
### Why we need a numpy over list ?
1. List can hold different data type values.
2. List value can change, add and remove. 
But, If we want to some powerful mathematical operation over collection.
So, We need a <b>numpy</b> Package.

Lets take a example,
```python
#Creating Height List
height = [1.45, 1.67, 1.09]

#Creating Weight List
weight = [65.6, 78.9, 90.09]

#BMI
print (weight / height ** 2)
```
```
Output console
TypeError: unsupported operand types()
```
So, We can do mathematical operation over collection.

## Import numpy
```python
import numpy as np
```

## Convert a List into numpy array
```python
import numpy as np
#Creating Height List
height = [1.45, 1.67, 1.09]
np_height = np.array(height)
```

<b>Note:</b>
Numpy array assume that the list contain only in single data type.

### Example (Add Two List):
```python
#list
python_list = [1, 2, 3]

## Add two list
print (python_list + python_list)
```
```
Console Output:
[1, 2, 3, 1, 2, 3]
```

### Example (Add Two numpy array):
```python
#list
python_list = [1, 2, 3]

numpy_array = np.array(python_list)

## Add two numpy array
print (numpy_array + numpy_array)
```
```
Console Output:
[2, 4, 6]
```
## Types of Array
```python 
import numpy as np
np_height = np.array([1.73, 1.68, 1.71, 1.89, 1.79])
np_weight = np.array([65.4, 59.2, 63.6, 88.4, 68.7])
print (type(np_height))
print (type(np_weight))
```
```
Console Output:
numpy.ndarray
numpy.ndarray  
```

## 2D Numpy Arrays
```python
np_2d = np.array([[1.73, 1.68, 1.71, 1.89, 1.79],
 		[65.4, 59.2, 63.6, 88.4, 68.7]])

print (np_2d)
print (np_2d.shape)

np_2d = np.array([[1.73, 1.68, 1.71, 1.89, 1.79],
 [65.4, 59.2, 63.6, 88.4, "68.7"]])
 ```

```
Output console:
array([[ 1.73, 1.68, 1.71, 1.89, 1.79],
 [ 65.4 , 59.2 , 63.6 , 88.4 , 68.7 ]])

(2, 5)

array([['1.73', '1.68', '1.71', '1.89', '1.79'],
 ['65.4', '59.2', '63.6', '88.4', '68.7']],
 dtype='<U32')
```

## Subsetting
```python
np_2d = np.array([[1.73, 1.68, 1.71, 1.89, 1.79],
 		[65.4, 59.2, 63.6, 88.4, 68.7]])

In [10]: np_2d[0]
Out[10]: array([ 1.73, 1.68, 1.71, 1.89, 1.79])s

In [11]: np_2d[0][2]
Out[11]: 1.71

In [12]: np_2d[0,2]
Out[12]: 1.71

In [13]: np_2d[:,1:3]
Out[13]:
array([[ 1.68, 1.71],
 [ 59.2 , 63.6 ]])

In [14]: np_2d[1,:]
Out[14]: array([ 65.4, 59.2, 63.6, 88.4, 68.7])


```


