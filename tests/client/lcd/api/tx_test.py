from cyber_sdk.client.lcd import LCDClient
from cyber_sdk.client.lcd.params import PaginationOptions

bostrom = LCDClient(
    url="https://lcd.bostrom.cybernode.ai/",
    chain_id="bostrom",
)

pagOpt = PaginationOptions(limit=2, count_total=True)


def test_tx_info():
    result = bostrom.tx.tx_info(
        "23AEDC95A3992E673111AFF899F0C98B46B6E408F8663758F1E492ADB8882D99"
    )
    assert result is not None


def test_search():
    result = bostrom.tx.search(
        [
            ["tx.height", 1674816],
            ["message.sender", "bostrom1udal5nr3lz7mg7j7k79se4rz0tsjj8lur45q99"],
        ]
    )
    assert result is not None
    assert len(result) > 0


def test_tx_infos_by_height():
    result = bostrom.tx.tx_infos_by_height()
    assert result is not None


def test_tx_infos_by_height_with_height():
    result = bostrom.tx.tx_infos_by_height(1674816)
    assert result is not None
