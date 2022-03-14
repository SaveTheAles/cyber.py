from cyber_sdk.client.lcd import LCDClient, PaginationOptions

bostrom = LCDClient(
    url="https://lcd.space-pussy-1.cybernode.ai/",
    chain_id="space-pussy-1",
)

pagOpt = PaginationOptions(limit=2, count_total=True)


def test_proposals():
    result = bostrom.gov.proposals()
    assert result is not None


def test_proposals_with_pagination():
    result = bostrom.gov.proposals(PaginationOptions(limit=2))
    assert result is not None


def test_proposal():
    result = bostrom.gov.proposal(5368)
    assert result is not None


# public lcd requires tx.height
# def test_proposer():
#     result = bostrom.gov.proposer(5368)
#     assert(result is not None)


# public lcd requires tx.height
# def test_deposits():
#    result = bostrom.gov.deposits(5368)
#    assert(result is not None)


# public lcd requires tx.height
# def test_deposits_with_pagination():
#     result = bostrom.gov.deposits(5368, params=pagOpt)
#     assert(result is not None)


# public lcd requires tx.height
# def test_votes():
#     result = bostrom.gov.votes(5368)
#     assert(result is not None)


# public lcd requires tx.height
# def test_votes_with_pagination():
#     result = bostrom.gov.votes(5368, pagOpt)
#     assert(result is not None)


def test_tally():
    result = bostrom.gov.tally(5368)
    assert result is not None


def test_deposit_parameters():
    result = bostrom.gov.deposit_parameters()
    assert result.get("min_deposit")
    assert result.get("max_deposit_period")


def test_voting_parameters():
    result = bostrom.gov.voting_parameters()
    assert result.get("voting_period")


def test_tally_parameters():
    result = bostrom.gov.tally_parameters()
    assert result.get("quorum")
    assert result.get("threshold")
    assert result.get("veto_threshold")


def test_parameters():
    result = bostrom.gov.parameters()
    assert result.get("deposit_params")
    assert result.get("voting_params")
    assert result.get("tally_params")
