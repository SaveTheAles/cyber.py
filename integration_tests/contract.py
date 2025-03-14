from pathlib import Path

from cyber_sdk.client.lcd.api.tx import CreateTxOptions
from cyber_sdk.client.localbostrom import LocalBostrom
from cyber_sdk.core import Coins
from cyber_sdk.core.fee import Fee
from cyber_sdk.core.wasm import MsgExecuteContract, MsgInstantiateContract, MsgStoreCode
from cyber_sdk.util.contract import get_code_id, get_contract_address, read_file_as_b64


def main():
    bostrom = LocalBostrom()
    bostrom.gas_prices = "1boot"
    test1 = bostrom.wallets["test1"]

    store_code_tx = test1.create_and_sign_tx(
        CreateTxOptions(
            msgs=[
                MsgStoreCode(
                    test1.key.acc_address,
                    read_file_as_b64(Path(__file__).parent / "./contract.wasm"),
                )
            ],
            gas_adjustment=1.75,
        )
    )
    store_code_tx_result = bostrom.tx.broadcast(store_code_tx)
    print(store_code_tx_result)

    code_id = get_code_id(store_code_tx_result)
    print(f"cod_id:{code_id}")

    instantiate_tx = test1.create_and_sign_tx(
        CreateTxOptions(
            msgs=[
                MsgInstantiateContract(
                    test1.key.acc_address, test1.key.acc_address, code_id, {"count": 10}
                )
            ],
            gas_prices="10boot",
            gas_adjustment=2,
        )
    )
    print(instantiate_tx)
    instantiate_tx_result = bostrom.tx.broadcast(instantiate_tx)
    print(instantiate_tx_result)
    contract_address = get_contract_address(instantiate_tx_result)
    # """
    # contract_address = "bostrom1e8d3cw4j0k5fm9gw03jzh9xzhzyz99pa8tphd8"
    result = bostrom.wasm.contract_query(contract_address, {"get_count": {}})
    print("get_count1: ", result)
    execute_tx = test1.create_and_sign_tx(
        CreateTxOptions(
            msgs=[
                MsgExecuteContract(
                    test1.key.acc_address,
                    contract_address,
                    {"increment": {}},
                )
            ],
            gas_adjustment=1.75,
        )
    )
    #                {"boot": 1000},

    execute_tx_result = bostrom.tx.broadcast(execute_tx)
    print(execute_tx_result)

    result = bostrom.wasm.contract_query(contract_address, {"get_count": {}})
    print("get_count2: ", result)


# try:
main()
# except Exception as e:
#    print("exception occured")
#    print(e)
