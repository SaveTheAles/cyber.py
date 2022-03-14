from cyber_sdk.client.lcd import LCDClient
from cyber_sdk.core import Coin

bostrom = LCDClient(
    url="https://lcd.space-pussy-1.cybernode.ai/",
    chain_id="space-pussy-1",
)


def test_swap_rate():
    result = bostrom.market.swap_rate(Coin.parse("10000boot"), "uusd")
    assert result is not None


def test_pool_delta():
    result = bostrom.market.bostrom_pool_delta()
    assert result is not None


def test_parameters():
    result = bostrom.market.parameters()
    assert result.get("base_pool")
    assert result.get("pool_recovery_period")
    assert result.get("min_stability_spread")
