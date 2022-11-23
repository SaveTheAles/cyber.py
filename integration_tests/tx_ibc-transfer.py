from cyber_sdk.client.lcd import LCDClient, PaginationOptions
from cyber_sdk.client.lcd.api.tx import CreateTxOptions
from cyber_sdk.core import Coin, Coins
from cyber_sdk.core.ibc import Height
from cyber_sdk.core.ibc_transfer import MsgTransfer
from cyber_sdk.exceptions import LCDResponseError
from cyber_sdk.key.mnemonic import MnemonicKey
from cyber_sdk.util.contract import get_code_id


def main():
    bostrom = LCDClient(
        url="https://lcd.bostrom.cybernode.ai/",
        chain_id="bostrom",
    )

    key = MnemonicKey(
        mnemonic="notice oak worry limit wrap speak medal online prefer cluster roof addict wrist behave treat actual wasp year salad speed social layer crew genius"
    )

    wallet = bostrom.wallet(key=key)

    signedTx = wallet.create_and_sign_tx(
        CreateTxOptions(
            msgs=[
                MsgTransfer(
                    source_port="transfer",
                    source_channel="channel-9",
                    token="10000boot",
                    sender="bostrom1x46rqay4d3cssq8gxxvqz8xt6nwlz4td20k38v",
                    receiver="bostrom17lmam6zguazs5q5u6z5mmx76uj63gldnse2pdp",
                    timeout_height=Height(revision_number=0, revision_height=10000),
                    timeout_timestamp=0,
                )
            ]
        )
    )
    try:
        result = bostrom.tx.broadcast(signedTx)
    except LCDResponseError as err:
        print("err: ", err)
    else:
        print("err..")

    print(result)


main()
