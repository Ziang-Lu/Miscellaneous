# `pytest` for Python

## Installation

```bash
> pip3 install pytest
```

## Usage

Check out `test_my_dict_func.py` and `test_my_dict_class.py` for test discovery rules

```bash
> pytest -v tests/
# tests/ contains the test files ("test_*.py" and "*_test.py")
# -v increase verbosity
```

**Skip some tests (maybe on some condition)**

```bash
> pytest -v -rxs tests/
# -r shows extra test summry info as specified by ...
#     x: failed
#     s: skipped
```

**Run tests selectively by <u>name</u>**

```bash
> pytest -k 'key or attr' -v tests/
# -k [EXPRESSION] EXPRESSION is a Python expression within which substrings are used to be checked against the test names
# => Run tests whose name contains "key" or "attr"
```

**Run tests selectively by <u>custom mark</u>**

```bash
> pytest -m 'linux or mac' -v tests/
# -m [MARKEXPR] MARKEXPR is a Python expression within which substrings are used to be checked against the custom marks of the tests
# => Run tests whose custom mark is "linux" or "mac"
```

