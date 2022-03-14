import asyncio
import base64
from pathlib import Path

from cyber_sdk.client.lcd.api.tx import CreateTxOptions, SignerOptions
from cyber_sdk.client.localbostrom import LocalBostrom
from cyber_sdk.core import (
    Coins,
    LegacyAminoMultisigPublicKey,
    MultiSignature,
    SignatureV2,
    SignDoc,
)
from cyber_sdk.core.bank import MsgSend
from cyber_sdk.util.contract import get_code_id


def main():
    bostrom = LocalBostrom()
    test1 = bostrom.wallets["test1"]
    test2 = bostrom.wallets["test2"]
    test3 = bostrom.wallets["test3"]

    multisigPubKey = LegacyAminoMultisigPublicKey(
        2, [test1.key.public_key, test2.key.public_key, test3.key.public_key]
    )

    address = multisigPubKey.address()
    multisig = MultiSignature(multisigPubKey)

    msg = MsgSend(
        address,
        "bostrom1x46rqay4d3cssq8gxxvqz8xt6nwlz4td20k38v",
        Coins(boot=100000),
    )
    print(f"msgAmino:{msg.to_amino()}")

    accInfo = bostrom.auth.account_info(address)
    tx = bostrom.tx.create(
        signers=[
            SignerOptions(
                address=address,
                sequence=accInfo.get_sequence(),
                public_key=accInfo.get_public_key(),
            )
        ],
        options=CreateTxOptions(
            msgs=[msg],
            memo="memo",
            gas_prices="0.456boot",
            gas=200000,
            gas_adjustment=1.2,
        ),
    )
    signDoc = SignDoc(
        chain_id=bostrom.chain_id,
        account_number=accInfo.get_account_number(),
        sequence=accInfo.get_sequence(),
        auth_info=tx.auth_info,
        tx_body=tx.body,
    )
    print("----")
    print(signDoc.to_amino_json())
    print("----")

    sig1 = test3.key.create_signature_amino(signDoc)
    sig2 = test2.key.create_signature_amino(signDoc)

    multisig.append_signature_v2s([sig1, sig2])
    sig_v2 = SignatureV2(
        public_key=multisigPubKey,
        data=multisig.to_signature_descriptor(),
        sequence=accInfo.get_sequence(),
    )
    tx.append_signatures([sig_v2])

    print(tx.to_proto())

    print("-" * 32)
    print(tx.to_proto().SerializeToString())
    print("-" * 32)
    result = bostrom.tx.broadcast(tx)
    print(result)


main()
