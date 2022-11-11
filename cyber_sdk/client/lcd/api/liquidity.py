from cyber_sdk.core import Coin, Dec

from ._base import BaseAsyncAPI, sync_bind

__all__ = ["AsyncLiquidityAPI", "LiquidityAPI"]


class AsyncLiquidityAPI(BaseAsyncAPI):
    async def swap_rate(self, offer_coin: Coin, ask_denom: str) -> Coin:
        """Simulates a swap given an amount offered and a target denom.

        Args:
            offer_coin (Coin): amount offered (swap from)
            ask_denom (str): target denom (swap to)

        Returns:
            Coin: simulated amount received
        """
        params = {"offer_coin": str(offer_coin), "ask_denom": ask_denom}
        res = await self._c._get("/bostrom/liquidity/v1beta1/swap", params)
        return Coin.from_data(res.get("return_coin"))

    async def bostrom_pool_delta(self) -> Dec:
        """Fetches the Bostrom pool delta.

        Returns:
            Dec: Bostrom pool delta
        """
        res = await self._c._get("/bostrom/liquidity/v1beta1/bostrom_pool_delta")
        return Dec(res.get("bostrom_pool_delta"))

    async def parameters(self) -> dict:
        """Fetches the Liquidity module's parameters.

        Returns:
            dict: Liquidity module parameters
        """
        res = await self._c._get("/bostrom/liquidity/v1beta1/params")
        params = res["params"]
        return {
            "base_pool": Dec(params.get("base_pool")),
            "pool_recovery_period": int(params.get("pool_recovery_period")),
            "min_stability_spread": Dec(params.get("min_stability_spread")),
        }


class LiquidityAPI(AsyncLiquidityAPI):
    @sync_bind(AsyncLiquidityAPI.swap_rate)
    def swap_rate(self, offer_coin: Coin, ask_denom: str) -> Coin:
        pass

    swap_rate.__doc__ = AsyncLiquidityAPI.swap_rate.__doc__

    @sync_bind(AsyncLiquidityAPI.bostrom_pool_delta)
    def bostrom_pool_delta(self) -> Dec:
        pass

    bostrom_pool_delta.__doc__ = AsyncLiquidityAPI.bostrom_pool_delta.__doc__

    @sync_bind(AsyncLiquidityAPI.parameters)
    def parameters(self) -> dict:
        pass

    parameters.__doc__ = AsyncLiquidityAPI.parameters.__doc__
