from cyber_sdk.client.lcd import LCDClient
from cyber_sdk.client.lcd.api.tx import CreateTxOptions
from cyber_sdk.client.localbostrom import LocalBostrom
from cyber_sdk.core.liquidity import MsgSwapWithinBatch
from cyber_sdk.core.tx import SignMode
from cyber_sdk.util.json import JSONSerializable

""" untested
import lcd_gov
"""

########

from cyber_sdk.core import Coin, Coins
from cyber_sdk.core.public_key import SimplePublicKey


def main():
    bostrom = LocalBostrom()
    test1 = bostrom.wallets["test1"]

    msg = MsgSwapWithinBatch(
        swap_requester_address="bostrom1x46rqay4d3cssq8gxxvqz8xt6nwlz4td20k38v",
        offer_coin=Coin.parse("1000000boot"),
        ask_denom="hydrogen",
    )

    opt = CreateTxOptions(msgs=[msg], memo="send test")
    # tx = test1.create_tx(opt)
    tx = test1.create_and_sign_tx(opt)
    print("SIGNED TX", tx)

    result = bostrom.tx.broadcast(tx)
    print(f"RESULT:{result}")


main()
