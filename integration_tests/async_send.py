import asyncio

import uvloop

from cyber_sdk.client.lcd import AsyncLCDClient
from cyber_sdk.client.lcd.api.tx import CreateTxOptions
from cyber_sdk.core import Coins
from cyber_sdk.core.bank import MsgSend
from cyber_sdk.key.mnemonic import MnemonicKey


async def with_sem(aw, sem):
    async with sem:
        print(sem)
        return await aw


async def main():
    bostrom = AsyncLCDClient(chain_id="space-pussy-1", url="https://lcd.space-pussy-1.cybernode.ai/")
    mk = MnemonicKey(
        mnemonic="index light average senior silent limit usual local involve delay update rack cause inmate wall render magnet common feature laundry exact casual resource hundred"
    )
    awallet = bostrom.wallet(mk)

    msg = MsgSend(
        "bostrom1333veey879eeqcff8j3gfcgwt8cfrg9mq20v6f",
        "bostrom17lmam6zguazs5q5u6z5mmx76uj63gldnse2pdp",
        Coins(boot=20),
    )
    print(msg)
    tx = await awallet.create_and_sign_tx(
        CreateTxOptions(
            msgs=[msg],
            gas_prices="0.15boot",
            gas="63199",  # gas="auto", gas_adjustment=1.1
            fee_denoms=["boot"],
        )
    )
    print(tx)

    result = await bostrom.tx.broadcast(tx)
    print(result)
    await bostrom.session.close()


uvloop.install()
asyncio.run(main())
