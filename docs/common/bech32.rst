.. bech32:

Bech32 Strings
==============

To provide some clarity for arguments, some functions in the SDK are documented that
they take a type like :class:`AccAddress` where one may expect a ``str``. It is simply a
type alias annotation (equivalent to ``str``) that serves only to remind the developer
which format the string is expected to be in. 

Bostrom SDK also provides useful functions for checking and converting **addresses** and **pubkeys**.

Addresses
---------

AccAddress
^^^^^^^^^^

.. autoclass:: cyber_sdk.core.bech32.AccAddress
    :members:

.. autofunction:: cyber_sdk.core.bech32.is_acc_address

.. autofunction:: cyber_sdk.core.bech32.to_acc_address

ValAddress
^^^^^^^^^^

.. autoclass:: cyber_sdk.core.bech32.ValAddress
    :members:

.. autofunction:: cyber_sdk.core.bech32.is_val_address

.. autofunction:: cyber_sdk.core.bech32.to_val_address



PubKeys
-------

AccPubKey
^^^^^^^^^

.. autoclass:: cyber_sdk.core.bech32.AccPubKey
    :members:

.. autofunction:: cyber_sdk.core.bech32.is_acc_pubkey

.. autofunction:: cyber_sdk.core.bech32.to_acc_pubkey

ValPubKey
^^^^^^^^^

.. autoclass:: cyber_sdk.core.bech32.ValPubKey
    :members:

.. autofunction:: cyber_sdk.core.bech32.is_acc_pubkey

.. autofunction:: cyber_sdk.core.bech32.to_acc_pubkey

