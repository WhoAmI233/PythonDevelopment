year = 1
years = 5
bj = 10000
rate = 0.05
f = open("D:/work/python/pythonDevelop/autoText.txt", 'w+')
while year < years:
    bj = bj * (1 + rate)
    print("第{0}年,本金息总计{1}".format(year, bj), file=f)
    year += 1