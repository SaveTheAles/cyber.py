from cyber_sdk.core.bech32 import (
    is_acc_address,
    is_acc_pubkey,
    is_val_address,
    is_val_pubkey,
    is_valcons_pubkey,
    to_acc_address,
    to_acc_pubkey,
    to_val_address,
    to_val_pubkey,
)


def test_validates_acc_address():
    assert not is_acc_address("bostromvaloper1pdx498r0hrc2fj36sjhs8vuhrz9hd2cw0yhqtk")
    assert not is_acc_address(
        "bostrom1pdx498r0h7c2fj36sjhs8vu8rz9hd2cw0tmam9"
    )  # bad checksum
    assert not is_acc_address("cosmos176m2p8l3fps3dal7h8gf9jvrv98tu3rqfdht86")

    assert is_acc_address("bostrom1pdx498r0hrc2fj36sjhs8vuhrz9hd2cw0tmam9")


def test_convert_to_acc_address():
    assert (
        to_acc_address("bostromvaloper1pdx498r0hrc2fj36sjhs8vuhrz9hd2cw0yhqtk")
        == "bostrom1pdx498r0hrc2fj36sjhs8vuhrz9hd2cw0tmam9"
    )


def test_validates_val_address():
    assert not is_val_address("bostrom1pdx498r0hrc2fj36sjhs8vuhrz9hd2cw0tmam9")
    assert not is_val_address(
        "bostromvaloper1pdx498r0hrc2fj36sjhs8vuhrz9hd2cw0ygqtk"
    )  # bad checksum
    assert is_val_address("bostromvaloper1pdx498r0hrc2fj36sjhs8vuhrz9hd2cw0yhqtk")


def test_convert_to_val_address():
    assert (
        to_val_address("bostrom1pdx498r0hrc2fj36sjhs8vuhrz9hd2cw0tmam9")
        == "bostromvaloper1pdx498r0hrc2fj36sjhs8vuhrz9hd2cw0yhqtk"
    )


def test_validates_acc_pubkey():
    assert not is_acc_pubkey(
        "bostromvaloperpub1addwnpepqt8ha594svjn3nvfk4ggfn5n8xd3sm3cz6ztxyugwcuqzsuuhhfq5y7accr"
    )
    assert is_acc_pubkey(
        "bostrompub1addwnpepqt8ha594svjn3nvfk4ggfn5n8xd3sm3cz6ztxyugwcuqzsuuhhfq5nwzrf9"
    )


def test_converts_to_acc_pubkey():
    assert (
        to_acc_pubkey(
            "bostromvaloperpub1addwnpepqt8ha594svjn3nvfk4ggfn5n8xd3sm3cz6ztxyugwcuqzsuuhhfq5y7accr"
        )
        == "bostrompub1addwnpepqt8ha594svjn3nvfk4ggfn5n8xd3sm3cz6ztxyugwcuqzsuuhhfq5nwzrf9"
    )


def test_validates_val_pubkey():
    assert not is_val_pubkey(
        "bostrompub1addwnpepqt8ha594svjn3nvfk4ggfn5n8xd3sm3cz6ztxyugwcuqzsuuhhfq5nwzrf9"
    )
    assert is_val_pubkey(
        "bostromvaloperpub1addwnpepqt8ha594svjn3nvfk4ggfn5n8xd3sm3cz6ztxyugwcuqzsuuhhfq5y7accr"
    )


def test_converts_to_val_pubkey():
    assert (
        to_val_pubkey(
            "bostrompub1addwnpepqt8ha594svjn3nvfk4ggfn5n8xd3sm3cz6ztxyugwcuqzsuuhhfq5nwzrf9"
        )
        == "bostromvaloperpub1addwnpepqt8ha594svjn3nvfk4ggfn5n8xd3sm3cz6ztxyugwcuqzsuuhhfq5y7accr"
    )
