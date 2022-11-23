import asyncio
import base64
from pathlib import Path

from cyber_sdk.client.lcd import LCDClient
from cyber_sdk.client.lcd.api.tx import CreateTxOptions
from cyber_sdk.client.localbostrom import LocalBostrom
from cyber_sdk.core import Coins
from cyber_sdk.core.liquidity import MsgSwapWithinBatch
from cyber_sdk.key.mnemonic import MnemonicKey


def main():
    bostrom = LCDClient(
        chain_id="bostrom",
        url="https://lcd.bostrom.cybernode.ai/",
    )
    key = MnemonicKey(
        mnemonic="notice oak worry limit wrap speak medal online prefer cluster roof addict wrist behave treat actual wasp year salad speed social layer crew genius"
    )

    test1 = bostrom.wallet(key=key)

    print(test1)
    msg = MsgSwapWithinBatch(
        swap_requester_address="bostrom1x46rqay4d3cssq8gxxvqz8xt6nwlz4td20k38v",
        offer_coin="100000boot",
        ask_denom="uusd",
    )
    print(msg)
    tx = test1.create_and_sign_tx(
        CreateTxOptions(msgs=[msg], gas_prices="0.2boot", gas_adjustment="1.4")
    )
    print(tx)

    result = bostrom.tx.broadcast(tx)
    print(result)


main()
