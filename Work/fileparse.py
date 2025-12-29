# fileparse.py
#
# Exercise 3.3
import csv


def parse_csv(filename, select=None):
    """
    Parse a CSV file into a list of records
    """
    with open(filename) as f:
        rows = csv.reader(f)

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
            if indices:
                row = [row[index] for index in indices]

            # Make a dictionary
            record = dict(zip(headers, row))
            records.append(record)
    return records
