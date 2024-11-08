import pandas

data = pandas.read_csv('记录.csv')
people = data['人流量']

pre_sale = []
for x in people:
    y = 12 * x
    pre_sale.append(y)

print(pre_sale)