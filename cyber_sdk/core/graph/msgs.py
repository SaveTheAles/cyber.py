"""Graph module message types."""

from __future__ import annotations

from typing import Any


from cyber_proto.cyber.graph.v1beta1 import MsgCyberlink as MsgCyberlink_pb
from cyber_proto.cyber.graph.v1beta1 import Link as Link_pb

from cyber_sdk.core import AccAddress
from cyber_sdk.core.msg import Msg

# TODO: add linkchain. Refactor to/from methods
__all__ = ["MsgCyberlink"]

import attr


@attr.s
class MsgCyberlink(Msg):
    """Creats native Bostrom cyberlinks from ``object_from`` to
    ``object_to``.

    Args:
        neuron: creator
        object_from: cid_from
        object_to: cid_to
    """

    type_amino = "cyber/MsgCyberlink"
    """"""
    type_url = "/cyber.graph.v1beta1.MsgCyberlink"
    """"""
    action = "cyberlink"
    """"""

    neuron: AccAddress = attr.ib()
    object_from: str = attr.ib()
    object_to: str = attr.ib()

    def to_amino(self) -> dict:
        return {
            "type": self.type_amino,
            "value": {
                "neuron": self.from_address,
                "links": self.links,
            },
        }

    @classmethod
    def from_data(cls, data: dict) -> MsgCyberlink:
        return cls(
            neuron=data["neuron"],
            object_from=data["object_from"],
            object_to=data["object_to"],
        )

    def to_data(self) -> dict:
        return {
            "@type": self.type_url,
            "neuron": self.neuron,
            "links": self.links,
        }

    @classmethod
    def from_proto(cls, proto: MsgCyberlink_pb) -> MsgCyberlink:
        return cls(
            neuron=proto["neuron"],
            object_from=proto["object_from"],
            object_to=proto["object_to"],
        )

    def to_proto(self) -> MsgCyberlink_pb:
        proto = MsgCyberlink_pb()
        proto.neuron = self.neuron
        link = Link_pb()
        link.from_ = self.object_from
        link.to = self.object_to
        proto.links.append(link)
        return proto

    @classmethod
    def unpack_any(cls, any: Any) -> MsgCyberlink:
        return MsgCyberlink.from_proto(any)