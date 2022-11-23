from cyber_sdk.client.lcd import LCDClient

if __name__ == "__main__":
    client = LCDClient(url="https://lcd.bostrom.cybernode.ai/", chain_id="bostrom")

    client.tx.tx_info(
        "D22FC6EB287D9F099DD8EBADAAC5D9A0F6AA9D6B87F4A35A3FACEF4182706A16"
    )
