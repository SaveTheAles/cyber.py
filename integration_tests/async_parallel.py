import asyncio

import uvloop

from cyber_sdk.client.lcd import AsyncLCDClient


async def with_sem(aw, sem):
    async with sem:
        print(sem)
        return await aw


async def main():
    bostrom = AsyncLCDClient(url="https://lcd.space-pussy-1.cybernode.ai/", chain_id="space-pussy-1")
    validators, _ = await bostrom.staking.validators()
    validator_addresses = [v.operator_address for v in validators]

    sem = asyncio.Semaphore(2)  # 2 continuous connections
    result = await asyncio.gather(
        *[
            with_sem(bostrom.oracle.misses(address), sem)
            for address in validator_addresses
        ]
    )

    await bostrom.session.close()
    print(result)


uvloop.install()
asyncio.run(main())
