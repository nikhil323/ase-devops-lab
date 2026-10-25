import pytest

from app.price import parse_price


def test_normal_price():
    assert parse_price("$499.99") == 499.99


def test_price_with_comma():
    assert parse_price("$1,299.99") == 1299.99


def test_price_without_cents():
    assert parse_price("$25") == 25.0


def test_price_with_currency_and_spaces():
    assert parse_price("  $89.50 CAD ") == 89.50


def test_bad_input_raises_error():
    with pytest.raises(ValueError):
        parse_price("Out of stock")


def test_empty_input_raises_error():
    with pytest.raises(ValueError):
        parse_price("")
