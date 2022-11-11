""" done
import lcd_auth
import lcd_authz
import lcd_bank
import lcd_distribution
import lcd_gov
import lcd_liquidity
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
from cyber_sdk.client.lcd.api.tx import CreateTxOptions, SignerOptions
from cyber_sdk.client.localbostrom import LocalBostrom
from cyber_sdk.core.bank import MsgMultiSend, MsgSend, MultiSendInput, MultiSendOutput
from cyber_sdk.core.tx import SignMode
from cyber_sdk.key.key import SignOptions
from cyber_sdk.util.json import JSONSerializable

""" untested
import lcd_gov
"""

########

from cyber_sdk.core import Coin, Coins, SignDoc
from cyber_sdk.core.public_key import SimplePublicKey


def main():
    bostrom = LocalBostrom()
    wallet1 = bostrom.wallets["test1"]
    wallet2 = bostrom.wallets["test2"]
    info1 = bostrom.auth.account_info(wallet1.key.acc_address)
    info2 = bostrom.auth.account_info(wallet2.key.acc_address)

    inputs = [
        MultiSendInput(
            address=wallet1.key.acc_address,
            coins=Coins(boot=10000),
        ),
        MultiSendInput(
            address=wallet2.key.acc_address,
            coins=Coins(boot=20000),
        ),
    ]
    outputs = [
        MultiSendOutput(
            address=wallet2.key.acc_address,
            coins=Coins(boot=10000),
        ),
        MultiSendOutput(
            address=wallet1.key.acc_address,
            coins=Coins(boot=20000),
        ),
    ]

    msg = MsgMultiSend(inputs, outputs)

    opt = CreateTxOptions(msgs=[msg], memo="memo", gas_prices="0.38boot")

    tx = bostrom.tx.create(
        [
            SignerOptions(
                address=wallet1.key.acc_address, public_key=info1.get_public_key()
            ),
            SignerOptions(
                address=wallet2.key.acc_address, public_key=info2.get_public_key()
            ),
        ],
        opt,
    )

    signdoc1 = SignDoc(
        chain_id=bostrom.chain_id,
        account_number=info1.get_account_number(),
        sequence=info1.get_sequence(),
        auth_info=tx.auth_info,
        tx_body=tx.body,
    )

    signdoc2 = SignDoc(
        chain_id=bostrom.chain_id,
        account_number=info2.get_account_number(),
        sequence=info2.get_sequence(),
        auth_info=tx.auth_info,
        tx_body=tx.body,
    )
    sig1 = wallet1.key.create_signature_amino(signdoc1)
    sig2 = wallet2.key.create_signature_amino(signdoc2)
    tx.append_signatures([sig1, sig2])

    print("=======================")
    print(tx.to_data())

    result = bostrom.tx.broadcast(tx)
    print(f"RESULT:{result}")


main()
