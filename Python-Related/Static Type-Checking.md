# Static Type-Checking & `typing` Auxiliary Examples

## `Optional`

`Optional[X]` <=> `Union[X, None]`

```python
from typing import Optional


def get_foo(foo_id: Optional[int]) -> Optional[int]:
    if foo_id is None:
        return None
    return Foo(foo_id)
```

<br>

## `TypeVar`

Define a self-defined type, which could be a combination of multiple types

```python
from typing import TypeVar

# Define a self-defined type "AnyStr", which is could be "str" or "bytes"
AnyStr = TypeVar('AnyStr', str, bytes)


def concat(a: AnyStr, b: AnyStr) -> AnyStr:
    return a + b
```

***

What is the difference with `Union[str, bytes]`?

<u>`TypeVar` will make sure any arguments annotated with that `AnyStr` type, actually are of the same type.</u>

```python
print(concat('s', b's'))  # Type-check error! Because "a" and "b" are both annotated with "AnyStr" type, but they are passed with arguments of different actual types.
```

***

**=> `AnyStr` is built into `typing`!!!**

<br>

## Typing World VS Duck Typing

In the typing world, how to be compatible with the traditional duck typing in Python world?

e.g., Assume we have this `render()` function, which takes in any object that itself has a `render()` method:

```python
def render(obj):
    return obj.render()
```

To support this duck typing (i.e., any object that itself has a `render()` method can be passed to this function), we can use `typing_extensions.Protocol`:

```python
from typing_extensions import Protocol


# Define a duck-typing protocol
class Renderable(Protocol):

    def render(self) -> str:
        pass


def render(obj: Renderable) -> str:
    return obj.render()
# We specified that the input object obeys "Renderable" protocol, which means it must have a "render()" method.


class Foo:

    def render(self) -> str:
        # ignored


render(Foo())  # OK, since Foo() object has a "render()" method
render(3)  # Type-check error! Since an integer does NOT have a "render()" method, and thus doesn't follow that "Renderable" protocol
```

<br>

## Best static type-checker `MyPy`

-> Check out https://mypy.readthedocs.io/en/stable/

***

When we introduce static type-checking for a large non-typed codebase, we can do it function-by-function, module-by-module, ...

We can

* Integrate `MyPy` checking to CI

* After we type-checked each module, set `MyPy` so that any non-typed functions can't be introduced to that module.

  In this way, we can "save" and "defend" our progress of static type-checking introduction.

***

<br>

## How to Auto-Generate Annotated Codes?

To generate correct annotations for a non-typed codebase, we need to correctly find the usages of the functions, methods, ...

This can be done by:

* `MonkeyType` by Instagram

  Check out https://www.youtube.com/watch?v=pMgmKJyWKn8&t=1715s and https://monkeytype.readthedocs.io/en/stable/index.html for more details

* `PyAnnatate` by Dropbox

  Check out https://pypi.org/project/pyannotate/

