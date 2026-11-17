import pytest
from order import order_total
# 테스트 코드, 코드 기술 명세서


def test_small_order_has_no_discount():
    assert order_total(["아메리카노", "라떼"]) == 9500


def test_big_order_gets_discount():
    assert order_total(["샌드위치", "샌드위치", "샌드위치", "라떼"]) == 22050


def test_exactly_20000_gets_discount():
    assert order_total(["라떼", "라떼", "라떼", "라떼"]) == 18000

def test_empty_order_is_zero() :
    assert order_total([]) == 0
    
def test_unknown_menu_raises_error():
    with pytest.raises(ValueError):
        order_total(["콜라"])

def test_ten_items_is_ok():
    assert order_total(["아메리카노"] * 10) == 40500

def test_eleven_items_raises_error():
    with pytest.raises(ValueError):
        order_total(["아메리카노"] * 11)

def test_exactly_50000_gets_20_percent():
    assert order_total(["라떼"] * 10) == 40000
        

test_small_order_has_no_discount()