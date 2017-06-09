import numpy as np

data1 = [6,7.5,8,0,1]

arr1 = np.array(data1)

print arr1
print arr1.shape
print arr1.dtype

data2 = [[1,2,3,4],[5,6,7,8]]

arr2 = np.array(data2)

print arr2
print arr2.ndim
print arr2.shape



print np.array(np.zeros(10))

print np.array(np.arange(15))


num_strings = np.array(['1.23','-90','42'],dtype=np.string_)
print num_strings.astype(float)


empty_uint32 = np.empty(8,dtype='u4')

print empty_uint32

#99