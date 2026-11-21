import pytest

from main import Account, print_choices_unauth, print_choices_auth


# replace Python's input with a function that returns "x", then "q".
def test_auth_menu_invalid_then_quit_returns_2(monkeypatch):
    answers = iter(  # iter(...) wraps the list in an iterator. Object that hands out one item at a time and remembers where it left off.
        [
            "x",
            "q",
        ]  # A list which is iterable. Every loop over starts again from the beginning.
    )  # iterator object from an iterable so you can traverse its values one by one.
    monkeypatch.setattr("builtins.input", lambda _prompt="": next(answers))
    result = print_choices_auth()
    assert result == 2
