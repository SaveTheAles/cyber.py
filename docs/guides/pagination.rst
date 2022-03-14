Usage with Pagination
=====================

You can query information with Pagination to get information partially.

PaginationOption
----------------

.. autoclass:: bostrom_sdk.client.lcd.params.APIParams
    :members:

.. autoclass:: bostrom_sdk.client.lcd.params.PaginationOptions
    :members:

You can use PaginationOptions as APIParams for params of query functions.

.. code-block:: python
    :emphasize-lines: 5,8

    from bostrom_sdk.client.lcd import LCDClient, PaginationOptions

    bostrom = LCDClient(
        url="https://lcd.space-pussy-1.cybernode.ai/",
        chain_id="space-pussy-1",
    )


    result, pagination  = bostrom.gov.proposals()

    while pagination["next_key"] is not None:
        pagOpt = PaginationOptions(key=pagination["next_key"])
        result, pagination = bostrom.gov.proposals(params=pagOpt)
        pagOpt.key = pagination["next_key"]
        print(result)

