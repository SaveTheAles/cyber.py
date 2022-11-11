from cyber_sdk.core.liquidity import MsgSwapWithinBatch


def test_deserializes_msg_swap_examples(load_msg_examples):
    examples = load_msg_examples(MsgSwapWithinBatch.type_url, "./MsgSwapWithinBatch.data.json")
    for example in examples:
        assert MsgSwapWithinBatch.from_data(example).to_data() == example
