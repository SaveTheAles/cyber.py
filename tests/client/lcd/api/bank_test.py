from cyber_sdk.client.lcd import LCDClient
from cyber_sdk.client.lcd.params import PaginationOptions

bostrom = LCDClient(
    url="https://lcd.bostrom.cybernode.ai/",
    chain_id="bostrom",
)
pagOpt = PaginationOptions(limit=2, count_total=True)


def test_balance():
    result, _ = bostrom.bank.balance(
        address="bostrom1vk20anceu6h9s00d27pjlvslz3avetkvnph7p8"
    )
    assert result.to_data()
    assert result.get("boot").amount > 0


def test_balance_with_pagination():
    result, _ = bostrom.bank.balance(
        address="bostrom1vk20anceu6h9s00d27pjlvslz3avetkvnph7p8", params=pagOpt
    )
    assert result.to_data()


def test_total():
    result, _ = bostrom.bank.total()
    assert result.to_data()


def test_total_with_pagination():
    result, _ = bostrom.bank.total(pagOpt)
    assert result.to_data()
