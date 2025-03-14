from cyber_sdk.client.lcd import LCDClient, PaginationOptions

bostrom = LCDClient(
    url="https://lcd.bostrom.cybernode.ai/",
    chain_id="bostrom",
)


def test_account_info():
    result = bostrom.auth.account_info("bostrom1x46rqay4d3cssq8gxxvqz8xt6nwlz4td20k38v")

    assert result.address == "bostrom1x46rqay4d3cssq8gxxvqz8xt6nwlz4td20k38v"
    assert result.account_number == 1165
