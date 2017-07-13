from pandas import Series, DataFrame
import pandas as pd

# about Series
# obj = Series([1,-1,2,-2])
# print("obj:\n",obj)
# print("obj.values:\n",obj.values)
#
# obj2 = Series([1,-1,2,-2],index=['a','c','b','d'])
# print("obj2:\n",obj2)
# print("obj2.index:\n",obj2.index)
#
# print('e' in obj2)
#
# sdata={'echo':33333,'alex':22222,'Charm':11111}
# obj3 = Series(sdata)
# print("obj3:\n",obj3)

# about DataFrame
data={'state':['Ohio','Ohio','Ohio','Nevada','Nevada'],'year':[2000,2001,2002,2001,2002],'pop':[1.5,1.7,3.6,2.4,2.9]}
frame = DataFrame(data,columns=['year','state','pop'])
print("Frame:\n",frame)
print("Frame['year']:\n",frame['year'])