import gzip
with gzip.open('Data/portfolio.csv.gz', 'r') as f:
    for line in f:
        print(line, end='')