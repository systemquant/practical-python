# fileparse.py
#
# Exercise 3.3
import collections
import csv
import zlib
import pathlib


def parse_csv(file, select: bool = None, types: list = [], has_headers: bool = True, delimiter: str = '', silence_errors: bool = False) -> list:
    """
    CSV 파일을 파싱해 레코드의 목록을 생성
    """

    # Filetype Shielder
    if isinstance(file, str):
        raise TypeError(f"Type {type(file)} is not compatible")
    
    elif not(isinstance(file, collections.Iterable)):
        raise TypeError(f"Type {type(file)} is not iterable")

    # header conflict check
    if select and not(has_headers):
        raise RuntimeError("select argument requires column headers")

    rows = csv.reader(
        file, delimiter=delimiter) if delimiter else csv.reader(file)

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


def read_csv(filename: str, select: bool = None, types: list = [], has_headers: bool = True, delimiter: str = '', silence_errors: bool = False) -> list:
    path = pathlib.Path(filename)
    suffix_list = path.suffixes

    if len(suffix_list) == 1:
        with open(filename) as f:
            return parse_csv(f, select, types, has_headers, delimiter, silence_errors)

    else:
        
        '''
        # Decompress
        with open(filename, 'rb') as f:
            decom: bytes = None

            while len(suffix_list) > 1:
                zip_type = suffix_list.pop()
                #print(zip_type, suffix_list)
                
                if len(suffix_list) == 2:
                    if zip_type == '.gz':
                        decom = zlib.decompress(f.read())
                        print(decom, type(decom))
                        
                else:
                    if zip_type == '.gz':
                        decom = zlib.decompress(f.read())
                        print(decom, type(decom))
                        
                    else:
                        raise TypeError(
                            f'Type {zip_type} is not supported to decompress')
                
            
            return parse_csv(decom, select, types, has_headers, delimiter, silence_errors)
        
        '''


if __name__ == "__main__":
    # portfolio = read_csv("Data/portfolio.csv", types=[str, int, float])
    # print(portfolio)

    # print("")
    # shares_held = read_csv(
    #     "Data/portfolio.csv", select=["name", "shares"], types=[str, int]
    # )
    # print(shares_held)

    # print("")
    # prices = read_csv('Data/prices.csv',
    #                    types=[str, float], has_headers=False)
    # print(prices)

    # print('')
    # portfolio = read_csv('Data/portfolio.dat',
    #                       types=[str, int, float], delimiter=' ')
    # print(portfolio)

    # portfolio2 = read_csv('Data/missing_origin.csv', types=[str, int, float])
    # print(portfolio2)

    # portfolio = read_csv('Data/missing.csv',
    #                       types=[str, int, float], silence_errors=True)
    # print(portfolio2)
    
    portfolio3 = read_csv(
        'Data/portfolio.csv.gz', select=['name', 'shares', 'price'], types=[str, int, float])
    print(portfolio3)
