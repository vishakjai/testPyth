"""Small CSV parsing utility.

Provides `parse_csv()` which returns a list or a generator of rows.
"""
from typing import List, Dict, Iterator, Union
import csv


def parse_csv(
    path: str,
    delimiter: str = ",",
    has_header: bool = True,
    encoding: str = "utf-8",
    strip: bool = True,
    lazy: bool = False,
) -> Union[List[Union[List[str], Dict[str, str]]], Iterator[Union[List[str], Dict[str, str]]]]:
    """Parse a CSV file.

    - If `has_header` is True, rows are returned as dicts mapping header->value.
    - If `has_header` is False, rows are returned as lists of values.
    - If `lazy` is True, returns a generator; otherwise returns a list.

    Args:
      path: Path to the CSV file.
      delimiter: Field delimiter (default ',').
      has_header: Whether the first row is a header.
      encoding: File encoding.
      strip: Trim whitespace from each cell.
      lazy: If True, return a generator else return a list.

    Returns:
      List or generator of rows (dicts if header present, else lists).
    """

    def _iter_rows():
        with open(path, newline="", encoding=encoding) as f:
            reader = csv.reader(f, delimiter=delimiter)
            if has_header:
                header = next(reader, None)
                if header is None:
                    return
                if strip:
                    header = [h.strip() for h in header]
                for row in reader:
                    if strip:
                        row = [c.strip() for c in row]
                    yield dict(zip(header, row))
            else:
                for row in reader:
                    if strip:
                        row = [c.strip() for c in row]
                    yield row

    if lazy:
        return _iter_rows()
    else:
        return list(_iter_rows())


__all__ = ["parse_csv"]
