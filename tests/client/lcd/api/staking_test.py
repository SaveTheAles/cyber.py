from cyber_sdk.client.lcd import LCDClient
from cyber_sdk.client.lcd.params import PaginationOptions

bostrom = LCDClient(
    url="https://lcd.space-pussy-1.cybernode.ai/",
    chain_id="space-pussy-1",
)
pagOpt = PaginationOptions(limit=1, count_total=True)


def test_delegations():
    result = bostrom.staking.delegations(
        validator="bostromvaloper1rdkyl03zd4d2g8hlchf0cmpwty2et4vfdjlaef",
        delegator=None,
        params=pagOpt,
    )
    assert result is not None
    result = bostrom.staking.delegations(
        validator=None,
        delegator="bostrom1x46rqay4d3cssq8gxxvqz8xt6nwlz4td20k38v",
        params=pagOpt,
    )
    assert result is not None
    result = bostrom.staking.delegations(
        validator="bostromvaloper1rdkyl03zd4d2g8hlchf0cmpwty2et4vfdjlaef",
        delegator="bostrom1x46rqay4d3cssq8gxxvqz8xt6nwlz4td20k38v",
    )
    assert result is not None
    result = bostrom.staking.delegation(
        validator="bostromvaloper1rdkyl03zd4d2g8hlchf0cmpwty2et4vfdjlaef",
        delegator="bostrom1x46rqay4d3cssq8gxxvqz8xt6nwlz4td20k38v",
    )
    assert result is not None


def test_unbonding():
    # result = bostrom.staking.unbonding_delegations(validator='bostromvaloper1vk20anceu6h9s00d27pjlvslz3avetkvnwmr35',
    #                                              delegator='bostrom17lmam6zguazs5q5u6z5mmx76uj63gldnse2pdp')
    # assert(result is not None)
    result = bostrom.staking.unbonding_delegations(
        validator="bostromvaloper1vk20anceu6h9s00d27pjlvslz3avetkvnwmr35", delegator=None
    )
    assert result is not None
    result = bostrom.staking.unbonding_delegations(
        validator=None,
        delegator="bostrom17lmam6zguazs5q5u6z5mmx76uj63gldnse2pdp",
        params=pagOpt,
    )
    assert result is not None
    # result = bostrom.staking.unbonding_delegation(validator='bostromvaloper1vk20anceu6h9s00d27pjlvslz3avetkvnwmr35',
    #                                             delegator='bostrom17lmam6zguazs5q5u6z5mmx76uj63gldnse2pdp')
    # assert(result is not None)


def test_validators():
    _pagOpt = PaginationOptions(limit=3, count_total=True, reverse=False)
    result = bostrom.staking.validators(_pagOpt)
    assert result is not None
    result = bostrom.staking.validator(
        "bostromvaloper1rdkyl03zd4d2g8hlchf0cmpwty2et4vfdjlaef"
    )
    assert result is not None


def test_redelagations():
    _pagOpt = PaginationOptions(limit=1, count_total=True, reverse=False)
    result = bostrom.staking.redelegations(
        "bostrom17lmam6zguazs5q5u6z5mmx76uj63gldnse2pdp", params=_pagOpt
    )
    assert result is not None
    # result = bostrom.staking.redelegations("bostrom17lmam6zguazs5q5u6z5mmx76uj63gldnse2pdp",
    #                                      validator_src='bostromvaloper1vk20anceu6h9s00d27pjlvslz3avetkvnwmr35',
    #                                      params=_pagOpt)
    # assert(result is not None)
    # result = bostrom.staking.redelegations("bostrom17lmam6zguazs5q5u6z5mmx76uj63gldnse2pdp",
    #                                      validator_dst='bostromvaloper1vk20anceu6h9s00d27pjlvslz3avetkvnwmr35',
    #                                      params=_pagOpt)
    # assert(result is not None)
    # result = bostrom.staking.redelegations("bostrom17lmam6zguazs5q5u6z5mmx76uj63gldnse2pdp",
    #                                      validator_src='bostromvaloper1vk20anceu6h9s00d27pjlvslz3avetkvnwmr35',
    #                                      validator_dst='bostromvaloper1ze5dxzs4zcm60tg48m9unp8eh7maerma38dl84')
    # assert(result is not None)


def test_bonded_validators():
    result = bostrom.staking.bonded_validators(
        "bostrom17lmam6zguazs5q5u6z5mmx76uj63gldnse2pdp", pagOpt
    )
    assert result is not None


def test_pool():
    result = bostrom.staking.pool()
    assert result is not None


def test_parameters():
    result = bostrom.staking.parameters()
    assert result.get("unbonding_time")
    assert result.get("max_validators")
    assert result.get("max_entries")
    assert result.get("historical_entries")
    assert result.get("bond_denom")
