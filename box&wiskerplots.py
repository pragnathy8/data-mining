from matplotlib import pyplot
from pandas import read_csv
filename='diabetes.csv'
data=read_csv(filename)
data.plot(kind='box', subplots=True, layout=(3,3), sharex=False,sharey=False)
pyplot.show()