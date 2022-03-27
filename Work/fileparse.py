# fileparse.py
#
# Exercise 3.3
import csv


def parse_csv(filename: str, select: bool = None, types: list = [], has_headers: bool = True, delimiter: str = '', silence_errors: bool = False) -> list:
    """
    CSV 파일을 파싱해 레코드의 목록을 생성
    """
    
    if select and not(has_headers):
        raise RuntimeError("select argument requires column headers")
    
    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter) if delimiter else csv.reader(f)
        
        # 헤더를 읽음
        if has_headers:
            headers = next(rows)

        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select

        else:
            indices = []

        records = []
        for i, row in enumerate(rows):
            if not row:
                continue
     
            if indices:
                row = [row[index] for index in indices]

            if types:
                try:
                    row = [func(val) for func, val in zip(types, row)]
                except ValueError as e:
                    if not(silence_errors):
                        print(f"Row {i+1}: Couldn't convert {row}")
                        print(f"Row {i+1}: Reason {e}")
                
            if has_headers:
                record = dict(zip(headers, row))
            
            else:
                record = tuple(row)

            records.append(record)

        return records


if __name__ == "__main__":
    portfolio = parse_csv("Data/portfolio.csv", types=[str, int, float])
    print(portfolio)

    print("")
    shares_held = parse_csv(
        "Data/portfolio.csv", select=["name", "shares"], types=[str, int]
    )
    print(shares_held)
    
    print("")
    prices = parse_csv('Data/prices.csv', types=[str,float], has_headers=False)
    print(prices)

    print('')
    portfolio = parse_csv('Data/portfolio.dat', types=[str, int, float], delimiter=' ')
    print(portfolio)
    
    portfolio2 = parse_csv('Data/missing_origin.csv', types=[str, int, float])
    print(portfolio2)
    
    portfolio = parse_csv('Data/missing.csv', types=[str,int,float], silence_errors=True)
    print(portfolio2)