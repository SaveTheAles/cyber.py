from abc import ABC, abstractmethod

from cyber_sdk.core.public_key import PublicKey
from cyber_sdk.util.json import JSONSerializable

from .base_account import BaseAccount
from .base_periodic_vesting_account import BasePeriodicVestingAccount
from .lazy_graded_vesting_account import LazyGradedVestingAccount


class Account(JSONSerializable, ABC):
    @abstractmethod
    def get_account_number(self) -> int:
        pass

    @abstractmethod
    def get_sequence(self) -> int:
        pass

    @abstractmethod
    def get_public_key(self) -> PublicKey:
        pass

    @classmethod
    def from_amino(cls, amino: dict):  # -> Account:
        if amino["type"] == BaseAccount.type_amino:
            return BaseAccount.from_amino(amino)
        else:
            return LazyGradedVestingAccount.from_amino(amino)

    @classmethod
    def from_data(cls, data: dict):  # -> Account:
        if data["@type"] == BaseAccount.type_url:
            return BaseAccount.from_data(data)
        # TODO refactor that
        elif data["@type"] == '/cosmos.vesting.v1beta1.PeriodicVestingAccount':
            return BasePeriodicVestingAccount.from_data(data)
        else:
            return LazyGradedVestingAccount.from_data(data)
