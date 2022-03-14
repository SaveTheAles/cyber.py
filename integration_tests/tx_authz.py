from cyber_sdk.client.lcd.api.tx import CreateTxOptions
from cyber_sdk.client.localbostrom import LocalBostrom
from cyber_sdk.core.authz import (
    MsgExecAuthorized,
    MsgGrantAuthorization,
    MsgRevokeAuthorization,
)


def main():
    bostrom = LocalBostrom()
    test1 = bostrom.wallets["test1"]

    msgG = MsgGrantAuthorization(
        granter="bostrom1x46rqay4d3cssq8gxxvqz8xt6nwlz4td20k38v",
        grantee="bostrom17lmam6zguazs5q5u6z5mmx76uj63gldnse2pdp"
        """
        grant=Grant(
            authorization=...,
            expiration=
        )
        """,
    )
    msgE = MsgExecAuthorized()
    msgR = MsgRevokeAuthorization()

    tx = test1.create_and_sign_tx(CreateTxOptions(msgs=[msgG]))
    result = bostrom.tx.broadcast(tx)
    print(f"RESULT:{result}")

    tx = test1.create_and_sign_tx(CreateTxOptions(msgs=[msgE]))
    result = bostrom.tx.broadcast(tx)
    print(f"RESULT:{result}")

    tx = test1.create_and_sign_tx(CreateTxOptions(msgs=[msgR]))
    result = bostrom.tx.broadcast(tx)
    print(f"RESULT:{result}")


main()
