from __future__ import annotations

from betterproto.lib.google.protobuf import Any as Any_pb

from cyber_sdk.util.base import BaseBostromData


class Msg(BaseBostromData):
    def to_proto(self):
        raise NotImplementedError

    def pack_any(self) -> Any_pb:
        return Any_pb(type_url=self.type_url, value=bytes(self.to_proto()))

    @staticmethod
    def from_data(data: dict) -> Msg:
        from cyber_sdk.util.parse_msg import parse_msg

        return parse_msg(data)
