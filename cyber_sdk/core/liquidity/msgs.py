"""Liquidity module message types."""

from __future__ import annotations

import attr
from cyber_proto.tendermint.liquidity.v1beta1 import MsgSwapWithinBatch as MsgSwapWithinBatch_pb

from cyber_sdk.core import AccAddress, Coin
from cyber_sdk.core.msg import Msg

__all__ = ["MsgSwapWithinBatch"]


@attr.s
class MsgSwapWithinBatch(Msg):
    """Perform a native on-chain swap from ``offer_coin`` to ``demand_coin_denom``.

    Args:
        swap_requester_address (str): address of swap requester.
        pool_id (int): id of swap type, must match the value in the pool. Only `swap_type_id` 1 is supported.
        swap_type_id (int): id of swap type. Must match the value in the pool.
        offer_coin (Union[Coin, str, dict]): coin offered for swap, must match the denom in the pool.
        demand_coin_denom (str): denom of demand coin to be exchanged on the swap request, must match the denom .
        in the pool.
        offer_coin_fee (Union[Coin, str, dict]): limit order price for the order, the price is the exchange ratio
        of X/Y where X is the amount of the first coin and Y is the amount  of the second coin when their denoms are
        sorted alphabetically.
        order_price (str): limit order price for the order, the price is the exchange ratio of X/Y, where X is the
        amount of the first coin and Y is the amount  of the second coin when their denoms are sorted alphabetically.
    """

    type_amino = "liquidity/MsgSwapWithinBatch"
    """"""
    type_url = "/tendermint.liquidity.v1beta1.MsgSwapWithinBatch"
    """"""
    action = "swap"
    """"""

    swap_requester_address: AccAddress = attr.ib()
    pool_id: int = attr.ib()
    swap_type_id: int = attr.ib()
    offer_coin: Coin = attr.ib(converter=Coin.parse)  # type: ignore
    demand_coin_denom: str = attr.ib()
    offer_coin_fee: Coin = attr.ib(converter=Coin.parse)  # type: ignore
    order_price: str = attr.ib()

    def to_amino(self) -> dict:
        return {
            "type": self.type_amino,
            "value": {
                "swap_requester_address": self.swap_requester_address,
                "pool_id": self.pool_id,
                "swap_type_id": self.swap_type_id,
                "offer_coin": self.offer_coin.to_amino(),
                "demand_coin_denom": self.demand_coin_denom,
                "offer_coin_fee": self.offer_coin_fee.to_amino(),
                "order_price": self.order_price,
            },
        }

    @classmethod
    def from_data(cls, data: dict) -> MsgSwapWithinBatch:
        return cls(
            swap_requester_address=data["swap_requester_address"],
            pool_id=data["pool_id"],
            swap_type_id=data["swap_type_id"],
            offer_coin=Coin.from_data(data["offer_coin"]),
            demand_coin_denom=data["demand_coin_denom"],
            offer_coin_fee=Coin.from_data(data["offer_coin_fee"]),
            order_price=data["order_price"],
        )

    def to_proto(self) -> MsgSwapWithinBatch_pb:
        return MsgSwapWithinBatch_pb(
            swap_requester_address=self.swap_requester_address,
            pool_id=self.pool_id,
            swap_type_id=self.swap_type_id,
            offer_coin=self.offer_coin.to_proto(),
            demand_coin_denom=self.demand_coin_denom,
            offer_coin_fee=self.offer_coin_fee.to_proto(),
            order_price=self.order_price,
        )

    @classmethod
    def from_proto(cls, proto: MsgSwapWithinBatch_pb) -> MsgSwapWithinBatch:
        return cls(
            swap_requester_address=proto.swap_requester_address,
            pool_id=proto.pool_id,
            swap_type_id=proto.swap_requester_address,
            offer_coin=Coin.from_proto(proto.offer_coin),
            demand_coin_denom=proto.demand_coin_denom,
            offer_coin_fee=Coin.from_proto(proto.offer_coin_fee),
            order_price=proto.order_price
        )
