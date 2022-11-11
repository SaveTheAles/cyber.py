from cyber_sdk.core.authz import (
    MsgExecAuthorized,
    MsgGrantAuthorization,
    MsgRevokeAuthorization,
)
from cyber_sdk.core.bank import MsgMultiSend, MsgSend
from cyber_sdk.core.distribution import (
    MsgFundCommunityPool,
    MsgSetWithdrawAddress,
    MsgWithdrawDelegationReward,
    MsgWithdrawValidatorCommission,
)
from cyber_sdk.core.gov.msgs import MsgDeposit, MsgSubmitProposal, MsgVote
from cyber_sdk.core.ibc.msgs import (
    MsgAcknowledgement,
    MsgChannelCloseConfirm,
    MsgChannelCloseInit,
    MsgChannelOpenAck,
    MsgChannelOpenConfirm,
    MsgChannelOpenInit,
    MsgChannelOpenTry,
    MsgConnectionOpenAck,
    MsgConnectionOpenConfirm,
    MsgConnectionOpenInit,
    MsgConnectionOpenTry,
    MsgCreateClient,
    MsgRecvPacket,
    MsgSubmitMisbehaviour,
    MsgTimeout,
    MsgUpdateClient,
    MsgUpgradeClient,
)
from cyber_sdk.core.ibc_transfer import MsgTransfer
from cyber_sdk.core.liquidity import MsgSwapWithinBatch
from cyber_sdk.core.oracle import (
    MsgAggregateExchangeRatePrevote,
    MsgAggregateExchangeRateVote,
    MsgDelegateFeedConsent,
)
from cyber_sdk.core.slashing import MsgUnjail
from cyber_sdk.core.staking import (
    MsgBeginRedelegate,
    MsgCreateValidator,
    MsgDelegate,
    MsgEditValidator,
    MsgUndelegate,
)
from cyber_sdk.core.wasm import (
    MsgClearContractAdmin,
    MsgExecuteContract,
    MsgInstantiateContract,
    MsgMigrateCode,
    MsgMigrateContract,
    MsgStoreCode,
    MsgUpdateContractAdmin,
)

from .base import create_demux, create_demux_proto

bank_msgs = [MsgSend, MsgMultiSend]
distribution_msgs = [
    MsgFundCommunityPool,
    MsgSetWithdrawAddress,
    MsgWithdrawDelegationReward,
    MsgWithdrawValidatorCommission,
]
gov_msgs = [MsgDeposit, MsgSubmitProposal, MsgVote]
liquidity_msgs = [MsgSwapWithinBatch]
authz_msgs = [
    MsgExecAuthorized,
    MsgGrantAuthorization,
    MsgRevokeAuthorization,
]
oracle_msgs = [
    MsgAggregateExchangeRatePrevote,
    MsgAggregateExchangeRateVote,
    MsgDelegateFeedConsent,
]
slashing_msgs = [MsgUnjail]
staking_msgs = [
    MsgBeginRedelegate,
    MsgCreateValidator,
    MsgDelegate,
    MsgEditValidator,
    MsgUndelegate,
]
wasm_msgs = [
    MsgStoreCode,
    MsgMigrateCode,
    MsgInstantiateContract,
    MsgExecuteContract,
    MsgMigrateContract,
    MsgUpdateContractAdmin,
    MsgClearContractAdmin,
]

ibc_transfer_msgs = [MsgTransfer]
ibc_msgs = [
    MsgCreateClient,
    MsgUpdateClient,
    MsgUpgradeClient,
    MsgSubmitMisbehaviour,
    MsgConnectionOpenInit,
    MsgConnectionOpenTry,
    MsgConnectionOpenAck,
    MsgConnectionOpenConfirm,
    MsgChannelOpenInit,
    MsgChannelOpenTry,
    MsgChannelOpenAck,
    MsgChannelOpenConfirm,
    MsgChannelCloseInit,
    MsgChannelCloseConfirm,
    MsgRecvPacket,
    MsgTimeout,
    MsgAcknowledgement,
]

parse_msg = create_demux(
    [
        *bank_msgs,
        *distribution_msgs,
        *gov_msgs,
        *liquidity_msgs,
        *oracle_msgs,
        *slashing_msgs,
        *staking_msgs,
        *wasm_msgs,
        *ibc_msgs,
        *ibc_transfer_msgs,
    ]
)
parse_proto = create_demux_proto(
    [
        *bank_msgs,
        *distribution_msgs,
        *gov_msgs,
        *liquidity_msgs,
        *oracle_msgs,
        *slashing_msgs,
        *staking_msgs,
        *wasm_msgs,
        *ibc_msgs,
        *ibc_transfer_msgs,
    ]
)
