summ = int(input())

def all_sums(summ):
    # Половина
    half = summ/2
    # Четверть
    quarter = summ / 4
    # Десятая часть
    decimal = round(0.1 * summ, 1)
    return half, quarter, decimal

def test_all_sums():
    sm = 12
    a, b, c = all_sums(sm)
    v1, v2, v3 = 6, 3, 1.2
    assert a == v1
    assert b == v2
    assert c == v3



a, b, c = all_sums(summ)

print("Половина", a)
print("Четверть", b)
print("Десятая", c)
