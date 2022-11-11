from cyber_sdk.client.lcd import LCDClient

bostrom = LCDClient(chain_id="bostrom", url="https://lcd.bostrom.cybernode.ai/")


def test_validators_with_voting_power():
    validators_with_voting_power = bostrom.utils.validators_with_voting_power()
    print(validators_with_voting_power)
    assert validators_with_voting_power is not None
