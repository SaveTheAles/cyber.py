LCDClient
=========

The :class:`LCDClient` is an object representing a HTTP connection to a Bostrom LCD node.

Get connected
-------------

Create a new LCDClient instance by specifying the URL and chain ID of the node to connect to.

.. note::
    It is common practice to name the active LCDClient instance ``bostrom``, but this is not required.

.. code-block:: python

    >>> from bostrom_sdk.client.lcd import LCDClient
    >>> bostrom = LCDClient(url="https://lcd.bostrom.cybernode.ai/", chain_id="bostrom")
    >>> bostrom.tendermint.node_info()['default_node_info']['network']
    'columbus-5'

You can also specify gas estimation parameters for your chain for building transactions.

.. code-block:: python
    :emphasize-lines: 8-9

    import requests
    from bostrom_sdk.core import Coins

    res = requests.get("https://fcd.bostrom.dev/v1/txs/gas_prices")
    bostrom = LCDClient(
        url="https://lcd.bostrom.cybernode.ai/",
        chain_id="bostrom",
        gas_prices=Coins(res.json()),
        gas_adjustment="1.4"
    )    


Using the module APIs
---------------------

LCDClient includes functions for interacting with each of the core modules (see sidebar). These functions are divided and
and organized by module name (eg. :class:`bostrom.liquidity<bostrom_sdk.client.lcd.api.liquidity.LiquidityAPI>`), and handle
the tedium of building HTTP requests, parsing the results, and handling errors. 

Each request fetches live data from the blockchain:

.. code-block:: python

    >>> bostrom.liquidity.parameters()
    {'base_pool': '7000000000000.000000000000000000', 'pool_recovery_period': '200', 'min_spread': '0.005000000000000000'}

The height of the last result (if applicable) is available:

.. code-block:: python

    >>> bostrom.last_request_height
    89292


Create a wallet
---------------

LCDClient can create a :class:`Wallet` object from any :class:`Key` implementation. Wallet objects
are useful for easily creating and signing transactions.

.. code-block:: python

    >>> from bostrom_sdk.key.mnemonic import MnemonicKey
    >>> mk = MnemonicKey()
    >>> wallet = bostrom.wallet(mk)
    >>> wallet.account_number()
    27


LCDClient Reference
-------------------

.. autoclass:: bostrom_sdk.client.lcd.LCDClient
    :members:
