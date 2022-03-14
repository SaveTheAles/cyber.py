import base64

from cyber_sdk.client.lcd.api.tx import CreateTxOptions
from cyber_sdk.client.localbostrom import LocalBostrom
from cyber_sdk.core import Coin, Coins, ValConsPubKey
from cyber_sdk.core.staking import (
    CommissionRates,
    Description,
    MsgBeginRedelegate,
    MsgCreateValidator,
    MsgDelegate,
    MsgEditValidator,
    MsgUndelegate,
)


def main():
    bostrom = LocalBostrom()
    test1 = bostrom.wallets["test1"]
    """
    msgCV = MsgCreateValidator(
        description=Description(moniker="testval_1"),
        commission=CommissionRates(rate="0.01", max_rate="0.1", max_change_rate="0.01"),
        min_self_delegation=1,
        delegator_address="bostrom1x46rqay4d3cssq8gxxvqz8xt6nwlz4td20k38v",
        validator_address="bostromvalcons1mgp3028ry5wf464r3s6gyptgmngrpnelhkuyvm",
        pubkey=ValConsPubKey(),
        value="10000000uusd"
    )

    tx = test1.create_and_sign_tx(CreateTxOptions(msgs=[msgCV]))
    result = bostrom.tx.broadcast(tx)
    print(f"RESULT:{result}")
    
    """

    msgEV = MsgEditValidator(
        validator_address="",
        description=Description(moniker="testval_1"),
        commission=CommissionRates(rate="0.02", max_rate="0.1", max_change_rate="0.01"),
        min_self_delegation=1,
    )

    msgDel = MsgDelegate(
        validator_address="bostromvaloper1dcegyrekltswvyy0xy69ydgxn9x8x32zdy3ua5",
        delegator_address="bostrom1x46rqay4d3cssq8gxxvqz8xt6nwlz4td20k38v",
        amount="10000000boot",
    )
    msgRedel = MsgBeginRedelegate(
        validator_dst_address="bostromvaloper1dcegyrekltswvyy0xy69ydgxn9x8x32zdy3ua5",
        validator_src_address="bostromvaloper1dcegyrekltswvyy0xy69ydgxn9x8x32zdy3ua5",
        delegator_address="bostrom1x46rqay4d3cssq8gxxvqz8xt6nwlz4td20k38v",
        amount=Coin.parse("1000000boot"),
    )

    msgUndel = MsgUndelegate(
        validator_address="bostromvaloper1dcegyrekltswvyy0xy69ydgxn9x8x32zdy3ua5",
        delegator_address="bostrom1x46rqay4d3cssq8gxxvqz8xt6nwlz4td20k38v",
        amount=Coin.parse("10000000boot"),
    )

    """

    tx = test1.create_and_sign_tx(CreateTxOptions(msgs=[msgEV]))
    result = bostrom.tx.broadcast(tx)
    print(f"RESULT:{result}")
    """

    tx = test1.create_and_sign_tx(CreateTxOptions(msgs=[msgDel]))
    result = bostrom.tx.broadcast(tx)
    print(f"RESULT:{result}")

    tx = test1.create_and_sign_tx(CreateTxOptions(msgs=[msgRedel]))
    result = bostrom.tx.broadcast(tx)
    print(f"RESULT:{result}")

    tx = test1.create_and_sign_tx(CreateTxOptions(msgs=[msgUndel]))
    result = bostrom.tx.broadcast(tx)
    print(f"RESULT:{result}")


main()
