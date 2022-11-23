from cyber_sdk.client.lcd import LCDClient

bostrom = LCDClient(
    chain_id="bostrom",
    url="https://lcd.bostrom.cybernode.ai/",
)
res = bostrom.tendermint.node_info()
print(res)
