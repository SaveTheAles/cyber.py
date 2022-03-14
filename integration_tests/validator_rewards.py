from cyber_sdk.client.lcd import LCDClient

bostrom = LCDClient(chain_id="space-pussy-1", url="https://lcd.space-pussy-1.cybernode.ai/")
print(
    bostrom.distribution.validator_rewards(
        "bostromvaloper1259cmu5zyklsdkmgstxhwqpe0utfe5hhyty0at"
    )
)
