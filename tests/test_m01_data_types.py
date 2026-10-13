from decimal import Decimal

import pytest
from m01_data_types import (
    chunk,
    clone_config,
    common_to_all,
    count_missing,
    dedupe_preserve_order,
    diff_tags,
    format_row,
    head_tail,
    invert_dict,
    is_palindrome,
    last_n,
    make_grid,
    merge_sum,
    rotate_left,
    round_half_up,
    sum_prices,
    word_count,
)

# ------------------------------------------------------------------ 1. Strings


def test_counts_words_case_insensitively():
    assert word_count("a A b") == {"a": 2, "b": 1}


def test_word_count_splits_on_any_whitespace():
    assert word_count("the cat  the\nhat\tthe") == {"the": 3, "cat": 1, "hat": 1}


@pytest.mark.parametrize("text", ["", "   ", "\n\t "])
def test_word_count_blank_text_is_empty(text):
    assert word_count(text) == {}


def test_word_count_keeps_punctuation_attached():
    assert word_count("Hello, hello") == {"hello,": 1, "hello": 1}


@pytest.mark.parametrize(
    "text",
    ["A man, a plan, a canal: Panama", "No 'x' in Nixon", "12321", "x", "", "!?"],
)
def test_is_palindrome_true(text):
    assert is_palindrome(text) is True


@pytest.mark.parametrize("text", ["race a car", "ab", "12345", "hello"])
def test_is_palindrome_false(text):
    assert is_palindrome(text) is False


@pytest.mark.parametrize(
    ("name", "qty", "price", "expected"),
    [
        ("Widget", 3, "4.50", "Widget     |   3 |    4.50 |    13.50"),
        ("Gadget", 12, "0.99", "Gadget     |  12 |    0.99 |    11.88"),
        ("Pen", 1, "4.5", "Pen        |   1 |    4.50 |     4.50"),
    ],
)
def test_format_row(name, qty, price, expected):
    assert format_row(name, qty, Decimal(price)) == expected


# ------------------------------------------------------------------ 2. Numbers


def test_sum_prices_is_exact():
    # With floats, 0.1 + 0.2 == 0.30000000000000004
    assert sum_prices(["0.10", "0.20"]) == Decimal("0.30")
    assert sum_prices(["0.1"] * 10) == Decimal("1.0")
    assert sum_prices(["19.99", "5.01"]) == Decimal("25.00")


def test_sum_prices_always_returns_decimal():
    result = sum_prices([])
    assert isinstance(result, Decimal)
    assert result == 0
    assert isinstance(sum_prices(["1.25"]), Decimal)


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        ("2.675", "2.68"),
        ("2.665", "2.67"),
        ("0.125", "0.13"),  # half-even would give 0.12
        ("0.005", "0.01"),
        ("-0.125", "-0.13"),  # ties go away from zero
        ("10.994", "10.99"),
        ("10.995", "11.00"),
        ("0.004", "0.00"),
        ("2.5", "2.50"),
        ("1", "1.00"),
    ],
)
def test_round_half_up(value, expected):
    result = round_half_up(Decimal(value))
    assert isinstance(result, Decimal)
    assert str(result) == expected  # compares the string so the 2 places count


# ------------------------------------------------- 3. Truthiness and None


def test_count_missing_counts_only_none():
    assert count_missing([1, None, 0, "", None, [], False]) == 2


def test_count_missing_falsy_values_are_not_missing():
    assert count_missing([0, "", [], {}, False, 0.0]) == 0


@pytest.mark.parametrize(("values", "expected"), [([], 0), ([None] * 3, 3)])
def test_count_missing_edges(values, expected):
    assert count_missing(values) == expected


# ------------------------------------------------- 4. Slicing and unpacking


@pytest.mark.parametrize(
    ("items", "n", "expected"),
    [
        ([1, 2, 3, 4], 2, [3, 4]),
        ([1, 2, 3, 4], 1, [4]),
        ([1, 2, 3], 3, [1, 2, 3]),
        ([1, 2, 3], 10, [1, 2, 3]),
        ([], 3, []),
    ],
)
def test_last_n(items, n, expected):
    assert last_n(items, n) == expected


def test_last_n_zero_is_empty():
    # Careful: items[-0:] is the whole list, because -0 == 0
    assert last_n([1, 2, 3], 0) == []


def test_last_n_negative_raises():
    with pytest.raises(ValueError):
        last_n([1, 2, 3], -1)


def test_last_n_returns_a_new_list():
    items = [1, 2, 3]
    assert last_n(items, 3) is not items
    assert last_n(items, 99) is not items


@pytest.mark.parametrize(
    ("items", "k", "expected"),
    [
        ([1, 2, 3, 4, 5], 2, [3, 4, 5, 1, 2]),
        ([1, 2, 3, 4, 5], 0, [1, 2, 3, 4, 5]),
        ([1, 2, 3, 4, 5], 5, [1, 2, 3, 4, 5]),
        ([1, 2, 3, 4, 5], 7, [3, 4, 5, 1, 2]),
        ([1, 2, 3, 4, 5], -1, [5, 1, 2, 3, 4]),
        ([1, 2, 3, 4, 5], -6, [5, 1, 2, 3, 4]),
        ([1], 3, [1]),
        ([], 3, []),
    ],
)
def test_rotate_left(items, k, expected):
    assert rotate_left(items, k) == expected


def test_rotate_left_does_not_modify_input():
    items = [1, 2, 3]
    result = rotate_left(items, 1)
    assert items == [1, 2, 3]
    assert result is not items
    assert rotate_left(items, 0) is not items


@pytest.mark.parametrize(
    ("items", "size", "expected"),
    [
        ([1, 2, 3, 4, 5], 2, [[1, 2], [3, 4], [5]]),
        ([1, 2, 3, 4], 2, [[1, 2], [3, 4]]),
        ([1, 2], 5, [[1, 2]]),
        ([1, 2, 3], 1, [[1], [2], [3]]),
        ([], 3, []),
    ],
)
def test_chunk(items, size, expected):
    assert chunk(items, size) == expected


@pytest.mark.parametrize("size", [0, -1])
def test_chunk_rejects_bad_size(size):
    with pytest.raises(ValueError):
        chunk([1, 2, 3], size)


def test_head_tail():
    assert head_tail([1, 2, 3]) == (1, [2, 3])
    assert head_tail([7]) == (7, [])


def test_head_tail_works_on_any_iterable():
    assert head_tail((4, 5, 6)) == (4, [5, 6])
    assert head_tail(range(1, 4)) == (1, [2, 3])
    assert head_tail(iter([1, 2, 3])) == (1, [2, 3])


def test_head_tail_empty_raises_value_error():
    with pytest.raises(ValueError):
        head_tail([])


# ------------------------------------------------------------------ 5. Dicts


def test_invert_dict_groups_keys_that_share_a_value():
    assert invert_dict({"a": 1, "b": 2, "c": 1}) == {1: ["a", "c"], 2: ["b"]}


def test_invert_dict_keeps_key_order_within_each_group():
    assert invert_dict({"z": 1, "y": 1, "x": 1}) == {1: ["z", "y", "x"]}


def test_invert_dict_empty():
    assert invert_dict({}) == {}


def test_invert_dict_does_not_modify_input():
    d = {"a": 1, "b": 1}
    invert_dict(d)
    assert d == {"a": 1, "b": 1}


def test_merge_sum_adds_shared_keys():
    assert merge_sum({"a": 1, "b": 2}, {"b": 3, "c": 4}) == {"a": 1, "b": 5, "c": 4}


def test_merge_sum_with_empty_side():
    assert merge_sum({}, {"x": 1}) == {"x": 1}
    assert merge_sum({"x": 1}, {}) == {"x": 1}
    assert merge_sum({}, {}) == {}


def test_merge_sum_does_not_modify_inputs():
    a, b = {"a": 1, "b": 2}, {"b": 3}
    result = merge_sum(a, b)
    assert a == {"a": 1, "b": 2}
    assert b == {"b": 3}
    assert result is not a
    assert merge_sum(a, {}) is not a


# ------------------------------------------------------- 6. Lists and sets


def test_dedupe_keeps_first_occurrence_in_order():
    assert dedupe_preserve_order([3, 1, 3, 2, 1]) == [3, 1, 2]
    assert dedupe_preserve_order(["b", "a", "b", "c", "a"]) == ["b", "a", "c"]


def test_dedupe_empty_and_already_unique():
    assert dedupe_preserve_order([]) == []
    assert dedupe_preserve_order([1, 2, 3]) == [1, 2, 3]


def test_dedupe_accepts_any_iterable():
    assert dedupe_preserve_order(x for x in [1, 1, 2]) == [1, 2]
    assert dedupe_preserve_order("hello") == ["h", "e", "l", "o"]


def test_dedupe_uses_equality():
    # 1 == True == 1.0 and they hash the same, so they are duplicates
    assert dedupe_preserve_order([1, True, 1.0, 2]) == [1, 2]


def test_dedupe_unhashable_items_raise_type_error():
    with pytest.raises(TypeError):
        dedupe_preserve_order([[1], [1]])


def test_diff_tags():
    added, removed, kept = diff_tags(["a", "b", "c"], ["b", "c", "d", "d"])
    assert added == {"d"}
    assert removed == {"a"}
    assert kept == {"b", "c"}


def test_diff_tags_edges():
    assert diff_tags([], []) == (set(), set(), set())
    assert diff_tags(["a"], ["a"]) == (set(), set(), {"a"})
    assert diff_tags([], ["a", "b"]) == ({"a", "b"}, set(), set())
    assert diff_tags(["a", "b"], []) == (set(), {"a", "b"}, set())


def test_diff_tags_returns_sets():
    for part in diff_tags(["a"], ["b"]):
        assert isinstance(part, set)


def test_common_to_all():
    lists = [["a", "b", "c"], ["b", "c", "d"], ["c", "b"]]
    assert common_to_all(lists) == {"b", "c"}


@pytest.mark.parametrize(
    ("lists", "expected"),
    [
        ([["a", "b"]], {"a", "b"}),
        ([["a", "a"], ["a"]], {"a"}),
        ([["a"], ["b"]], set()),
        ([["a"], []], set()),
        ([], set()),
    ],
)
def test_common_to_all_edges(lists, expected):
    result = common_to_all(lists)
    assert isinstance(result, set)
    assert result == expected


# ------------------------------------------------------------- 7. Aliasing


def test_make_grid_shape_and_fill():
    assert make_grid(2, 3) == [[0, 0, 0], [0, 0, 0]]
    assert make_grid(2, 2, fill=7) == [[7, 7], [7, 7]]
    assert make_grid(0, 5) == []


def test_make_grid_rows_are_independent():
    grid = make_grid(3, 3)
    grid[0][0] = 9
    assert grid == [[9, 0, 0], [0, 0, 0], [0, 0, 0]]


def test_make_grid_rows_are_distinct_objects_even_when_empty():
    grid = make_grid(2, 0)
    assert grid == [[], []]
    assert grid[0] is not grid[1]


def test_clone_config_is_equal_but_not_the_same_object():
    config = {"ports": [80, 443], "retries": [3]}
    clone = clone_config(config)
    assert clone == config
    assert clone is not config


def test_clone_config_does_not_share_nested_lists():
    config = {"ports": [80, 443]}
    clone = clone_config(config)

    clone["ports"].append(8080)
    assert config == {"ports": [80, 443]}

    config["ports"].append(22)
    assert clone == {"ports": [80, 443, 8080]}


def test_clone_config_empty():
    assert clone_config({}) == {}
