Usage with asyncio
==================
    
You can use AsyncLCDClient to make asynchronous, non-blocking LCD requests.
The interface is similar to LCDClient, except the module and wallet API functions must be awaited.

Async module APIs
-----------------

You can replace your LCDClient instance with AsyncLCDClient inside a coroutine function:

.. code-block:: python
    :emphasize-lines: 5,8

    import asyncio 
    from cyber_sdk.client.lcd import AsyncLCDClient

    async def main():
        bostrom = AsyncLCDClient("https://lcd.bostrom.dev", "columbus-5")
        total_supply = await bostrom.bank.total()
        print(total_supply)
        await bostrom.session.close() # you must close the session

    asyncio.get_event_loop().run_until_complete(main())


For convenience, you can use the async context manager to automatically teardown the
session. Here's the same code as above, this time using the ``async with`` construct.

.. code-block:: python
    :emphasize-lines: 5

    import asyncio 
    from cyber_sdk.client.lcd import AsyncLCDClient

    async def main():
        async with AsyncLCDClient("https://lcd.bostrom.dev", "columbus-5") as bostrom:
            total_supply = await bostrom.bank.total()
            print(total_supply)

    asyncio.get_event_loop().run_until_complete(main())

Async wallet API
----------------

When creating a wallet with AsyncLCDClient, the wallet's methods that create LCD requests
are also asychronous and therefore must be awaited.

.. code-block:: python
    :emphasize-lines: 12-13

    import asyncio
    from cyber_sdk.client.lcd.api.tx import CreateTxOptions
    from cyber_sdk.client.lcd import AsyncLCDClient
    from cyber_sdk.key.mnemonic import MnemonicKey
    from cyber_sdk.core import Coins

    mk = MnemonicKey()
    recipient = "bostrom1..."

    async def main():
        async with AsyncLCDClient("https://lcd.bostrom.dev", "columbus-5") as bostrom:
            wallet = bostrom.wallet(mk)
            account_number = await wallet.account_number()
            tx = await wallet.create_and_sign_tx(
                CreateTxOptions(
                    msgs=[MsgSend(wallet.key.acc_address, recipient, Coins(boot=10202))]
                )
            )
    
    asyncio.get_event_loop().run_until_complete(main())

Alternative event loops
-----------------------

The native ``asyncio`` event loop can be replaced with an alternative such as ``uvloop``
for more performance. For example:

.. code-block:: python
    :emphasize-lines: 2, 10

    import asyncio
    import uvloop

    from cyber_sdk.client.lcd import AsyncLCDClient

    async def main():
        async with AsyncLCDClient("https://lcd.bostrom.dev", "columbus-5") as bostrom:
            total_supply = await wallet.bank.total()

    uvloop.install() 
    asyncio.get_event_loop().run_until_complete(main())
