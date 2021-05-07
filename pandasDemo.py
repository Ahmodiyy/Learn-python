import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

d = pd.date_range("20200301", periods=10)
df = pd.DataFrame(np.random.randn(10, 4), index=d, columns=["A", "B", "C", "D"])

def seriesAndDataframe():
    s = pd.Series([1, 2, 3, 4, np.nan])
    print(s)
    d = pd.date_range("20200301", periods=10)
    print(d)
    df = pd.DataFrame(np.random.randn(10, 4), index=d, columns=["A", "B", "C", "D"])
    print(df)
    df2 = pd.DataFrame({"A": 101, "B": 102}, d)
    print(df2)


def viewData():
    d = pd.date_range("20200301", periods=10)
    df = pd.DataFrame(np.random.randn(10, 4), index=d, columns=["A", "B", "C", "D"])
    print(df)
    print(df.head())
    print(df.tail())
    print("describe ", df.describe())
    print(df.index)
    print(df.columns)
    print(df.sort_index(axis=0, ascending=True))
    print(df.sort_values(by="C"))
    print("access row and column with label")
    print(d[0])
    print("location ", df.loc[d[0]])
    print("specific rows ", df.loc["20200301":"20200304", ["A", "B"]])
    print("get val using position ", df.iloc[0])
    print("get val using position ", df.iloc[0:5])
    print("boolean indexing")
    print(df[df["A"] > 0])

def handlingMissingData():
    df2 = df.reindex(index=d[0:4], columns=list(df.columns) + ["E"])
    df2.loc[d[0]:d[1], "E"] = 1
    print(df2)
    print(df2.isnull())
    print(df2.isnull().count())
    print(df2.fillna(value=2))
    print(pd.isna(df2))

def pandasOperation():
    print(df)
    print(df.mean())
    print(df.mean(0))
    s = pd.Series([1, 2, 3, np.nan, 4, 5, 6, 7, 8, 9], d).shift(periods=2)
    print("s ", s)
    print(df.sub(s, axis= "index"))
    print(df.apply(lambda x: x.max() - x.min()))
    dff = pd.DataFrame(np.random.randn(10, 4))
    dff2 = [dff[:3], dff[4:7], dff[7:]]
    print(dff)
    print(dff2)
    daf = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
    daf2 = pd.DataFrame({"A": [1, 8, 9], "D": [10, 11, 12]})
    print(daf)
    print(daf2)
    print("merge")
    print(daf.merge(daf2))
    la = [["a", 12, 12], [None, 12.3, 33.], ["b", 12.3, 123], ["a", 1, 1]]
    print(la)
    dfa = pd.DataFrame(la, columns=["a", "b", "c"])
    print(dfa)
    print(dfa.groupby("a").sum())

def stackAndPivot():
    lists = list(zip([1, 2, 3, 4, 5, 17, 18, 19], [11, 12, 13, 6, 7, 8, 9, 10]))
    print(lists)
    index = pd.MultiIndex.from_tuples(lists, names=["First", "Second"])
    print(index)
    dataframe = pd.DataFrame(np.random.randn(8, 2), index=index, columns=["A", "B"])
    dataframe2 = dataframe[:4]
    print(dataframe2)
    print(dataframe2.stack())
    print(dataframe2.unstack())
    print(dataframe2.pivot_table(dataframe, index=["A", "B"], columns=["C", "D"]))

def timeSeriesAndCategorical():
    ts = pd.Series(np.random.randn(500), index=pd.date_range("01/02/2020", periods=500))
    print(ts)
    ts = ts.cumsum()
    print(ts)
    plt.plot(ts)
    plt.show()
    sts = ts.to_csv("ts.csv")
    print("reading from ts.csv file")
    pdr = pd.read_csv(r"C:\Users\AHMOD\PycharmProjects\PythonDemo\ts.csv")
    print(pdr)

if __name__ == '__main__':
    # seriesAndDataframe()
    # viewData()
    # handlingMissingData()
    # pandasOperation()
    # stackAndPivot()
    timeSeriesAndCategorical()
