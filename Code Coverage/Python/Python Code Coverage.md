# Python Code Coverage (by Test Cases)

## Installation

```bash
> pip3 install coverage
```

<br>

## Usage

***

Check out https://github.com/Ziang-Lu/Software-Development-and-Design/blob/master/1-Software%20Phases/4-Testing.md for <u>various coverage criteria</u>:

* Statement Coverage
* Branch Coverage

***

* **Statement Coverage**

  ```bash
  > coverage3 run script.py
  ```

* **Branch Coverage**

  ```bash
  > coverage3 run --branch script.py
  ```

**Specify / Omit the source files:**

Use `--source`, `--include`, `--omit` command-line options

**Output the report to the terminal:**

```bash
> coverage3 report -m --fail-under=0.8
# -m will show the line numbers of the codes that are not covered
# --fail-under=MIN specifies that if the total coverage is < MIN, exit with a status of 2
```

**Generate a `htmlcov/` folder, which contains reports in html format:**

```bash
> coverage3 html --fail-under=0.8 --title="Coverage Result"
```

**Exclude reporting on some code:**

*<u>Excluded code is executed as usual,  and its execution is recorded in the coverage data as usual. However, when producing reports, `coverage.py` excludes it from the list of missing code.</u>*

```python
debug = False

a = my_func1()
if debug:  # pragma: no cover
    msg = 'bla bla'
    log_message(msg, a)
b = my_func2()
# Note that "# pragma: no cover" will exclude the entire clause, function or class definition
```

