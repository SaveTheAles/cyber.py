from cyber_sdk.client.lcd import LCDClient

bostrom = LCDClient(
    chain_id="space-pussy-1",
    url="https://lcd.space-pussy-1.cybernode.ai/",
)
res = bostrom.tendermint.node_info()
print(res)
