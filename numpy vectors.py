import numpy as np

a = np.random.rand(5)  # creates wierd metrix shape (5,) don't use this rank one array
# a = a.reshape((5, 1)) this is how to fix that
print(a)

print(a.shape)

print(a.T)
print(np.dot(a, a.T))

a = np.random.randn(5, 1)  # use this for (m x 1) or (1 x m) row or column vector

assert a.shape == (5, 1)  # to make sure that shape is correct

print(a)
print(a.T)
print(np.dot(a, a.T))
# use rand(m, 1) else some wierd bugs happens
