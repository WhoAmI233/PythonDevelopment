from numpy import *
import operator
import matplotlib
import matplotlib.pyplot as plt

def createrDataSet():
    group = array([1,1,2,2,3,4,5])
    labels = ['A','A','B','B']
    return group,labels

def testMatplotlib():
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter([1],[2])
    plt.show()

if __name__ == '__main__':
    group, labels=createrDataSet()
    print (group)
    testMatplotlib()

