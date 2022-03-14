from cyber_sdk.client.lcd import LCDClient, PaginationOptions
from cyber_sdk.client.lcd.api.gov import ProposalStatus

bostrom = LCDClient(
    url="https://lcd.space-pussy-1.cybernode.ai/",
    chain_id="space-pussy-1",
)


result, pagination = bostrom.gov.proposals()

while pagination["next_key"] is not None:
    pagOpt = PaginationOptions(key=pagination["next_key"])
    result, pagination = bostrom.gov.proposals(params=pagOpt)
    pagOpt.key = pagination["next_key"]
    print(result)


result, pagination = bostrom.gov.proposals(
    options={
        "proposal_status": ProposalStatus.PROPOSAL_STATUS_DEPOSIT_PERIOD,
        "depositor": "bostrom1w8wc2ke09242v7vjqd5frzw6ulpz4l7yrcwppt",
    }
)
print(result)
