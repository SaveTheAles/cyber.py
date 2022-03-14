from cyber_sdk.client.lcd.api.tx import CreateTxOptions
from cyber_sdk.client.localbostrom import LocalBostrom
from cyber_sdk.core import Coin, Coins
from cyber_sdk.core.distribution import (
    MsgFundCommunityPool,
    MsgSetWithdrawAddress,
    MsgWithdrawDelegationReward,
    MsgWithdrawValidatorCommission,
)


def main():
    bostrom = LocalBostrom()
    test1 = bostrom.wallets["test1"]
    validator = bostrom.wallets["validator"]

    msgFund = MsgFundCommunityPool(
        depositor="bostrom1x46rqay4d3cssq8gxxvqz8xt6nwlz4td20k38v",
        amount=Coins("1000000uusd,1000000ukrw"),
    )
    msgSet = MsgSetWithdrawAddress(
        delegator_address="bostrom1x46rqay4d3cssq8gxxvqz8xt6nwlz4td20k38v",
        withdraw_address="bostrom1av6ssz7k4xpc5nsjj2884nugakpp874ae0krx7",
    )
    msgWCom = MsgWithdrawValidatorCommission(
        validator_address="bostromvaloper1dcegyrekltswvyy0xy69ydgxn9x8x32zdy3ua5"
    )
    msgWDel = MsgWithdrawDelegationReward(
        delegator_address="bostrom1x46rqay4d3cssq8gxxvqz8xt6nwlz4td20k38v",
        validator_address="bostromvaloper1dcegyrekltswvyy0xy69ydgxn9x8x32zdy3ua5",
    )

    tx = test1.create_and_sign_tx(CreateTxOptions(msgs=[msgFund]))
    result = bostrom.tx.broadcast(tx)
    print(f"RESULT:{result}")

    tx = test1.create_and_sign_tx(CreateTxOptions(msgs=[msgSet]))
    result = bostrom.tx.broadcast(tx)
    print(f"RESULT:{result}")

    tx = test1.create_and_sign_tx(CreateTxOptions(msgs=[msgWDel]))
    result = bostrom.tx.broadcast(tx)
    print(f"RESULT:{result}")

    tx = validator.create_and_sign_tx(CreateTxOptions(msgs=[msgWCom]))
    result = bostrom.tx.broadcast(tx)
    print(f"RESULT:{result}")


main()
