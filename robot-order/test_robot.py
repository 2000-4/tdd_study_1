from robot import can_deliver

def test_least_20_battery_distance() : # battery, distance_km
    assert can_deliver(100, 8) == True
    
def test_least_19_battery_distance() :
    assert can_deliver(99, 8) == False

def test_is_enough_to_return_battery_left() :
    assert can_deliver(80, 3) == True

def test_is_not_enough_to_return_battery_left() :
    assert can_deliver(19, 0) == False
    assert can_deliver(20, 0) == True
    
def test_is_oneway_distance_check_km() :
    assert can_deliver(60, 5) == False
    
def test_km_is_more_big_then_battery():
    assert can_deliver(30, 5) == False

# def test_is_enough_battert_left() :
#     assert can_deliver(100, 100) == True