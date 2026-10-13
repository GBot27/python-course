"""M01 · data types: practice.

Replace each `raise NotImplementedError` with your solution. The docstring is the
spec, and the `>>>` examples are runnable as a quick check:

    uv run python -m doctest practice/m01_data_types.py

Full test suite: `uv run pytest -q tests/test_m01_data_types.py`
Suggested order is top to bottom; each section matches a section in the notes.
"""

from collections.abc import Hashable, Iterable
from decimal import Decimal

# ------------------------------------------------------------------ 1. Strings


def word_count(text: str) -> dict[str, int]:
    """Return how many times each word appears (case-insensitive).

    Words are separated by any run of whitespace. Punctuation is NOT stripped,
    so "hi," and "hi" are different words. Blank text gives an empty dict.

    >>> word_count("a A b")
    {'a': 2, 'b': 1}
    >>> word_count("Hello, hello")
    {'hello,': 1, 'hello': 1}
    """
    raise NotImplementedError


def is_palindrome(text: str) -> bool:
    """Return True if text reads the same backwards, ignoring case and anything
    that is not a letter or a digit.

    Text with no letters or digits at all counts as a palindrome.

    >>> is_palindrome("A man, a plan, a canal: Panama")
    True
    >>> is_palindrome("race a car")
    False
    """
    raise NotImplementedError


def format_row(name: str, qty: int, unit_price: Decimal) -> str:
    """Format one receipt line as a fixed-width row. Columns are joined by " | ".

    - name:       left-aligned,  width 10
    - qty:        right-aligned, width 3
    - unit price: right-aligned, width 7, 2 decimal places
    - line total: right-aligned, width 8, 2 decimal places (qty * unit_price)

    Use one f-string with format specs. Widths are minimums, nothing is cut off.

    >>> format_row("Widget", 3, Decimal("4.50"))
    'Widget     |   3 |    4.50 |    13.50'
    """
    raise NotImplementedError


# ------------------------------------------------------------------ 2. Numbers


def sum_prices(prices: list[str]) -> Decimal:
    """Add up price strings exactly, with no floating-point error.

    An empty list sums to Decimal("0"). The result is always a Decimal.

    >>> sum_prices(["0.10", "0.20"])
    Decimal('0.30')
    """
    raise NotImplementedError


def round_half_up(value: Decimal) -> Decimal:
    """Round to exactly 2 decimal places, with ties going away from zero.

    Python's default rounding mode for Decimal is "half even": ties go to the
    nearest even digit (0.125 -> 0.12). Money usually wants the schoolbook rule
    instead (0.125 -> 0.13, -0.125 -> -0.13). The result keeps 2 places (1 -> 1.00).

    >>> round_half_up(Decimal("2.675"))
    Decimal('2.68')
    >>> round_half_up(Decimal("1"))
    Decimal('1.00')
    """
    raise NotImplementedError


# ------------------------------------------------- 3. Truthiness and None


def count_missing(values: list[object]) -> int:
    """Count how many values are None.

    0, "", [] and False are real values, not missing ones.

    >>> count_missing([1, None, 0, "", None])
    2
    """
    raise NotImplementedError


# ------------------------------------------------- 4. Slicing and unpacking


def last_n(items: list[int], n: int) -> list[int]:
    """Return a NEW list holding the last n items.

    n == 0 gives []. An n larger than len(items) gives a copy of everything.
    Raises ValueError if n is negative.

    >>> last_n([1, 2, 3, 4], 2)
    [3, 4]
    >>> last_n([1, 2, 3], 0)
    []
    """
    raise NotImplementedError


def rotate_left(items: list[int], k: int) -> list[int]:
    """Return a NEW list rotated left by k positions. `items` is not modified.

    k may be larger than len(items), or negative (which rotates right).
    An empty list stays empty.

    >>> rotate_left([1, 2, 3, 4, 5], 2)
    [3, 4, 5, 1, 2]
    >>> rotate_left([1, 2, 3, 4, 5], -1)
    [5, 1, 2, 3, 4]
    """
    raise NotImplementedError


def chunk(items: list[int], size: int) -> list[list[int]]:
    """Split items into consecutive chunks of `size`; the last may be shorter.

    An empty list gives []. Raises ValueError if size < 1.

    >>> chunk([1, 2, 3, 4, 5], 2)
    [[1, 2], [3, 4], [5]]
    """
    raise NotImplementedError


def head_tail(items: Iterable[int]) -> tuple[int, list[int]]:
    """Split an iterable into its first item and a list of the rest.

    Use unpacking, not indexing, so it works on any iterable (list, range,
    iterator). Raises ValueError when there are no items at all.

    >>> head_tail([1, 2, 3])
    (1, [2, 3])
    >>> head_tail(range(1))
    (0, [])
    """
    raise NotImplementedError


# ------------------------------------------------------------------ 5. Dicts


def invert_dict(d: dict[str, int]) -> dict[int, list[str]]:
    """Map each value to the list of keys that had it, keys in original order.

    Several keys can share one value, so a plain key/value swap would silently
    lose data.

    >>> invert_dict({"a": 1, "b": 2, "c": 1})
    {1: ['a', 'c'], 2: ['b']}
    """
    raise NotImplementedError


def merge_sum(a: dict[str, int], b: dict[str, int]) -> dict[str, int]:
    """Return a NEW dict with the keys of both; shared keys get the summed value.

    Neither input may be modified.

    >>> merge_sum({"a": 1, "b": 2}, {"b": 3, "c": 4})
    {'a': 1, 'b': 5, 'c': 4}
    """
    raise NotImplementedError


# ------------------------------------------------------- 6. Lists and sets


def dedupe_preserve_order(items: Iterable[Hashable]) -> list[Hashable]:
    """Remove duplicates, keeping the first occurrence of each item, in order.

    Two items are duplicates when they are equal (==). Unhashable items such as
    lists raise TypeError. (Generics that tie the output type to the input type
    come in M08, so `Hashable` will do for now.)

    >>> dedupe_preserve_order([3, 1, 3, 2, 1])
    [3, 1, 2]
    """
    raise NotImplementedError


def diff_tags(old: list[str], new: list[str]) -> tuple[set[str], set[str], set[str]]:
    """Compare two tag lists and return (added, removed, kept) as sets.

    added:   in `new` but not in `old`
    removed: in `old` but not in `new`
    kept:    in both
    Duplicates inside the inputs make no difference.

    >>> diff_tags(["a", "b"], ["b", "c"])
    ({'c'}, {'a'}, {'b'})
    """
    raise NotImplementedError


def common_to_all(lists: list[list[str]]) -> set[str]:
    """Return the items that appear in every list.

    No lists at all gives an empty set (watch out: that is an edge case).

    >>> sorted(common_to_all([["a", "b", "c"], ["b", "c", "d"], ["c", "b"]]))
    ['b', 'c']
    """
    raise NotImplementedError


# ------------------------------------------------------------- 7. Aliasing


def make_grid(rows: int, cols: int, fill: int = 0) -> list[list[int]]:
    """Build a rows x cols grid (a list of rows) with every cell set to `fill`.

    Each row must be its own list: changing grid[0][0] must not touch any
    other row.

    >>> make_grid(2, 3, fill=7)
    [[7, 7, 7], [7, 7, 7]]
    """
    raise NotImplementedError


def clone_config(config: dict[str, list[int]]) -> dict[str, list[int]]:
    """Return a fully independent copy of config.

    Mutating the clone, including the lists inside it, must never change the
    original, and the other way round.

    >>> original = {"ports": [80, 443]}
    >>> clone = clone_config(original)
    >>> clone["ports"].append(8080)
    >>> original
    {'ports': [80, 443]}
    """
    raise NotImplementedError
