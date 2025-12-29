# fileparse.py
#
# Exercise 3.3
import csv


def parse_csv(filename, select=None, types=None, has_headers=True, delimiter=','):
    """
    Parse a CSV file into a list of records
    """
    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)

        if has_headers:
            # Read the file headers
            headers = next(rows)

            if select:
                indices = [headers.index(colname) for colname in select]
                headers = select
            else:
                indices = []

        records = []
        for row in rows:    # Skip rows with no data
            if not row:
                continue
            # Filter the row if specific columns are selected
            if has_headers and indices:
                row = [row[index] for index in indices]
            # Perform type conversion
            if types:
                row = [func(val) for func, val in zip(types, row)]

            # Make a dictionary
            if has_headers:
                record = dict(zip(headers, row))
            else:    # Make a tuple
                record = tuple(row)

            records.append(record)
    return records
