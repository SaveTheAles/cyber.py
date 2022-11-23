from cyber_sdk.client.lcd import LCDClient

bostrom = LCDClient(chain_id="bostrom", url="https://lcd.bostrom.cybernode.ai/")
res = bostrom.gov.deposits(proposal_id=5333)
print(res)
res = bostrom.gov.votes(proposal_id=5333)
print(res)
