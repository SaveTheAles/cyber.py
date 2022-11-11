from cyber_sdk.client.lcd import LCDClient
from cyber_sdk.core.bech32 import is_acc_address

bostrom = LCDClient(
    url="https://lcd.bostrom.cybernode.ai/",
    chain_id="bostrom",
)


def test_rewards():
    result = bostrom.distribution.rewards("bostrom1x46rqay4d3cssq8gxxvqz8xt6nwlz4td20k38v")
    assert result.total.to_data()


def test_validator_commission():
    result = bostrom.distribution.validator_commission(
        "bostromvaloper19ne0aqltndwxl0n32zyuglp2z8mm3nu0gxpfaw"
    )
    assert result.to_data()


def test_withdraw_address():
    result = bostrom.distribution.withdraw_address(
        "bostrom1x46rqay4d3cssq8gxxvqz8xt6nwlz4td20k38v"
    )
    assert is_acc_address(result)


def test_comminity_pool():
    result = bostrom.distribution.community_pool()
    assert result.to_data()


def test_parameters():
    result = bostrom.distribution.parameters()
    assert result.get("community_tax")
    assert result.get("base_proposer_reward")
    assert result.get("bonus_proposer_reward")
    assert result.get("withdraw_addr_enabled")
