import csv


def read_csv_headers(filename, delimiter=','):
    f = open(filename, 'r')
    reader = csv.reader(f, delimiter=delimiter)
    headers = next(reader, None)
    if headers:
        column = {}
        for h in headers:
            column[h] = []
        for row in reader:
            for h, v in zip(headers, row):
                column[h].append(v)
    f.close()
    return column if headers else False
