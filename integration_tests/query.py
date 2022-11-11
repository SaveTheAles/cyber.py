import asyncio
import base64
from pathlib import Path

from cyber_sdk.client.lcd import LCDClient
from cyber_sdk.core import Coins
from cyber_sdk.core.bank import MsgSend
from cyber_sdk.util.contract import get_code_id


def main():
    bostrom = LCDClient(
        url="https://lcd.bostrom.cybernode.ai/",
        chain_id="bostrom",
    )

    result = bostrom.tx.tx_infos_by_height(None)
    print(result)


main()
