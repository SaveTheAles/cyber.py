from cyber_sdk.client.lcd import LCDClient

bostrom = LCDClient(
    url="https://lcd.bostrom.cybernode.ai/",
    chain_id="bostrom",
)


def test_code_info():
    result = bostrom.wasm.code_info(3)
    assert result is not None


def test_contract_info():
    result = bostrom.wasm.contract_info("bostrom1p4gg3p2ue6qy2qfuxtrmgv2ec3f4jmgqtazum8")
    assert result is not None


def test_contract_query():
    result = bostrom.wasm.contract_query(
        "bostrom1p4gg3p2ue6qy2qfuxtrmgv2ec3f4jmgqtazum8",
        {"prices": {}},
    )
    assert result is not None


def test_parameters():
    result = bostrom.wasm.parameters()
    assert result.get("max_contract_size")
    assert result.get("max_contract_gas")
    assert result.get("max_contract_msg_size")
