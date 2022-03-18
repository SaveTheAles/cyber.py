"""Some useful base classes to inherit from."""
from abc import abstractmethod
from typing import Any, Callable, Dict, List
from betterproto.lib.google.protobuf import Any as Any_pb
from betterproto import Message

from .json import JSONSerializable, dict_to_data


class BaseTerraData(JSONSerializable, Message):

    type: str
    type_url: str

    def to_data(self) -> dict:
        return {"type": self.type_url, "value": dict_to_data(self.__dict__)}

    @abstractmethod
    def to_proto(self):
        pass


def create_demux(inputs: List) -> Callable[[Dict[str, Any]], Any]:
    table = {i.type_url: i.from_data for i in inputs}

    def from_data(data: dict):
        return table[data["@type"]](data)

    return from_data


def create_demux_proto(inputs: [str, List]) -> Callable[[Dict[str, Any]], Any]:
    table = {i[0]: i[1]().parse for i in inputs}

    def from_proto(data: Any_pb):
        return table[data.type_url](data.value)

    return from_proto


def create_demux_amino(inputs: List) -> Callable[[Dict[str, Any]], Any]:
    table = {i.type_amino: i.from_amino for i in inputs}

    def from_amino(data: dict):
        return table[data["type"]](data)

    return from_amino
