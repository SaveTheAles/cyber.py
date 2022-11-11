import asyncio
import base64
from pathlib import Path

from cyber_sdk.client.lcd import LCDClient
from cyber_sdk.client.lcd.api.tx import CreateTxOptions
from cyber_sdk.core import Coins
from cyber_sdk.core.bank import MsgSend
from cyber_sdk.core.wasm import MsgExecuteContract
from cyber_sdk.core.tx import SignMode
from cyber_sdk.key.mnemonic import MnemonicKey


bostrom = LCDClient(
    url="https://lcd.bostrom.cybernode.ai/",
    chain_id="bostrom",
)
key = MnemonicKey(
    mnemonic='develop sail resist join lumber door door jelly apology trap note seek gentle bamboo enough concert exhibit disorder turn soul bullet cash debris wire'
)
test1 = bostrom.wallet(key=key)

contract_msg = {
    "create_passport": {"nickname": "bostrompytest", "avatar": "QmfGPoU364TK3T2UxDdJKXVuzTrGhAcfCT7v8Cx8QmoWvv"}}


msg = MsgExecuteContract(
    sender='bostrom1udal5nr3lz7mg7j7k79se4rz0tsjj8lur45q99',
    contract='bostrom1hxwv9eu9duxkuvluunxlayy9dhzwtm3e84fx47suf5jju04gumsqx7afgz',
    execute_msg=contract_msg)
print(msg)
tx = test1.create_and_sign_tx(
    CreateTxOptions(
        msgs=[msg],
        gas_prices="0.1boot",
        gas="500000",  # gas="auto", gas_adjustment=1.1
    )
)
print(tx)

result = bostrom.tx.broadcast(tx)
print(result)

