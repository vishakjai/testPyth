import os
import tempfile
from csv_utils import parse_csv


def _write_tmp(content: str) -> str:
    tf = tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".csv")
    try:
        tf.write(content)
        tf.flush()
        return tf.name
    finally:
        tf.close()


def test_with_header():
    content = """a,b,c
1,2,3
4,5,6
"""
    path = _write_tmp(content)
    try:
        rows = parse_csv(path)
        assert isinstance(rows, list)
        assert rows == [{"a": "1", "b": "2", "c": "3"}, {"a": "4", "b": "5", "c": "6"}]
    finally:
        os.unlink(path)


def test_without_header():
    content = """1,2
3,4
"""
    path = _write_tmp(content)
    try:
        rows = parse_csv(path, has_header=False)
        assert rows == [["1", "2"], ["3", "4"]]
    finally:
        os.unlink(path)


def test_lazy_generator():
    content = """x,y
a,b
c,d
"""
    path = _write_tmp(content)
    try:
        gen = parse_csv(path, lazy=True)
        assert hasattr(gen, "__iter__")
        out = list(gen)
        assert out[0] == {"x": "a", "y": "b"}
    finally:
        os.unlink(path)
