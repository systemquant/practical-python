# tableformat.py

class FormatError(Exception):
    pass

class TableFormatter:
    def headings(self, table):
        """
        테이블 헤딩을 반환
        """
        raise NotImplementedError()

    def row(self, rowdata):
        """
        테이블 데이터의 단일 행을 반환
        """
        raise NotImplementedError()


def create_formatter(fmt):
    format_dict = {
        'txt': TextTableFormatter,
        'csv': CSVTableFormatter,
        'html': HTMLTableFormatter,
    }
    try:
        return format_dict[fmt]()
    except KeyError as name:
        raise FormatError(f'Unknown table format {fmt}')

def print_table(portfolio, headings, formatter):
    formatter.headings(headings)
    for stock in portfolio:
        rowdata = [str(getattr(stock, head)) for head in headings]
        formatter.row(rowdata)


class TextTableFormatter(TableFormatter):
    """
    테이블을 일반 텍스트 포맷으로 출력
    """

    def headings(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')

        print()
        print(('-' * 10 + ' ') * len(headers))

    def row(self, rowdata):
        for d in rowdata:
            print(f'{d:>10s}', end=' ')
        print()


class CSVTableFormatter(TableFormatter):
    """
    포트폴리오 데이터를 CSV 포맷으로 출력.
    """

    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(rowdata))


class HTMLTableFormatter(TableFormatter):
    def headings(self, headers):
        print('<tr><th>' + '</th><th>'.join(headers) + '</th></tr>')

    def row(self, rowdata):
        print('<tr><td>' + '</td><td>'.join(rowdata) + '</td></tr>')


class HTMLTableFormatter2(TableFormatter):
    def openclose(self, line: str, tag: str):
        return f'<{tag}>' + line + f'</{tag}>'

    def lineclose(self, line: str):
        print(self.openclose(line, 'tr'))

    def headings(self, headers):
        html = ''
        for header in headers:
            html += self.openclose(header, 'th')

        self.lineclose(html)

    def row(self, rowdata):
        html = ''
        for row in rowdata:
            html += self.openclose(row, 'td')

        self.lineclose(html)

if __name__ == '__main__':
    formatter = create_formatter('xls')