from cyber_sdk.client.lcd import LCDClient

bostrom = LCDClient(chain_id="bostrom", url="https://lcd.bostrom.cybernode.ai/")
print(
    bostrom.distribution.validator_rewards(
        "bostromvaloper1259cmu5zyklsdkmgstxhwqpe0utfe5hhyty0at"
    )
)
