from __future__ import annotations

from asyncio import AbstractEventLoop, get_event_loop
from json import JSONDecodeError
from typing import List, Optional, Union
from warnings import warn

import nest_asyncio
from aiohttp import ClientSession
from multidict import CIMultiDict

from cyber_sdk.core import Coins, Dec, Numeric
from cyber_sdk.exceptions import LCDResponseError
from cyber_sdk.key.key import Key
from cyber_sdk.util.json import dict_to_data
from cyber_sdk.util.url import urljoin

from .api.auth import AsyncAuthAPI, AuthAPI
from .api.authz import AsyncAuthzAPI, AuthzAPI
from .api.bank import AsyncBankAPI, BankAPI
from .api.distribution import AsyncDistributionAPI, DistributionAPI
from .api.feegrant import AsyncFeeGrantAPI, FeeGrantAPI
from .api.gov import AsyncGovAPI, GovAPI
from .api.graph import AsyncGraphAPI, GraphAPI
from .api.ibc import AsyncIbcAPI, IbcAPI
from .api.ibc_transfer import AsyncIbcTransferAPI, IbcTransferAPI
from .api.liquidity import AsyncLiquidityAPI, LiquidityAPI
from .api.mint import AsyncMintAPI, MintAPI
from .api.oracle import AsyncOracleAPI, OracleAPI
from .api.rank import AsyncRankAPI, RankAPI
from .api.slashing import AsyncSlashingAPI, SlashingAPI
from .api.staking import AsyncStakingAPI, StakingAPI
from .api.tendermint import AsyncTendermintAPI, TendermintAPI
from .api.treasury import AsyncTreasuryAPI, TreasuryAPI
from .api.tx import AsyncTxAPI, TxAPI
from .api.wasm import AsyncWasmAPI, WasmAPI
from .lcdutils import AsyncLCDUtils, LCDUtils
from .params import APIParams
from .wallet import AsyncWallet, Wallet


def get_default(chain_id: str) -> [Coins, Numeric]:
    if chain_id == "bostrom":
        return [Coins.from_str("0.1boot"), Numeric.parse(1.75)]
    if chain_id == "localbostrom":
        return [Coins.from_str("0.1boot"), Numeric.parse(1.75)]
    if chain_id == "space-pussy":
        return [Coins.from_str("0.1pussy"), Numeric.parse(1.75)]
    if chain_id == "osmosis-1":
        return [Coins.from_str("0.001uosmo"), Numeric.parse(1.75)]
    if chain_id == "crescent-1":
        return [Coins.from_str("0.001ucre"), Numeric.parse(1.75)]
    if chain_id == "cosmoshub-4":
        return [Coins.from_str("0.001uatom"), Numeric.parse(1.75)]
    if chain_id == "juno-1":
        return [Coins.from_str("0.001ujuno"), Numeric.parse(1.75)]
    return [Coins(), Numeric.parse(1.75)]


class AsyncLCDClient:
    def __init__(
        self,
        url: str,
        chain_id: Optional[str] = None,
        prefix: str = "bostrom",
        gas_prices: Optional[Coins.Input] = None,
        gas_adjustment: Optional[Numeric.Input] = None,
        loop: Optional[AbstractEventLoop] = None,
        _create_session: bool = True,  # don't create a session (used for sync LCDClient)
    ):
        if loop is None:
            loop = get_event_loop()
        self.loop = loop
        if _create_session:
            self.session = ClientSession(
                headers={"Accept": "application/json"}, loop=self.loop
            )

        self.chain_id = chain_id
        self.url = url
        self.prefix = prefix
        self.last_request_height = None

        default_price, default_adjustment = get_default(chain_id)
        if default_price == Coins() and gas_prices is None:
            warn('Please set `gas_price` and optionally `gas_adjustment` for the LCD client to work properly',
                 stacklevel=2)
        self.gas_prices = Coins(gas_prices) if gas_prices else default_price
        self.gas_adjustment = gas_adjustment if gas_adjustment else default_adjustment

        self.auth = AsyncAuthAPI(self)
        self.bank = AsyncBankAPI(self)
        self.distribution = AsyncDistributionAPI(self)
        self.feegrant = AsyncFeeGrantAPI(self)
        self.gov = AsyncGovAPI(self)
        self.graph = AsyncGraphAPI(self)
        self.liquidity = AsyncLiquidityAPI(self)
        self.mint = AsyncMintAPI(self)
        self.authz = AsyncAuthzAPI(self)
        self.oracle = AsyncOracleAPI(self)
        self.rank = AsyncRankAPI(self)
        self.slashing = AsyncSlashingAPI(self)
        self.staking = AsyncStakingAPI(self)
        self.tendermint = AsyncTendermintAPI(self)
        self.treasury = AsyncTreasuryAPI(self)
        self.wasm = AsyncWasmAPI(self)
        self.ibc = AsyncIbcAPI(self)
        self.ibc_transfer = AsyncIbcTransferAPI(self)
        self.tx = AsyncTxAPI(self)
        self.utils = AsyncLCDUtils(self)

    def wallet(self, key: Key) -> AsyncWallet:
        """Creates a :class:`AsyncWallet` object from a key.

        Args:
            key (Key): key implementation
        """
        return AsyncWallet(self, key)

    async def _get(
        self,
        endpoint: str,
        params: Optional[Union[APIParams, CIMultiDict, list, dict]] = None,
        # raw: bool = False
    ):
        if (
            params
            and hasattr(params, "to_dict")
            and callable(getattr(params, "to_dict"))
        ):
            params = params.to_dict()

        async with self.session.get(
            urljoin(self.url, endpoint), params=params
        ) as response:
            try:
                result = await response.json(content_type=None)
            except JSONDecodeError:
                raise LCDResponseError(message=str(response.reason), response=response)
            if not 200 <= response.status < 299:
                raise LCDResponseError(message=str(result), response=response)
        self.last_request_height = (
            result.get("height") if result else self.last_request_height
        )
        return result  # if raw else result["result"]

    async def _post(
        self, endpoint: str, data: Optional[dict] = None  # , raw: bool = False
    ):
        async with self.session.post(
            urljoin(self.url, endpoint), json=data and dict_to_data(data)
        ) as response:
            try:
                result = await response.json(content_type=None)
            except JSONDecodeError:
                raise LCDResponseError(message=str(response.reason), response=response)
            if not 200 <= response.status < 299:
                raise LCDResponseError(message=result.get("message"), response=response)
        self.last_request_height = (
            result.get("height") if result else self.last_request_height
        )
        return result  # if raw else result["result"]

    async def _search(
        self,
        events: List[list],
        params: Optional[Union[APIParams, CIMultiDict, list, dict]] = None,
        # raw: bool = False
    ):

        actual_params = CIMultiDict()

        for event in events:
            if event[0] == "tx.height":
                actual_params.add("events", f"{event[0]}={event[1]}")
            else:
                actual_params.add("events", f"{event[0]}='{event[1]}'")
        if params:
            for p in params:
                actual_params.add(p, params[p])

        async with self.session.get(
            urljoin(self.url, "/cosmos/tx/v1beta1/txs"), params=actual_params
        ) as response:
            try:
                result = await response.json(content_type=None)
            except JSONDecodeError:
                raise LCDResponseError(message=str(response.reason), response=response)
            if not 200 <= response.status < 299:
                raise LCDResponseError(message=str(result), response=response)
        self.last_request_height = (
            result.get("height") if result else self.last_request_height
        )
        return result  # if raw else result["result"]

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.session.close()


class LCDClient(AsyncLCDClient):
    """An object representing a connection to a node running the Bostrom LCD server."""

    url: str
    """URL endpoint of LCD server."""

    chain_id: str
    """Chain ID of blockchain network connecting to."""

    prefix: str
    """Address prefix"""

    gas_prices: Coins.Input
    """Gas prices to use for automatic fee estimation."""

    gas_adjustment: Union[str, float, int, Dec]
    """Gas adjustment factor for automatic fee estimation."""

    last_request_height: Optional[int]  # type: ignore
    """Height of response of last-made made LCD request."""

    auth: AuthAPI
    """:class:`AuthAPI<cyber_sdk.client.lcd.api.auth.AuthAPI>`."""

    bank: BankAPI
    """:class:`BankAPI<cyber_sdk.client.lcd.api.bank.BankAPI>`."""

    distribution: DistributionAPI
    """:class:`DistributionAPI<cyber_sdk.client.lcd.api.distribution.DistributionAPI>`."""

    gov: GovAPI
    """:class:`GovAPI<cyber_sdk.client.lcd.api.gov.GovAPI>`."""

    graph: GraphAPI
    """:class:`GraphAPI<cyber_sdk.client.lcd.api.graph.GraphAPI>`."""

    feegrant: FeeGrantAPI
    """:class:`FeeGrant<cyber_sdk.client.lcd.api.feegrant.FeeGrantAPI>`."""

    liquidity: LiquidityAPI
    """:class:`LiquidityAPI<cyber_sdk.client.lcd.api.liquidity.LiquidityAPI>`."""

    mint: MintAPI
    """:class:`MintAPI<cyber_sdk.client.lcd.api.mint.MintAPI>`."""

    authz: AuthzAPI
    """:class:`AuthzAPI<cyber_sdk.client.lcd.api.authz.AuthzAPI>`."""

    oracle: OracleAPI
    """:class:`OracleAPI<cyber_sdk.client.lcd.api.oracle.OracleAPI>`."""

    rank: RankAPI
    """:class:`RankAPI<cyber_sdk.client.lcd.api.rank.RankAPI>`."""

    slashing: SlashingAPI
    """:class:`SlashingAPI<cyber_sdk.client.lcd.api.slashing.SlashingAPI>`."""

    staking: StakingAPI
    """:class:`StakingAPI<cyber_sdk.client.lcd.api.staking.StakingAPI>`."""

    tendermint: TendermintAPI
    """:class:`TendermintAPI<cyber_sdk.client.lcd.api.tendermint.TendermintAPI>`."""

    treasury: TreasuryAPI
    """:class:`TreasuryAPI<cyber_sdk.client.lcd.api.treasury.TreasuryAPI>`."""

    wasm: WasmAPI
    """:class:`WasmAPI<cyber_sdk.client.lcd.api.wasm.WasmAPI>`."""

    tx: TxAPI
    """:class:`TxAPI<cyber_sdk.client.lcd.api.tx.TxAPI>`."""

    ibc: IbcAPI
    """:class:`IbcAPI<cyber_sdk.client.lcd.api.ibc.IbcAPI>`."""

    ibc_transfer: IbcTransferAPI
    """:class:`IbcTransferAPI<cyber_sdk.client.lcd.api.ibc_transfer.IbcTransferAPI>`."""

    def __init__(
        self,
        url: str,
        chain_id: str = None,
        prefix: str = "bostrom",
        gas_prices: Optional[Coins.Input] = None,
        gas_adjustment: Optional[Numeric.Input] = None,
    ):
        super().__init__(
            url,
            chain_id,
            prefix,
            gas_prices,
            gas_adjustment,
            _create_session=False,
            loop=nest_asyncio.apply(get_event_loop()),
        )

        self.auth = AuthAPI(self)
        self.bank = BankAPI(self)
        self.distribution = DistributionAPI(self)
        self.gov = GovAPI(self)
        self.graph = GraphAPI(self)
        self.feegrant = FeeGrantAPI(self)
        self.liquidity = LiquidityAPI(self)
        self.mint = MintAPI(self)
        self.authz = AuthzAPI(self)
        self.oracle = OracleAPI(self)
        self.rank = RankAPI(self)
        self.slashing = SlashingAPI(self)
        self.staking = StakingAPI(self)
        self.tendermint = TendermintAPI(self)
        self.treasury = TreasuryAPI(self)
        self.wasm = WasmAPI(self)
        self.ibc = IbcAPI(self)
        self.ibc_transfer = IbcTransferAPI(self)
        self.tx = TxAPI(self)
        self.utils = LCDUtils(self)

    async def __aenter__(self):
        raise NotImplementedError(
            "async context manager not implemented - you probably want AsyncLCDClient"
        )

    async def __aexit__(self, exc_type, exc, tb):
        raise NotImplementedError(
            "async context manager not implemented - you probably want AsyncLCDClient"
        )

    def wallet(self, key: Key) -> Wallet:  # type: ignore
        """Creates a :class:`Wallet` object from a key for easy transaction creating and
        signing.

        Args:
            key (Key): key implementation
        """
        return Wallet(self, key)

    async def _get(self, *args, **kwargs):
        # session has to be manually created and torn down for each HTTP request in a
        # synchronous client
        self.session = ClientSession(
            headers={"Accept": "application/json"}, loop=self.loop
        )
        try:
            result = await super()._get(*args, **kwargs)
        finally:
            await self.session.close()
        return result

    async def _post(self, *args, **kwargs):
        # session has to be manually created and torn down for each HTTP request in a
        # synchronous client
        self.session = ClientSession(
            headers={"Accept": "application/json"}, loop=self.loop
        )
        try:
            result = await super()._post(*args, **kwargs)
        finally:
            await self.session.close()
        return result

    async def _search(self, *args, **kwargs):
        # session has to be manually created and torn down for each HTTP request in a
        # synchronous client
        self.session = ClientSession(
            headers={"Accept": "application/json"}, loop=self.loop
        )
        try:
            result = await super()._search(*args, **kwargs)
        finally:
            await self.session.close()
        return result
