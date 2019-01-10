# Python Profiling

## Small Code Snippets => `timeit` Module

#### Python Programming Interface

Check out `sum.py`

```bash
> python3 -m timeit -s 'import sum' 'sum.main()'
```

Check out `for_loop.py`

```bash
> python3 -m timeit -s 'import for_loop' 'for_loop.main()'
```

#### Command-Line Interface

(Diretly run <u>the codes to be timed</u> from command-line interface)

```bash
> python3 -m timeit -s 'x = range(10000)' 'total = sum(x)'
```

<br>

## Python Application => `cProfile` Module

#### Python Programming Interface

* Use `cProfile.run()` function

  Check out `cprofile_demo1.py`

* Use `cProfile.Profile` and `pstats.Stats` classes

  Check out `cprofile_demo2.py`

#### Command-Line Interface

(Directly run <u>the script to be profiled</u> from command-line interface)

```bash
> python3 -m cProfile [-o outputfile] [-s sort_order] scripy.py
```

