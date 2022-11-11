from cyber_sdk.client.lcd import LCDClient

bostrom = LCDClient(
    url="https://lcd.bostrom.cybernode.ai/",
    chain_id="bostrom",
)


def test_exchange_rates():
    result = bostrom.oracle.exchange_rates()
    assert result is not None


def test_exchange_rate():
    result = bostrom.oracle.exchange_rate("ukrw")
    assert result is not None


def test_active_denoms():
    result = bostrom.oracle.active_denoms()
    assert result is not None


def test_feeder_address():
    result = bostrom.oracle.feeder_address(
        "bostromvaloper19ne0aqltndwxl0n32zyuglp2z8mm3nu0gxpfaw"
    )
    assert result is not None


def test_misses():
    result = bostrom.oracle.misses("bostromvaloper19ne0aqltndwxl0n32zyuglp2z8mm3nu0gxpfaw")
    assert result is not None


def test_aggregate_prevote():
    result = bostrom.oracle.aggregate_prevote(
        "bostromvaloper19ne0aqltndwxl0n32zyuglp2z8mm3nu0gxpfaw"
    )
    assert result is not None


# def test_aggregate_vote():
#    result = bostrom.oracle.aggregate_vote(
#        "bostromvaloper19ne0aqltndwxl0n32zyuglp2z8mm3nu0gxpfaw"
#    )
#    assert(result is not None)


def test_parameters():
    result = bostrom.oracle.parameters()
    assert result.get("vote_period")
    assert result.get("vote_threshold")
    assert result.get("reward_band")
    assert result.get("reward_distribution_window")
    assert result.get("whitelist")
    assert len(result.get("whitelist")) > 0
    assert result.get("slash_fraction")
    assert result.get("slash_window")
    assert result.get("min_valid_per_window")
