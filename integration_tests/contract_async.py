import asyncio
from pathlib import Path

from cyber_sdk.client.localbostrom import AsyncLocalBostrom
from cyber_sdk.core import Coins, Fee
from cyber_sdk.core.wasm import MsgExecuteContract, MsgInstantiateContract, MsgStoreCode
from cyber_sdk.util.contract import get_code_id, get_contract_address, read_file_as_b64


async def async_main():
    async with AsyncLocalBostrom() as bostrom:
        test1 = bostrom.wallets["test1"]
        store_code_tx = await test1.create_and_sign_tx(
            msgs=[
                MsgStoreCode(
                    test1.key.acc_address,
                    read_file_as_b64(Path(__file__).parent / "./contract.wasm"),
                )
            ]
        )
        store_code_tx_result = await bostrom.tx.broadcast(store_code_tx)
        print(store_code_tx_result)
        code_id = get_code_id(store_code_tx_result)
        instantiate_tx = await test1.create_and_sign_tx(
            msgs=[
                MsgInstantiateContract(
                    test1.key.acc_address,
                    code_id,
                    {"count": 0},
                    {"boot": 10000000, "ukrw": 1000000},
                    False,
                )
            ]
        )
        instantiate_tx_result = await bostrom.tx.broadcast(instantiate_tx)
        print(instantiate_tx_result)
        contract_address = get_contract_address(instantiate_tx_result)

        execute_tx = await test1.create_and_sign_tx(
            msgs=[
                MsgExecuteContract(
                    test1.key.acc_address,
                    contract_address,
                    {"increment": {}},
                    {"boot": 100000},
                )
            ],
            fee=Fee(1000000, Coins(boot=1000000)),
        )

        execute_tx_result = await bostrom.tx.broadcast(execute_tx)
        print(execute_tx_result)

        result = await bostrom.wasm.contract_query(contract_address, {"get_count": {}})
        print(result)


loop = asyncio.new_event_loop()
loop.run_until_complete(async_main())
