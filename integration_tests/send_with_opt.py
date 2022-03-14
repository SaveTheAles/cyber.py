import asyncio
import base64
from pathlib import Path

from cyber_sdk.client.lcd.api.tx import BroadcastOptions
from cyber_sdk.client.localbostrom import LocalBostrom
from cyber_sdk.core import Coins
from cyber_sdk.core.bank import MsgSend
from cyber_sdk.util.contract import get_code_id


def main():
    bostrom = LocalBostrom()
    test1 = bostrom.wallets["test1"]

    print(test1)
    msg = MsgSend(
        "bostrom1x46rqay4d3cssq8gxxvqz8xt6nwlz4td20k38v",
        "bostrom17lmam6zguazs5q5u6z5mmx76uj63gldnse2pdp",
        Coins(boot=1000000),
    )
    print(msg)
    tx = test1.create_and_sign_tx(msgs=[msg])
    print(tx)

    opt = BroadcastOptions(
        sequences=[58], fee_granter="bostrom1x46rqay4d3cssq8gxxvqz8xt6nwlz4td20k38v"
    )

    result = bostrom.tx.broadcast(tx, opt)
    print(result)


main()
