import pytest

from cyber_sdk.core import Coin, Dec


def test_multiple_amount_types():
    ref = Coin("boot", 1000)
    assert ref == Coin("boot", 1000)
    assert ref == Coin("boot", "1000")


def test_deserializes_coin():
    coin = Coin.from_data({"denom": "boot", "amount": "1000"})

    assert coin.denom == "boot"
    assert coin.amount == 1000


def test_eq():
    coin1 = Coin("boot", 1000)
    coin2 = Coin("boot", 1000)
    coin3 = Coin("boot", 1001)

    assert coin1 == coin2
    assert coin1 != coin3


def test_arithmetic():

    zero = Coin("boot", 0)
    coin = Coin("boot", 1000)
    coin2 = Coin("boot", 2000)
    coin3 = Coin("ukrw", 2000)

    # addition
    sum = coin.add(coin2)
    dec_sum = coin.add(0.1)
    sum2 = coin + coin2

    assert coin.add(zero).amount == coin.amount
    assert sum.amount == 3000
    assert sum.denom == "boot"
    assert sum2.amount == 3000
    assert coin.add(1500) == Coin("boot", 2500)
    assert dec_sum.is_dec_coin()
    assert not dec_sum.is_int_coin()
    assert dec_sum.amount == Dec(1000.1)
    with pytest.raises(ArithmeticError):
        coin.add(coin3)

    # subtraction
    diff = coin2.sub(coin)
    diff2 = coin2 - coin.amount
    diff3 = coin2 - coin
    assert diff.denom == "boot"
    assert diff.amount == 1000
    assert diff2.amount == 1000
    assert diff3.amount == 1000
    with pytest.raises(ArithmeticError):
        coin2.sub(coin3)

    # multiplication
    product = coin.mul(3.1233)
    product2 = coin * 3.1233
    assert product.denom == "boot"
    assert product.amount == 3123.3
    assert product2.amount == 3123.3

    # division
    quotient = coin.div(5)
    quotient2 = coin / 5
    quotient3 = coin / 5.0
    quotient4 = coin // 3
    assert quotient.denom == "boot"
    assert quotient.amount == 200
    assert quotient2.amount == 200 and quotient2.is_int_coin()
    assert quotient3.amount == 200 and quotient3.is_dec_coin()
    assert quotient4.amount == 333 and quotient4.is_int_coin()

    # modulo
    rem = coin.mod(43)
    assert rem.denom == "boot"
    assert rem.amount == coin.amount % 43


def test_to_str():
    coin1 = Coin("boot", 123456)
    coin2 = Coin("boot", 123456.789)

    assert str(coin1) == "123456boot"
    assert str(coin1.to_dec_coin()) == "123456.0boot"
    assert str(coin2.to_dec_coin()) == "123456.789boot"


def test_from_str_parse_int_coin():
    coin1 = Coin("boot", 1001)
    coin2 = Coin.from_str("1001boot")
    assert coin1 == coin2

    coin3 = Coin("boot", -1)
    coin4 = Coin.from_str("-1boot")
    assert coin3 == coin4


def test_from_str_parse_dec_coin():
    coin1 = Coin("boot", 1001.5)
    coin2 = Coin.from_str("1001.500000000000000000boot")
    assert coin1 == coin2

    coin3 = Coin("boot", "-1.0")
    coin2 = Coin.from_str("-1.000000000000000000boot")
    assert coin2 == coin3
