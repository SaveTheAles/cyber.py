from cyber_sdk.client.lcd import LCDClient

bostrom = LCDClient(chain_id="space-pussy-1", url="https://lcd.space-pussy-1.cybernode.ai/")
res = bostrom.gov.deposits(proposal_id=5333)
print(res)
res = bostrom.gov.votes(proposal_id=5333)
print(res)
