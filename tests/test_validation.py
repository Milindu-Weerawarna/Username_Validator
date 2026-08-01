"""Tests for username validation."""

from sliit_utils import validate_username


def test_accepts_valid_username():
    assert validate_username("milindu") == (True, None)


def test_rejects_empty_username():
    assert validate_username("") == (False, "Username is required")


def test_rejects_whitespace_only_username():
    assert validate_username("   ") == (False, "Username is required")


def test_rejects_short_username():
    valid, message = validate_username("ab")

    assert valid is False
    assert "at least 3 characters" in message


def test_rejects_non_string_username():
    assert validate_username(None) == (False, "Username must be a string")
