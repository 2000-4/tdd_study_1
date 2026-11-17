MENU = {"아메리카노": 4500, "라떼": 5000, "샌드위치": 6500}
BASE_FEE = 2000
BASE_KM = 2
EXTRA_FEE_PER_KM = 500


def menu_price(name):
    if name not in MENU:
        raise ValueError("없는 메뉴입니다: " + name)
    return MENU[name]


def apply_discount(total):
    if total >= 50000:
        return total - total // 5
    if total >= 20000:
        return total - total // 10
    return total


def order_total(items):
    if len(items) > 10:
        raise ValueError("한 번에 10개까지만 주문할 수 있습니다")
    total = 0
    for name in items:
        total += menu_price(name)
    return apply_discount(total)


def delivery_fee(distance_km):
    if distance_km < 0:
        raise ValueError("거리는 0 이상이어야 합니다")
    if distance_km <= BASE_KM:
        return BASE_FEE
    return BASE_FEE + (distance_km - BASE_KM) * EXTRA_FEE_PER_KM

def apply_coupon(total, code) :
    if code == "WELCOME" :
        discount = 3000
    elif code == "HALF" :
        discount = min(total // 2, 5000) # 5000원과 total //2, 중에 더 작은 값을 사용
    
    else :
        raise ValueError("없는 코드 값입니다.")
    return max(total - discount, 0) # total - discount와 0 중에 큰 값으로 돌려준다 (할인값)


