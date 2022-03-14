import asynctest
from aioresponses import aioresponses

from cyber_sdk.client.lcd import AsyncLCDClient, LCDClient


class TestDoSessionGet(asynctest.TestCase):
    @aioresponses()
    def test_makes_request_to_expected_url(self, mocked):
        mocked.get(
            "https://lcd.bostrom.dev/cosmos/base/tendermint/v1beta1/node_info",
            status=200,
            body='{"response": "test"}',
        )
        bostrom = LCDClient(chain_id="space-pussy-1", url="https://lcd.space-pussy-1.cybernode.ai/")

        resp = bostrom.tendermint.node_info()
        print(resp)
        assert resp == {"response": "test"}
        bostrom.session.close()

    @aioresponses()
    async def test_makes_request_to_expected_url_async(self, mocked):
        mocked.get(
            "https://lcd.bostrom.dev/cosmos/base/tendermint/v1beta1/node_info",
            status=200,
            body='{"response": "test"}',
        )
        bostrom = AsyncLCDClient(chain_id="space-pussy-1", url="https://lcd.space-pussy-1.cybernode.ai/")

        resp = await bostrom.tendermint.node_info()
        print(resp)
        assert resp == {"response": "test"}
        bostrom.session.close()


if __name__ == "__main__":
    asynctest.main()
