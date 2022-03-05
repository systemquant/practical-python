prices = {}

with open('Data/prices.csv', 'rt') as f:
    for line in f:
        row = line.split(',')
        try:
            prices[row[0]] = float(row[1])
        except:
            print("'", row[0], "'", sep='')

print(prices)