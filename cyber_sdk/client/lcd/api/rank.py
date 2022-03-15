from typing import Optional

from cyber_sdk.core import AccAddress, Coins

from ..params import APIParams
from ._base import BaseAsyncAPI, sync_bind

__all__ = ["AsyncRankAPI", "RankAPI"]


class AsyncRankAPI(BaseAsyncAPI):
    async def is_cyberlink_exist(
        self, object_from: str, object_to: str
    ) -> bool:
        """Checks if cyberlink exist.

        Args:
            object_from (str): cid_from
            object_to (str): cid_ti
            params (APIParams, optional): additional params for the API like pagination

        Returns:
            Bool: result
            Pagination: pagination info
        """
        res = await self._c._get(f"/cyber/rank/v1beta1/is_any_link_exist?from={object_from}&to={object_to}")
        return bool(res['exist'])

    async def is_neurons_cyberlink_exist(
        self, neuron: AccAddress, object_from: str, object_to: str, params: Optional[APIParams] = None
    ) -> bool:
        """Checks if cyberlink created by neuron exist.

        Args:
            neuron (AccAddress): account address
            object_from (str): cid_from
            object_to (str): cid_ti
            params (APIParams, optional): additional params for the API like pagination

        Returns:
            Bool: result
            Pagination: pagination info
        """
        res = await self._c._get(
            f"/cyber/rank/v1beta1/is_link_exist?from={object_from}&to={object_to}&address={neuron}", params
        )
        return bool(res['exist'])

    async def neuron_karma(
        self, neuron: AccAddress, params: Optional[APIParams] = None
    ) -> int:
        """Checks neurons karma.

        Args:
            neuron (AccAddress): account address
            params (APIParams, optional): additional params for the API like pagination

        Returns:
            Int: karma
            Pagination: pagination info
        """
        res = await self._c._get(
            f"/cyber/rank/v1beta1/karma/{neuron}", params
        )
        return int(res['karma'])

    async def negentropy(
        self, params: Optional[APIParams] = None
    ) -> int:
        """Checks graph negentropy.

        Args:
            params (APIParams, optional): additional params for the API like pagination

        Returns:
            Int: negentropy
            Pagination: pagination info
        """
        res = await self._c._get(
            f"/cyber/rank/v1beta1/negentropy", params
        )
        return int(res['negentropy'])

    async def particle_negentropy(
        self, particle: str,  params: Optional[APIParams] = None
    ) -> int:
        """Checks particle negentropy.

        Args:
            particle (str): cid
            params (APIParams, optional): additional params for the API like pagination

        Returns:
            Int: negentropy
            Pagination: pagination info
        """
        res = await self._c._get(
            f"/cyber/rank/v1beta1/negentropy/{particle}", params
        )
        return int(res['entropy'])

    async def particle_backlinks(
        self, particle: str,  params: Optional[APIParams] = None
    ) -> (list, dict):
        """Checks particle backlinks.

        Args:
            particle (str): cid
            params (APIParams, optional): additional params for the API like pagination

        Returns:
            List: backlinks
            Pagination: pagination info
        """
        res = await self._c._get(
            f"/cyber/rank/v1beta1/rank/backlinks/{particle}", params
        )
        return res['result'], res.get("pagination")

    async def params(
        self, params: Optional[APIParams] = None
    ) -> dict:
        """Get rank module params.

        Args:
            params (APIParams, optional): additional params for the API like pagination

        Returns:
            Dict: params
            Pagination: pagination info
        """
        res = await self._c._get(
            f"/cyber/rank/v1beta1/rank/params", params
        )
        return res['params']

    async def particle_rank(
        self, particle: str, params: Optional[APIParams] = None
    ) -> int:
        """Get particle rank.

        Args:
            particle (str): cid
            params (APIParams, optional): additional params for the API like pagination

        Returns:
            Int: rank
            Pagination: pagination info
        """
        res = await self._c._get(
            f"/cyber/rank/v1beta1/rank/rank/{particle}", params
        )
        return int(res['rank'])

    async def particle_search(
        self, particle: str, params: Optional[APIParams] = None
    ) -> (list, dict):
        """Get particle cyberlinked particles.

        Args:
            particle (str): cid
            params (APIParams, optional): additional params for the API like pagination

        Returns:
            List: result
            Pagination: pagination info
        """
        res = await self._c._get(
            f"/cyber/rank/v1beta1/rank/search/{particle}", params
        )
        return res['result'], res.get("pagination")

    async def top_particles(
        self, page: int, per_page: int, params: Optional[APIParams] = None
    ) -> (list, dict):
        """Get top particles.

        Args:
            page (int): page number
            per_page (int): amount of particles per page
            params (APIParams, optional): additional params for the API like pagination

        Returns:
            List: result
            Pagination: pagination info
        """
        res = await self._c._get(
            f"/cyber/rank/v1beta1/rank/top?page={page}&per_page={per_page}", params
        )
        return res['result'], res.get("pagination")


class RankAPI(AsyncRankAPI):
    @sync_bind(AsyncRankAPI.is_cyberlink_exist)
    def is_cyberlink_exist(
        self, object_from: str, object_to: str
    ) -> bool:
        pass

    is_cyberlink_exist.__doc__ = AsyncRankAPI.is_cyberlink_exist.__doc__

    @sync_bind(AsyncRankAPI.is_neurons_cyberlink_exist)
    def is_neurons_cyberlink_exist(
        self, neuron: AccAddress, object_from: str, object_to: str, params: Optional[APIParams] = None
    ) -> bool:
        pass

    is_neurons_cyberlink_exist.__doc__ = AsyncRankAPI.is_neurons_cyberlink_exist.__doc__

    @sync_bind(AsyncRankAPI.neuron_karma)
    def neuron_karma(
            self, neuron: AccAddress, params: Optional[APIParams] = None
    ) -> int:
        pass

    neuron_karma.__doc__ = AsyncRankAPI.neuron_karma.__doc__

    @sync_bind(AsyncRankAPI.negentropy)
    def negentropy(
            self, params: Optional[APIParams] = None
    ) -> int:
        pass

    negentropy.__doc__ = AsyncRankAPI.negentropy.__doc__

    @sync_bind(AsyncRankAPI.particle_negentropy)
    def particle_negentropy(
            self, particle: str, params: Optional[APIParams] = None
    ) -> int:
        pass

    particle_negentropy.__doc__ = AsyncRankAPI.particle_negentropy.__doc__

    @sync_bind(AsyncRankAPI.particle_backlinks)
    def particle_backlinks(
            self, particle: str, params: Optional[APIParams] = None
    ) -> dict:
        pass

    particle_backlinks.__doc__ = AsyncRankAPI.particle_backlinks.__doc__

    @sync_bind(AsyncRankAPI.params)
    def params(
            self, params: Optional[APIParams] = None
    ) -> dict:
        pass

    params.__doc__ = AsyncRankAPI.params.__doc__

    @sync_bind(AsyncRankAPI.particle_rank)
    def particle_rank(
            self, particle: str, params: Optional[APIParams] = None
    ) -> int:
        pass

    particle_rank.__doc__ = AsyncRankAPI.particle_rank.__doc__

    @sync_bind(AsyncRankAPI.particle_search)
    def particle_search(
            self, particle: str, params: Optional[APIParams] = None
    ) -> (list, dict):
        pass

    particle_search.__doc__ = AsyncRankAPI.top_particles.__doc__

    @sync_bind(AsyncRankAPI.top_particles)
    def top_particles(
            self, page: int, per_page: int, params: Optional[APIParams] = None
    ) -> (list, dict):
        pass

    top_particles.__doc__ = AsyncRankAPI.top_particles.__doc__

