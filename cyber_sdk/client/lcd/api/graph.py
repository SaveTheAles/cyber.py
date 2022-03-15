from typing import Optional


from ..params import APIParams
from ._base import BaseAsyncAPI, sync_bind

__all__ = ["AsyncGraphAPI", "GraphAPI"]


class AsyncGraphAPI(BaseAsyncAPI):
    async def graph_stats(
        self, params: Optional[APIParams] = None
    ) -> dict:
        """Fetches an graph current stats.

        Args:
            params (APIParams, optional): additional params for the API like pagination

        Returns:
            The dictionary of graph stats
        """
        res = await self._c._get(f"/cyber/graph/v1beta1/graph_stats", params)
        return res


class GraphAPI(AsyncGraphAPI):
    @sync_bind(AsyncGraphAPI.graph_stats)
    def graph_stats(
        self, params: Optional[APIParams] = None
    ) -> dict:
        pass

    graph_stats.__doc__ = AsyncGraphAPI.graph_stats.__doc__
