from cyber_sdk.client.lcd import LCDClient

bostrom = LCDClient(
    url="https://lcd.space-pussy-1.cybernode.ai/",
    chain_id="space-pussy-1",
)


def test_parameters():
    result = bostrom.ibc_transfer.parameters()
    assert result.get("send_enabled")
    assert result.get("receive_enabled")
