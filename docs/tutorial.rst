.. quickstart:

Quickstart
==========


.. note:: All code starting with a ``$`` is meant to run on your terminal.
    All code starting with a ``>>>`` is meant to run in a python interpreter,
    like `ipython <https://pypi.org/project/ipython/>`_.

Installation
------------

Bostrom SDK can be installed (preferably in a :ref:`virtualenv <setup_environment>`)
using ``pip`` as follows:

.. code-block:: shell

   $ pip install bostrom-sdk


.. note:: If you run into problems during installation, you might have a
    broken environment. See the troubleshooting guide to :ref:`setting up a
    clean environment <setup_environment>`.


Using Bostrom SDK
---------------

In order to interact with the Bostrom blockchain, you'll need a connection to a Bostrom node.
This can be done through setting up an LCDClient:


.. code-block:: python

    from bostrom_sdk.client.lcd import LCDClient

    bostrom = LCDClient(chain_id="space-pussy-1", url="https://lcd.space-pussy-1.cybernode.ai/")
    print(bostrom.tendermint.node_info())


Getting Blockchain Info
-----------------------

It's time to start using Bostrom SDK! Once properly configured, the ``LCDClient`` instance will allow you
to interact with the Bostrom blockchain. Try getting the latest block height:

.. code-block:: python

    >>> bostrom.tendermint.block_info()['block']['header']['height']
    '1687543'

Bostrom SDK can help you read block data, sign and send transactions, deploy and interact with contracts,
and a number of other features.
