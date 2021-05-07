import matplotlib.pyplot as plt
import numpy as np


def plotingGraph():
    x = [2, 3, 4]
    y = [5, 8, 1]
    plt.plot(x, y)
    plt.show()


def styling():
    x = [9, 10, 2]
    y = [2, 6, 8]
    plt.plot(x, y, "g", label="line one", linewidth=5)
    plt.plot(y, x, "y", label="line two", linewidth=5)
    plt.title("Info")
    plt.xlabel("x -axis")
    plt.ylabel("y -axis")
    plt.legend()
    plt.show()


def barplot():
    x = [9, 10, 2]
    y = [2, 6, 8]
    plt.bar(x, y, width=0.5, label="barChart")
    plt.title("Info")
    plt.xlabel("x -axis")
    plt.ylabel("y -axis")
    plt.legend()
    plt.show()


def histogram():
    x = [9, 10, 2]
    y = [2, 6, 8]
    plt.bar(x, y, width=0.5, label="hisChart")
    plt.title("Info")
    plt.xlabel("x -axis")
    plt.ylabel("y -axis")
    plt.legend()
    plt.show()


def scater():
    x = [9, 10, 2]
    y = [2, 6, 8]
    plt.scatter(x, y, label="scatter")
    plt.title("Info")
    plt.xlabel("x -axis")
    plt.ylabel("y -axis")
    plt.legend()
    plt.show()

def stackplotting():
    x = [9, 10, 2]
    y = [2, 6, 8]
    x1 = [7, 50, 1]
    y2 = [9, 5, 8]
    plt.stackplot(x, y)
    plt.title("Info")
    plt.xlabel("x -axis")
    plt.ylabel("y -axis")
    plt.legend()
    plt.show()

def pieplotting():
    ratio = [1, 2, 3]
    plt.pie(ratio, explode=[0, 1, 0], labels=["A", "B", "C"], startangle=90, autopct="%1.1f%%")
    plt.show()

def subplot():
    firstborn1 = np.arange(1, 10, 1)
    firstborn2 = np.arange(2, 20, 2)
    print(firstborn1)
    print(firstborn2)
    secondborn1 = np.arange(2, 20, 2)
    secondborn2 = np.arange(1, 10, 1)
    print(secondborn1)
    print(secondborn2)
    # create a subplot 2 vertical, 1 horizontal and put the plot at the first position
    plt.subplot(211)
    plt.plot(firstborn1, firstborn2)
    # create a subplot 2 vertical , 1 horizontal and put the plot at the second position
    plt.subplot(212)
    plt.plot(firstborn1, firstborn2)
    plt.show()

    # create a subplot 1 vertical, 2 horizontal and put the plot at the first position
    plt.subplot(121)
    plt.plot(firstborn1, firstborn2)
    # create a subplot 1 vertical for all, 2 horizontal for this plot and put the plot at the second
    plt.subplot(122)
    plt.plot(firstborn1, firstborn2)
    plt.show()

if __name__ == '__main__':
    # plotingGraph()
    # styling()
    # barplot()
    # histogram()
    # scater()
    # stackplotting()
    # pieplotting()
    subplot()
