import pytest

from order import delivery_fee


def test_short_distance_is_base_fee():
    assert delivery_fee(1) == 2000


def test_two_km_is_still_base_fee():
    assert delivery_fee(2) == 2000


def test_long_distance_adds_500_per_km():
    assert delivery_fee(5) == 3500


def test_negative_distance_raises_error():
    with pytest.raises(ValueError):
        delivery_fee(-3)