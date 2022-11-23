from cyber_sdk.client.lcd import LCDClient

bostrom = LCDClient(
    url="https://lcd.bostrom.cybernode.ai/",
    chain_id="bostrom",
)


def test_parameters():
    result = bostrom.ibc_transfer.parameters()
    assert result.get("send_enabled")
    assert result.get("receive_enabled")
