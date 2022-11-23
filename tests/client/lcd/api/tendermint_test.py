from cyber_sdk.client.lcd import LCDClient

bostrom = LCDClient(
    url="https://lcd.bostrom.cybernode.ai/",
    chain_id="bostrom",
)


def test_validator_set():
    result = bostrom.tendermint.validator_set()
    print(result)


def test_validator_set_with_height():
    result = bostrom.tendermint.validator_set(6740000)
    print(result)


def test_node_info():
    result = bostrom.tendermint.node_info()
    assert result["default_node_info"]["network"] == "bombay-12"


def test_block_info():
    result = bostrom.tendermint.block_info()
    print(result["block"]["header"]["height"])


def test_block_info_with_height():
    result = bostrom.tendermint.block_info(6740000)
    print(result)


def test_syncing():
    result = bostrom.tendermint.syncing()
    print(result)
