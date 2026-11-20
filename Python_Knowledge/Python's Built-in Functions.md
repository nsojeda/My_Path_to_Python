# Python's Built-in Functions

## 1. Type Conversion & Creation

| Function | What it does |
|---|---|
| `bool(x)` | Converts to boolean |
| `int(x)` | Converts to integer |
| `float(x)` | Converts to float |
| `str(x)` | Converts to string |
| `list(x)` | Converts iterable to list |
| `tuple(x)` | Converts iterable to tuple |
| `dict(x)` | Converts key-value pairs to dict |
| `set(x)` | Converts to set |
| `frozenset(x)` | Immutable set |
| `complex(x)` | Complex number |

## 2. Iterable & Sequence Tools

| Function | What it does |
|---|---|
| `len(x)` | Returns length |
| `range(n)` | Generates a sequence |
| `enumerate(iterable)` | Yields index + value |
| `zip(*iterables)` | Pairs elements by index |
| `reversed(seq)` | Returns reversed iterator |
| `sorted(iterable, key=…, reverse=…)` | Returns sorted list |
| `min(*args)` | Smallest value |
| `max(*args)` | Largest value |
| `sum(iterable, start)` | Sum of values |
| `any(iterable)` | True if any element is truthy |
| `all(iterable)` | True if all elements are truthy |

## 3. Functional Tools

| Function | What it does |
|---|---|
| `map(func, iterable)` | Applies func to each element |
| `filter(func, iterable)` | Filters elements where func returns True |
| `iter(obj)` | Returns an iterator |
| `next(iterator, default)` | Gets next item from iterator |
| `callable(obj)` | Checks if object is callable |
| `isinstance(obj, class)` | Checks type inheritance |
| `issubclass(cls, class)` | Checks class inheritance |

## 4. I/O & Interaction

| Function | What it does |
|---|---|
| `print(*objects, sep=…, end=…)` | Prints to stdout |
| `input(prompt)` | Reads a line from stdin |
| `open(file, mode)` | Opens a file |

## 5. Object Introspection

| Function | What it does |
|---|---|
| `type(obj)` | Returns the type |
| `dir(obj)` | Lists attributes / methods |
| `help(obj)` | Opens help system |
| `hasattr(obj, name)` | Checks for attribute |
| `getattr(obj, name, default)` | Gets attribute |
| `setattr(obj, name, value)` | Sets attribute |
| `delattr(obj, name)` | Deletes attribute |
| `vars(obj)` | Returns `__dict__` |
| `repr(obj)` | Returns unambiguous representation |

## 6. Math & Random

| Function | What it does |
|---|---|
| `abs(x)` | Absolute value |
| `round(number, ndigits)` | Rounds a number |
| `divmod(a, b)` | Returns `(a // b, a % b)` |
| `pow(x, y, z)` | Exponentiation; `z` is optional modulo |
| `hex(x)` / `oct(x)` / `bin(x)` | Base conversions |
| `ord(c)` / `chr(i)` | Unicode code point ↔ character |
| `hash(obj)` | Returns hash value |

## 7. Advanced

| Function | What it does |
|---|---|
| `eval(expression)` | Evaluates a string as Python code |
| `exec(object)` | Executes Python code |
| `compile(source, filename, mode)` | Compiles code to bytecode |
| `globals()` / `locals()` | Returns global / local namespace |
| `super()` | Returns a proxy for parent class |
| `property(fget, fset, fdel)` | Creates a property descriptor |
| `staticmethod(func)` | Creates a static method |
| `classmethod(func)` | Creates a class method |
| `slice(start, stop, step)` | Creates a slice object |
| `memoryview(obj)` | Creates a memory view |
| `object()` | Creates a new featureless object |
| `format(value, format_spec)` | Formats a value |

---

## Quick Tips

- **`*args` / `**kwargs`**: Many built-ins accept arbitrary arguments (e.g., `min(a, b, c)`, `print(a, b, c)`).
- **`len()`** is the only sequence function that raises `TypeError` on non-sequences — it uses `__len__`.
- **`eval()` and `exec()`** are powerful but dangerous with untrusted input — avoid them when possible.
- Use `help()` or `dir()` to explore any object at runtime.