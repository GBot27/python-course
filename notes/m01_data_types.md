# M01 · Data types

**Time:** ~5h. About 1.5h reading this file, about 3.5h on `practice/m01_data_types.py`.
**Run the REPL:** `uv run python` (try every snippet below; typing beats reading).
**Docs:** Python's stdlib docs are stable and excellent. Skim the links at the bottom.

## 0. The mental model

Python names are **labels stuck on objects**, not boxes holding values. This is
the same model as JS references, with two differences worth knowing up front:

| Topic      | JavaScript / TypeScript                  | Python                                                 |
| ---------- | ---------------------------------------- | ------------------------------------------------------ |
| Primitives | `number`, `string`, `boolean` are values | Everything is an object, even `5` (`(5).bit_length()`) |
| Typing     | Weak coercion: `"1" + 1 === "11"`        | Dynamic but **strong**: `"1" + 1` raises `TypeError`   |
| Constants  | `const`                                  | None. Convention only: `MAX_RETRIES = 3`               |
| "Nothing"  | `null` and `undefined`                   | Only `None`                                            |

`type(x)` tells you what an object is. `id(x)` tells you which object it is.

## 1. Numbers

- `int`: **arbitrary precision**. `2**100` just works. No `BigInt`, no overflow.
  Use `1_000_000` for readability.
- `float`: IEEE 754 double, **the same as a JS `number`**. So `0.1 + 0.2 == 0.3`
  is `False` here too. Compare with `math.isclose`.
- `Decimal` (`from decimal import Decimal`): exact base-10 arithmetic. Use it for
  **money**. Always build it from a **string**: `Decimal("0.1")`, never
  `Decimal(0.1)`, which faithfully copies the float's error
  (`0.1000000000000000055511...`).
- `bool` is a subclass of `int`: `True + True == 2`. A quirk, mostly harmless.

### Division and rounding (differs from JS!)

| Expression      | Result    | Note                                                    |
| --------------- | --------- | ------------------------------------------------------- |
| `7 / 2`         | `3.5`     | `/` is **always** float division                        |
| `7 // 2`        | `3`       | `//` floors (rounds toward negative infinity)           |
| `-7 // 2`       | `-4`      | JS `Math.trunc(-7/2)` would give `-3`                   |
| `-7 % 2`        | `1`       | Result takes the sign of the **divisor**. JS gives `-1` |
| `divmod(-7, 2)` | `(-4, 1)` | quotient and remainder in one call                      |

- `round()` uses **banker's rounding** (ties to the nearest even digit):
  `round(2.5) == 2`, `round(3.5) == 4`. And `round(2.675, 2) == 2.67` because
  `2.675` is not exactly representable as a float.
- `Decimal` has its own **rounding mode** (a setting in its context). The default
  is also "half even". For money you usually want schoolbook rounding, so read
  the `decimal` docs on rounding modes and on `Decimal.quantize`. You need them
  for `round_half_up`.
- Conversions are explicit: `int("42")`, `float("3.5")`, `str(42)`. Bad input
  raises `ValueError`. `int(3.9) == 3` and `int(-3.9) == -3` (truncates).

## 2. Strings

- `str` is an **immutable** sequence of Unicode code points. Indexing gives
  another `str` (there is no char type). Out-of-range indexing raises
  `IndexError`, it does not return `undefined`.
- Quotes: `'a'` and `"a"` are identical. `"""triple"""` spans lines. `r"\d+"` is a
  raw string (no escape processing, handy for regexes).
- **f-strings** are Python's template literals: `f"{name} is {age}"`. Expressions
  go inside `{}`, and after a colon comes the **format spec mini-language**:

```python
pi, n, name = 3.14159, 1234567, "Ada"
f"{pi:.2f}"  # '3.14'        2 decimals
f"{n:,}"  # '1,234,567'   thousands separator
f"{name:<6}"  # 'Ada   '      left-align, width 6
f"{name:>6}"  # '   Ada'      right-align
f"{name:^6}"  # ' Ada  '      center
f"{42:05d}"  # '00042'       zero-pad
f"{0.256:.1%}"  # '25.6%'       percent
f"{name!r}"  # "'Ada'"       repr() instead of str()
f"{n=}"  # 'n=1234567'   debug form, prints the expression too
```

Full spec: <https://docs.python.org/3/library/string.html#formatspec>.
(Since 3.12 you can reuse the same quote type inside `{}`.)

- Methods you will use daily: `split`, `join`, `strip`, `lower`/`upper`/`casefold`,
  `startswith`/`endswith`, `replace`, `partition`, `isalnum`/`isdigit`/`isalpha`.
  They **return new strings**, nothing mutates.
- `join` is on the **separator**, the reverse of JS: `", ".join(items)` vs
  `items.join(", ")`.
- `find` returns `-1` when missing, `index` raises `ValueError`. `"x" in s` tests
  for a substring.
- Building a string in a loop with `+=` is fine for small cases. For many pieces,
  collect them in a list and `join` once.
- `bytes` are what sockets, files and HTTP bodies carry. `str` ⇄ `bytes` is
  explicit: `"é".encode("utf-8")` gives `b'\xc3\xa9'`, and `.decode("utf-8")` goes
  back. `len("é") == 1` but `len("é".encode()) == 2`. You will meet this in backend work.

## 3. `bool`, `None` and truthiness

- Literals are capitalized: `True`, `False`, `None`. Operators are words:
  `and`, `or`, `not`. Chained comparisons work: `0 < x < 10`.
- `and`/`or` return **one of their operands**, as in JS: `name or "anonymous"`.
- **Falsy values**: `False`, `None`, `0`, `0.0`, `Decimal(0)`, `""`, `[]`, `()`,
  `{}`, `set()`, `range(0)`. Everything else is truthy, including `"0"`, `" "`,
  `[0]` and `float("nan")`.

| Value           | JS truthy? | Python truthy? |
| --------------- | ---------- | -------------- |
| `[]`            | yes        | **no**         |
| `{}` / `dict()` | yes        | **no**         |
| `"0"`           | yes        | yes            |
| `NaN`           | **no**     | yes            |

- Test for `None` with **`is None`**, never `== None`. `if not x:` also catches
  `0`, `""` and `[]`, so use it only when "empty" and "missing" mean the same thing.
- A missing dict key raises `KeyError`, a missing attribute raises
  `AttributeError`. Neither silently returns `None`/`undefined`.

## 4. The big four collections

| Type    | Literal    | Mutable | Ordered         | Duplicates  | Lookup `x in c` | TS analogue                               |
| ------- | ---------- | ------- | --------------- | ----------- | --------------- | ----------------------------------------- |
| `list`  | `[1, 2]`   | yes     | yes (by index)  | yes         | O(n)            | `Array<T>`                                |
| `tuple` | `(1, 2)`   | **no**  | yes (by index)  | yes         | O(n)            | `readonly [A, B]`, no exact JS equivalent |
| `dict`  | `{"a": 1}` | yes     | insertion order | keys unique | O(1) by key     | `Map<K, V>` (not a plain object)          |
| `set`   | `{1, 2}`   | yes     | **no**          | **no**      | O(1)            | `Set<T>` (but no order guarantee)         |

### list

- Dynamic array: `append`, `extend`, `insert`, `pop`, `remove`, `index`, `count`.
- **`list.sort()` sorts in place and returns `None`.** `x = x.sort()` is a classic
  bug. `sorted(x)` returns a new list and leaves `x` alone. Same for `reverse()`
  vs `reversed()`.
- Negative indexes count from the end: `x[-1]` is the last item (JS: `x.at(-1)`).
- `a + b` makes a new list. `a += b` **mutates** `a` in place.

### tuple

- Immutable, and **hashable** if its items are, so tuples work as dict keys and
  set members (`{(0, 0): "origin"}`).
- One-item tuple needs a comma: `(1,)`. `(1)` is just `1`.
- Convention: **list = many items of the same kind** (`list[int]`), **tuple = a
  fixed-shape record** (`tuple[str, int]`, e.g. `(name, age)`). Functions that
  "return several values" return a tuple.
- Immutability is shallow: `(1, [2])` is a tuple, but that inner list can still change.

### dict

- **Insertion-ordered** (guaranteed since 3.7). Keys must be **hashable**: `str`,
  `int`, `tuple` of hashables, yes. `list`, `dict`, `set`, no
  (`TypeError: unhashable type: 'list'`).
- Closest to a JS `Map`: any hashable key, not just strings. A JS object is
  different: it reorders integer-like keys and uses dot access. A dict has **no
  dot access** (`d.name` is an `AttributeError`). Typed records come later
  (dataclasses in M10, Pydantic in the backend levels).
- Read with `d[k]` (raises `KeyError`) or `d.get(k)` / `d.get(k, default)`.
- Iterating a dict gives **keys**. For pairs use `d.items()`; also `d.keys()` and
  `d.values()`. These return **live views**, not copies.
- Merge with `a | b` (3.9+) or `{**a, **b}`. On a conflict the **right side wins**.
  Both build a new dict.
- `"k" in d` checks keys. `del d[k]` and `d.pop(k, default)` remove.

### set

- Unique, unordered, hashable members. Built for membership tests and algebra:

```python
s, u = {1, 2, 3}, {3, 4}
s | u  # union                {1, 2, 3, 4}
s & u  # intersection         {3}
s - u  # difference           {1, 2}
s ^ u  # symmetric difference {1, 2, 4}
{1} <= s  # subset               True
```

- **`{}` is an empty dict, not an empty set.** An empty set is `set()`.
- Do not rely on set iteration order. Convert with `sorted(s)` when order matters.
- `frozenset` is the immutable, hashable version.

### Which one? (the one-sentence test)

- Ordered, growable sequence of similar things → **list**
- Fixed-shape record, a dict key, or "return several values" → **tuple**
- Look something up by a key → **dict**
- "Have I seen this?", dedupe, or what's common/different between groups → **set**

## 5. Slicing

`seq[start:stop:step]` works on `str`, `list`, `tuple` and `range`.
**`stop` is exclusive**, every part is optional, negatives count from the end.

```python
a = [0, 1, 2, 3, 4, 5]
a[1:4]  # [1, 2, 3]
a[:2]  # [0, 1]
a[-2:]  # [4, 5]
a[::2]  # [0, 2, 4]
a[::-1]  # [5, 4, 3, 2, 1, 0]   reversed copy
a[:]  # shallow copy
```

- **A slice that runs past the end is clamped, never an error**: `a[2:100]` and
  `a[10:]` (gives `[]`) are fine. A plain index `a[10]` raises `IndexError`.
- A slice always builds a **new** object (shallow copy for lists).
- Lists support slice assignment: `a[1:3] = [9]` replaces that range.
- JS bridge: `slice(a, b)` ≈ `[a:b]`, `at(-1)` ≈ `[-1]`. JS has no step.
- **Trap:** `a[-n:]` means "the last n items" only while `n > 0`. Think about what
  `-0` is.

## 6. Mutability, identity and copying

- **Immutable:** `int`, `float`, `Decimal`, `bool`, `str`, `bytes`, `None`,
  `tuple`, `frozenset`.
  **Mutable:** `list`, `dict`, `set`, and most objects you define.
- `==` compares **values**: `[1] == [1]` is `True` (in JS it is `false`).
  `is` compares **identity**, same object, like JS `===` on objects.
  `id(x)` shows the identity.
- Use `is` for `None` (and `True`/`False`/sentinels), nothing else. Never rely on
  `a is b` for numbers or strings. Python caches some, and that is an
  implementation detail.
- **Assignment never copies.** `b = a` just sticks a second label on the same
  object:

```python
a = b = []  # ONE list, two labels
a.append(1)
print(b)  # [1]
```

- Function arguments work the same way ("call by object reference", like JS):
  mutating a list inside a function is visible to the caller, but rebinding the
  parameter name is not.
- **Shallow vs deep copy**
  - Shallow: `list(a)`, `a.copy()`, `a[:]`, `dict(d)`, `d.copy()`. A new outer
    container, but the **inner objects are shared**.
  - Deep: `copy.deepcopy(x)` copies recursively.
  - JS bridge: `[...a]` is shallow, `structuredClone(x)` is deep.

```python
orig = {"a": [1]}
shallow = orig.copy()
orig["a"].append(2)
print(shallow)  # {'a': [1, 2]}   the inner list is shared!
```

- **The grid trap:** `[[0] * 3] * 3` repeats a reference to **one** row three
  times. Mutate one row and all of them change. Build each row separately.
- `x += y` on a list mutates it. On a tuple (no in-place version) it rebinds the
  name to a new tuple.

## 7. Unpacking

```python
a, b = b, a  # swap, no temp variable
first, *rest = [1, 2, 3]  # first=1, rest=[2, 3]
first, *mid, last = [1, 2, 3, 4]  # mid=[2, 3]
_, second, *_ = "abc"  # _ means "ignore"
for key, value in d.items():  # unpacking in a loop header
    print(key, value)
merged = [*xs, *ys]  # spread into a literal
config = {**defaults, **user}  # spread dicts, later keys win
```

- It works on **any iterable**, not just lists. The starred part is always a
  `list`. A wrong count raises `ValueError`
  (`too many values to unpack (expected 2)`).
- vs JS destructuring: Python unpacks **by position** only. There is no
  `{a, b} = obj` by key, and no default values inside the pattern. (Structural
  `match` in M02 covers the by-shape cases.)

## 8. Inspecting objects (REPL skills)

```python
type(x)  # what is it?
isinstance(x, int)
dir(x)  # attributes and methods (ignore the __dunder__ ones at first)
help(str.split)  # built-in docs, press q to quit
id(x)  # identity: same id, same object
repr(x)  # the unambiguous form; str(x) is the friendly form
```

## 9. Type hints you need now

`list[int]`, `dict[str, int]`, `set[str]`, `tuple[str, int]` (fixed shape),
`tuple[int, ...]` (any length), `int | None` (a TS-style union). For "anything I
can loop over" use `Iterable[T]` from `collections.abc`.

Hints are for you, your editor and a type checker. **Python itself ignores them
at runtime.** A proper tour (and adding a checker like pyright or mypy) is M08.

---

## Practice map

Open `practice/m01_data_types.py`. Docstrings are the spec. Work top to bottom.

| Section                | Functions                                             | Concept it drills                               |
| ---------------------- | ----------------------------------------------------- | ----------------------------------------------- |
| 1. Strings             | `word_count`, `is_palindrome`, `format_row`           | split/lower, `isalnum`, slicing, f-string specs |
| 2. Numbers             | `sum_prices`, `round_half_up`                         | `Decimal` from strings, rounding modes          |
| 3. Truthiness          | `count_missing`                                       | `is None` vs falsy                              |
| 4. Slicing / unpacking | `last_n`, `rotate_left`, `chunk`, `head_tail`         | edge cases of slices, `*rest`                   |
| 5. Dicts               | `invert_dict`, `merge_sum`                            | building dicts, no mutation of inputs           |
| 6. Lists / sets        | `dedupe_preserve_order`, `diff_tags`, `common_to_all` | hashing, set algebra, empty-input edge case     |
| 7. Aliasing            | `make_grid`, `clone_config`                           | shared references, shallow vs deep              |

Loop: **read the docstring → try it in the REPL → implement → `uv run pytest -q
tests/test_m01_data_types.py -k <name>`**. Stuck? Ask for a hint. I'll give a
small one first, a bigger one if you ask again.

## REPL lab: predict first, then run

Write your prediction **before** you press Enter. Every wrong guess is worth more
than a right one.

1. `a = b = []; a.append(1); print(b)`
2. `x = [1, 2, 3]; y = x[:]; y.append(4); print(x)`
3. `t = (1, [2]); t[1].append(3); print(t)`. Error, or not?
4. `-7 // 2` and `-7 % 2`
5. `bool(float("nan"))` and `bool([0])`
6. `d = {}; d[1] = "a"; d[1.0] = "b"; d[True] = "c"; print(d)`
7. `def f(lst): lst.append(1); lst = [99]`. Call `f(z)` with `z = []`. What is `z`?
8. `[1, 2, 3] == (1, 2, 3)` and `{1, 2} == {2, 1}`
9. `type({})`, `type(set())`, `type((1))`, `type((1,))`
10. `x = [3, 1, 2]; print(x.sort())`

## Done when (copied into the README checklist)

- [ ] All M01 tests pass (`uv run pytest -q`)
- [ ] You can explain `a = b = []` and shallow vs deep copy with an example
- [ ] You can pick list/tuple/dict/set for a problem and justify it in one sentence
- [ ] You can inspect any object in the REPL with `type`, `dir`, `help`, `id`
- [ ] `uv run ruff check . && uv run ruff format .` is clean

When you finish, say **"Review module 1"** and I'll go through your solutions like
a code review (correctness, Pythonic style, edge cases, type hints).

## Official docs

- Built-in types: <https://docs.python.org/3/library/stdtypes.html>
- Tutorial, data structures: <https://docs.python.org/3/tutorial/datastructures.html>
- Truth value testing: <https://docs.python.org/3/library/stdtypes.html#truth-value-testing>
- `decimal`: <https://docs.python.org/3/library/decimal.html>
- Format spec mini-language: <https://docs.python.org/3/library/string.html#formatspec>
- `copy`: <https://docs.python.org/3/library/copy.html>
- Objects, values and types: <https://docs.python.org/3/reference/datamodel.html#objects-values-and-types>
