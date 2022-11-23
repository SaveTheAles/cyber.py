from cyber_sdk.client.lcd import LCDClient

bostrom = LCDClient(
    url="https://lcd.bostrom.cybernode.ai/",
    chain_id="bostrom",
)


def test_inflation():
    result = bostrom.mint.inflation()
    print(result.to_data())


def test_annual_provisions():
    result = bostrom.mint.annual_provisions()
    print(result.to_data())


def test_parameters():
    result = bostrom.mint.parameters()
    print(result.get("mint_denom"))
    print(result.get("inflation_rate_change"))
    print(result.get("inflation_max"))
    print(result.get("inflation_min"))
    print(result.get("goal_bonded"))
    print(result.get("blocks_per_year"))
