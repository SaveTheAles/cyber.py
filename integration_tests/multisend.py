""" done
import lcd_auth
import lcd_authz
import lcd_bank
import lcd_distribution
import lcd_gov
import lcd_market
import lcd_mint
import lcd_oracle
import lcd_slashing
import lcd_wasm
import lcd_treasury
import lcd_tendermint
import lcd_ibc
import lcd_ibc_transfer

"""

from cyber_sdk.client.lcd import LCDClient

# import lcd_tx
from cyber_sdk.client.lcd.api.tx import CreateTxOptions
from cyber_sdk.client.localbostrom import LocalBostrom
from cyber_sdk.core.bank import MsgMultiSend, MsgSend, MultiSendInput, MultiSendOutput
from cyber_sdk.core.tx import SignMode
from cyber_sdk.key.mnemonic import MnemonicKey
from cyber_sdk.util.json import JSONSerializable

""" untested
import lcd_gov
"""

########

from cyber_sdk.core import Coin, Coins
from cyber_sdk.core.public_key import SimplePublicKey


def main():
    bostrom = LCDClient(
        url="https://lcd.space-pussy-1.cybernode.ai/",
        chain_id="space-pussy-1",
    )
    key = MnemonicKey(
        mnemonic="notice oak worry limit wrap speak medal online prefer cluster roof addict wrist behave treat actual wasp year salad speed social layer crew genius"
    )
    test1 = bostrom.wallet(key=key)

    msg = MsgSend(
        "bostrom1x46rqay4d3cssq8gxxvqz8xt6nwlz4td20k38v",
        "bostrom17lmam6zguazs5q5u6z5mmx76uj63gldnse2pdp",
        Coins(boot=30000),
    )
    inputs = [
        MultiSendInput(
            address="bostrom1x46rqay4d3cssq8gxxvqz8xt6nwlz4td20k38v",
            coins=Coins(boot=30000),
        )
    ]
    outputs = [
        MultiSendOutput(
            address="bostrom17lmam6zguazs5q5u6z5mmx76uj63gldnse2pdp",
            coins=Coins(boot=10000),
        ),
        MultiSendOutput(
            address="bostrom1av6ssz7k4xpc5nsjj2884nugakpp874ae0krx7",
            coins=Coins(boot=20000),
        ),
    ]
    msgMulti = MsgMultiSend(inputs, outputs)

    opt = CreateTxOptions(
        msgs=[msg, msgMulti], memo="send test", gas_adjustment=1.5, gas_prices="1boot"
    )
    # tx = test1.create_tx(opt)
    tx = test1.create_and_sign_tx(opt)
    print("SIGNED TX", tx)

    result = bostrom.tx.broadcast(tx)
    print(f"RESULT:{result}")


main()
