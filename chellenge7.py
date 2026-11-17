import pytest

from order import best_coupon_price


def test_no_stacking_coupons():
    # 1. 두 쿠폰을 연달아 중복 적용하지 않음 (HALF만 적용한 5000이 최선)
    assert best_coupon_price(10000, ["WELCOME", "HALF"]) == 5000


def test_half_discount_cap_at_5000():
    # 2. HALF의 최대 할인 한도(5000원)를 지킴 (30000 - 5000 = 25000)
    assert best_coupon_price(30000, ["WELCOME", "HALF"]) == 25000


def test_welcome_is_better_for_small_order():
    # 3. WELCOME(1000원)이 HALF(2000원)보다 더 유리한 경우
    assert best_coupon_price(4000, ["WELCOME", "HALF"]) == 1000


def test_price_never_goes_below_zero():
    # 4. 결제금액 하한은 0원
    assert best_coupon_price(2000, ["WELCOME", "HALF"]) == 0


def test_empty_codes_returns_original_total():
    # 5. 후보가 없으면 원래 금액 반환
    assert best_coupon_price(10000, []) == 10000


def test_case_insensitive_code():
    # 6. 소문자 코드도 대문자와 동일하게 처리
    assert best_coupon_price(10000, ["welcome"]) == 7000


def test_order_of_codes_does_not_matter():
    # 7. 후보 순서를 뒤집어도 결과가 같음
    assert best_coupon_price(10000, ["HALF", "WELCOME"]) == best_coupon_price(
        10000, ["WELCOME", "HALF"]
    )


def test_invalid_code_checked_even_after_zero_price():
    # 8. 앞의 쿠폰으로 0원이 됐더라도 뒤의 잘못된 코드를 검사해 ValueError 발생
    with pytest.raises(ValueError):
        best_coupon_price(2000, ["WELCOME", "FREE"])

def apply_coupon(total, code):
    if total < 0:
        raise ValueError("금액은 0 이상이어야 합니다")

    normalized = code.upper()
    if normalized == "WELCOME":
        discount = 3000
    elif normalized == "HALF":
        discount = min(total // 2, 5000)
    else:
        raise ValueError("없는 코드 값입니다: " + code)

    return max(total - discount, 0)


def best_coupon_price(total, codes):
    if total < 0:
        raise ValueError("금액은 0 이상이어야 합니다")
    if not codes:
        return total

    best = total
    for code in codes:
        price = apply_coupon(total, code)
        if price < best:
            best = price
    return best