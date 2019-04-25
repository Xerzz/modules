import csv


def read_csv(filename, delimiter=','):
    f = open(filename, 'r')
    reader = csv.reader(f, delimiter=delimiter)
    headers = next(reader, None)

    column = {}
    for h in headers:
        column[h] = []
    for row in reader:
        for h, v in zip(headers, row):
            column[h].append(v)
    f.close()
    return column
