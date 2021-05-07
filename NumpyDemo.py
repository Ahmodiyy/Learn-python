import numpy as np
import matplotlib.pyplot as plt


def numpying():
    arr = np.array([[1, 2, 3],
                   [4, 5, 6]])
    ar = np.array([(1, 2, 3),
                   (4, 5, 6)])
    print("dimension ", arr.ndim)
    print("data type in array ", arr.dtype)
    print("each item size ", arr.itemsize)
    print("size ", arr.size)
    print("row and column ", arr.shape)
    print(arr)
    print(arr.reshape(3, 2))
    print("slicing ", arr[0, 2])
    print("slicing ", arr[0:, 2])
    print("slicing ", arr[0:1, 2])
    print("slicing ", arr[0:2])
    print("min ", arr.min())
    print("max ", arr.max())
    print("sum ", arr.sum())
    # axis 1 rep row and axis 2 rep 0
    print(arr.sum(axis=0))
    print(arr.sum(axis=1))
    print("numpy square root ", np.sqrt(arr))
    print(arr + ar)
    print(arr - ar)
    print(arr / ar)
    print(arr * ar)
    print("vertical stacking of arrays ", np.vstack((arr, ar)))
    print("horizontal stacking of arrays ", np.hstack((arr, ar)))
    print("converte array to single column ", ar.ravel())
    # numpy special function
    x = np.arange(0, 3 * np.pi, 0.1)
    y = np.tan(x)
    plt.plot(x, y)
    plt.show()
    print("exponential ", np.exp(ar))
    print("natural log ", np.log(ar))
    print("log 10", np.log10(ar))
    #  ----
    print(np.random.randn(3, 3))
    print(np.random.randn(10, 2))
    print(type(x))
    print(np.arange(3))
    print(np.arange(3)*2)


if __name__ == '__main__':
    numpying()

