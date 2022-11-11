from cyber_sdk.client.lcd import LCDClient
from cyber_sdk.core import Coin

bostrom = LCDClient(
    url="https://lcd.bostrom.cybernode.ai/",
    chain_id="bostrom",
)


def test_swap_rate():
    result = bostrom.liquidity.swap_rate(Coin.parse("10000boot"), "hydrogen")
    assert result is not None


def test_pool_delta():
    result = bostrom.liquidity.bostrom_pool_delta()
    assert result is not None


def test_parameters():
    result = bostrom.liquidity.parameters()
    assert result.get("base_pool")
    assert result.get("pool_recovery_period")
    assert result.get("min_stability_spread")
