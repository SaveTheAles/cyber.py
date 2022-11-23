from cyber_sdk.client.lcd import LCDClient

bostrom = LCDClient(chain_id="bostrom", url="https://lcd.bostrom.cybernode.ai/")

res = bostrom.auth.account_info(address="bostrom1x46rqay4d3cssq8gxxvqz8xt6nwlz4td20k38v")
print(res)

res = bostrom.auth.account_info(address="bostrom1vk20anceu6h9s00d27pjlvslz3avetkvnph7p8")
print(res)
