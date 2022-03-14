from cyber_sdk.client.lcd import LCDClient, PaginationOptions

bostrom = LCDClient(
    url="https://lcd.space-pussy-1.cybernode.ai/",
    chain_id="space-pussy-1",
)

pagOpt = PaginationOptions(limit=2, count_total=True)


def test_allowances():
    result, _ = bostrom.feegrant.allowances(
        "bostrom17lmam6zguazs5q5u6z5mmx76uj63gldnse2pdp"
    )
    assert result is not None
    assert len(result) == 0


# def test_allowance():
#     result = bostrom.feegrant.allowance(
#         "bostrom1x46rqay4d3cssq8gxxvqz8xt6nwlz4td20k38v",
#         "bostrom17lmam6zguazs5q5u6z5mmx76uj63gldnse2pdp",
#    )
#     assert(result is not None)
