# fileparse.py
#
# Exercise 3.3
import csv
import logging

log = logging.getLogger(__name__)


def parse_csv(
    lines,
    select=None,
    types=None,
    has_headers=True,
    delimiter=",",
    silence_errors=False,
):
    """
    Parse a file-like objects into a list of records
    """
    if select and not has_headers:
        raise RuntimeError("select argument requires column headers")

    if isinstance(lines, str):
        raise RuntimeError("file-like object required")
    else:
        rows = csv.reader(lines, delimiter=delimiter)

    if has_headers:
        # Read the headers
        headers = next(rows)

        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select
        else:
            indices = []

    records = []
    for rowno, row in enumerate(rows, start=1):
        if not row:  # Skip line with no data
            continue

        try:
            # Filter the row if specific columns are selected
            if has_headers and indices:
                row = [row[index] for index in indices]
            # Perform type conversion
            if types:
                row = [func(val) for func, val in zip(types, row)]

            # Make a dictionary
            if has_headers:
                record = dict(zip(headers, row))
            else:  # Make a tuple
                record = tuple(row)

            records.append(record)
        except ValueError as e:
            if not silence_errors:
                log.warning("Row: %d Couldn't convert %s", rowno, row)
                log.debug("Row: %d Reason: %s", rowno, e)
    return records
