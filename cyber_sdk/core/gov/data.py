"""Gov module data types."""

from __future__ import annotations

import copy
from datetime import datetime
from typing import List, Union

import attr
from dateutil import parser
from cyber_proto.cosmos.gov.v1beta1 import Proposal as Proposal_pb
from cyber_proto.cosmos.gov.v1beta1 import TallyResult as TallyResult_pb
from cyber_proto.cosmos.gov.v1beta1 import Vote as Vote_pb
from cyber_proto.cosmos.gov.v1beta1 import VoteOption
from cyber_proto.cosmos.gov.v1beta1 import WeightedVoteOption as WeightedVoteOption_pb

from cyber_sdk.core import AccAddress, Coins
from cyber_sdk.core.distribution import CommunityPoolSpendProposal
from cyber_sdk.core.params import ParameterChangeProposal
from cyber_sdk.core.upgrade import (
    CancelSoftwareUpgradeProposal,
    SoftwareUpgradeProposal,
)
from cyber_sdk.util.json import JSONSerializable, dict_to_data

from .proposals import TextProposal

__all__ = ["Proposal", "Content", "VoteOption", "WeightedVoteOption"]

from ...util.converter import to_isoformat

Content = Union[
    TextProposal,
    CommunityPoolSpendProposal,
    ParameterChangeProposal,
    SoftwareUpgradeProposal,
    CancelSoftwareUpgradeProposal,
]


def Content_from_data(data: dict) -> Content:
    typ = data["@type"]
    if typ == TextProposal.type_url:
        return TextProposal.from_data(data)
    elif typ == CommunityPoolSpendProposal.type_url:
        return CommunityPoolSpendProposal.from_data(data)
    elif typ == ParameterChangeProposal.type_url:
        return ParameterChangeProposal.from_data(data)
    elif typ == SoftwareUpgradeProposal.type_url:
        return SoftwareUpgradeProposal.from_data(data)
    elif typ == CancelSoftwareUpgradeProposal.type_url:
        return CancelSoftwareUpgradeProposal.from_data(data)
    else:
        raise ValueError("content type is invalid")


@attr.s
class TallyResult(JSONSerializable):
    yes: str = attr.ib()
    abstain: str = attr.ib()
    no: str = attr.ib()
    no_with_veto: str = attr.ib()

    def to_amino(self) -> dict:
        return {
            "yes": self.yes,
            "abstain": self.abstain,
            "no": self.no,
            "no_with_veto": self.no_with_veto,
        }

    @classmethod
    def from_data(cls, data: dict) -> TallyResult:
        return cls(
            yes=data["yes"],
            abstain=data["abstain"],
            no=data["no"],
            no_with_veto=data["no_with_veto"],
        )

    def to_proto(self) -> TallyResult_pb:
        return TallyResult_pb(
            yes=self.yes,
            abstain=self.abstain,
            no=self.no,
            no_with_veto=self.no_with_veto,
        )


@attr.s
class Proposal(JSONSerializable):
    """Contains information about a submitted proposal on the blockchain."""

    proposal_id: int = attr.ib(converter=int)
    """Proposal's ID."""

    content: Content = attr.ib()
    """Proposal contents."""

    status: str = attr.ib()
    """Status of proposal."""

    final_tally_result: TallyResult = attr.ib()
    """Final tallied result of the proposal (after vote)."""

    submit_time: datetime = attr.ib(converter=parser.parse)
    """Timestamp at which proposal was submitted."""

    deposit_end_time: datetime = attr.ib(converter=parser.parse)
    """Time at which the deposit period ended, or will end."""

    total_deposit: Coins = attr.ib(converter=Coins)
    """Total amount deposited for proposal"""

    voting_start_time: datetime = attr.ib(converter=parser.parse)
    """Time at which voting period started, or will start."""

    voting_end_time: datetime = attr.ib(converter=parser.parse)
    """Time at which voting period ended, or will end."""

    def to_data(self) -> dict:
        d = copy.deepcopy(self.__dict__)
        d["id"] = str(d["id"])
        return dict_to_data(d)

    def to_amino(self) -> dict:
        return {
            "proposal_id": str(self.proposal_id),
            "content": self.content.to_amino(),
            "status": self.status,
            "final_tally_result": self.final_tally_result.to_amino(),
            "submit_time": to_isoformat(self.submit_time),
            "deposit_end_time": to_isoformat(self.deposit_end_time),
            "total_deposit": self.total_deposit.to_amino(),
            "voting_start_time": to_isoformat(self.voting_start_time),
            "voting_end_time": to_isoformat(self.voting_end_time),
        }

    @classmethod
    def from_data(cls, data: dict) -> Proposal:
        return cls(
            proposal_id=data["proposal_id"],
            content=Content_from_data(data["content"]),
            status=data["status"],
            final_tally_result=data["final_tally_result"],
            submit_time=data["submit_time"],
            deposit_end_time=data["deposit_end_time"],
            total_deposit=Coins.from_data(data["total_deposit"]),
            voting_start_time=data["voting_start_time"],
            voting_end_time=data["voting_end_time"],
        )

    def to_proto(self) -> Proposal_pb:
        return Proposal_pb(
            proposal_id=self.proposal_id,
            content=self.content.pack_any(),
            status=self.status,
            final_tally_result=self.final_tally_result.to_proto(),
            submit_time=self.submit_time,
            deposit_end_time=self.deposit_end_time,
            total_deposit=self.total_deposit.to_proto(),
            voting_start_time=self.voting_start_time,
            voting_end_time=self.voting_end_time,
        )


@attr.s
class WeightedVoteOption(JSONSerializable):
    weight: str = attr.ib()
    option: VoteOption = attr.ib(converter=int)

    def to_amino(self) -> dict:
        return {"weight": self.weight, "option": self.option.name}

    @classmethod
    def from_data(cls, data: dict) -> WeightedVoteOption:
        return cls(option=data["option"], weight=data["weight"])

    def to_proto(self) -> WeightedVoteOption_pb:
        return WeightedVoteOption_pb(option=self.option, weight=self.weight)


@attr.s
class Vote(JSONSerializable):
    proposal_id: int = attr.ib(converter=int)
    voter: AccAddress = attr.ib()
    options: List[WeightedVoteOption] = attr.ib(converter=list)

    def to_amino(self) -> dict:
        return {
            "proposal_id": str(self.proposal_id),
            "voter": self.voter,
            "options": [opt.to_amino() for opt in self.options],
        }

    @classmethod
    def from_data(cls, data: dict) -> Vote:
        return cls(
            proposal_id=data["proposal_id"],
            voter=data["voter"],
            options=data["options"],
        )

    def to_proto(self) -> Vote_pb:
        return Vote_pb(
            proposal_id=self.proposal_id, voter=self.voter, options=self.options
        )
