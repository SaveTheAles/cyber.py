from cyber_sdk.client.lcd import LCDClient

bostrom = LCDClient(
    url="https://lcd.bostrom.cybernode.ai/",
    chain_id="bostrom",
)


def test_parameters():
    result = bostrom.ibc.parameters()
    assert result.get("allowed_clients")
