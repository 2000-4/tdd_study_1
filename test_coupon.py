import pytest

from order import apply_coupon


def test_welcome_takes_off_3000():
    assert apply_coupon(10000, "WELCOME") == 7000
    
    


def test_half_takes_off_half():
    assert apply_coupon(8000, "HALF") == 4000


def test_half_discount_is_at_most_5000():
    assert apply_coupon(30000, "HALF") == 25000


def test_price_never_goes_below_zero():
    assert apply_coupon(2000, "WELCOME") == 0


def test_unknown_code_raises_error():
    with pytest.raises(ValueError):
        apply_coupon(10000, "FREE")
        