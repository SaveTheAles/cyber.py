Usage with Pagination
=====================

You can query information with Pagination to get information partially.

PaginationOption
----------------

.. autoclass:: cyber_sdk.client.lcd.params.APIParams
    :members:

.. autoclass:: cyber_sdk.client.lcd.params.PaginationOptions
    :members:

You can use PaginationOptions as APIParams for params of query functions.

.. code-block:: python
    :emphasize-lines: 5,8

    from cyber_sdk.client.lcd import LCDClient, PaginationOptions

    bostrom = LCDClient(
        url="https://lcd.bostrom.cybernode.ai/",
        chain_id="bostrom",
    )


    result, pagination  = bostrom.gov.proposals()

    while pagination["next_key"] is not None:
        pagOpt = PaginationOptions(key=pagination["next_key"])
        result, pagination = bostrom.gov.proposals(params=pagOpt)
        pagOpt.key = pagination["next_key"]
        print(result)

