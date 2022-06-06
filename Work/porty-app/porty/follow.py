# follow.py
import os
import time


def follow(filename):
    # f = open(filename)

    with open(filename) as f:
        f.seek(0, os.SEEK_END)

        while True:
            line = f.readline()
            if line == '':
                time.sleep(0.1)
                continue

            yield line


def filematch(lines, substr):
    for line in lines:
        if substr in line:
            yield line


if __name__ == '__main__':
    from . import report

    portfolio = report.read_portfolio('Data/portfolio.csv')

    '''
    # 연습 문제 6.8: 단순한 파이프라인 구성
    lines = follow('Data/stocklog.csv')
    ibm = filematch(lines, 'IBM')

    for line in ibm:
        print(line, end='')
    '''

    '''
    # 연습 문제 6.7: 포트폴리오 감시하기
    for line in follow('Data/stocklog.csv'):
        fields = line.split(',')
        name = fields[0].strip('""')
        price = float(fields[1])
        change = float(fields[4])
        if name in portfolio:
            print(f'{name:>10s} {price:>10.2f} {change:>10.2f}')
    '''

