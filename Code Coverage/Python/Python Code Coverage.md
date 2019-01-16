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

Output the report to the terminal:

```bash
> coverage3 report -m --fail-under=0.8
# -m will show the line numbers of the codes that are not covered
# --fail-under=MIN specifies that if the total coverage is < MIN, exit with a status of 2
```

Generate a `htmlcov/` folder, which contains reports in html format:

```bash
> coverage3 html --fail-under=0.8 --title="Coverage Result"
```

