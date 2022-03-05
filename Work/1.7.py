import csv
f = open('Data/portfolio.csv')
rows = csv.reader(f)
headers = next(rows)

#print(rows)

print(headers)
for row in rows:
    print(row)

f.close()
