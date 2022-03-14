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
from cyber_sdk.client.lcd.api.tx import CreateTxOptions, SignerOptions

# import lcd_tx
from cyber_sdk.client.localbostrom import LocalBostrom
from cyber_sdk.core import Coin, Coins
from cyber_sdk.core.bank import MsgSend
from cyber_sdk.core.tx import SignMode
from cyber_sdk.key.key import SignOptions
from cyber_sdk.key.mnemonic import MnemonicKey


def main():
    bostrom = LCDClient(
        url="https://lcd.space-pussy-1.cybernode.ai/",
        chain_id="space-pussy-1",
    )
    key = MnemonicKey(
        mnemonic='develop sail resist join lumber door door jelly apology trap note seek gentle bamboo enough concert exhibit disorder turn soul bullet cash debris wire'
    )
    test1 = bostrom.wallet(key=key)

    msg = MsgSend(
        "bostrom1udal5nr3lz7mg7j7k79se4rz0tsjj8lur45q99",
        "bostrom1hmkqhy8ygl6tnl5g8tc503rwrmmrkjcq3lduwj",
        Coins(boot=1),
    )
    print(msg)
    tx = test1.create_and_sign_tx(
        CreateTxOptions(
            msgs=[msg],
            gas_prices="0.1boot",
            gas="80000",  # gas="auto", gas_adjustment=1.1
        )
    )
    print(tx)

    result = bostrom.tx.broadcast(tx)
    print(result)


main()
