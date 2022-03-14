from cyber_sdk.client.lcd import LCDClient, PaginationOptions

bostrom = LCDClient(
    url="https://lcd.space-pussy-1.cybernode.ai/",
    chain_id="space-pussy-1",
)

pagopt = PaginationOptions(limit=3, count_total=True, reverse=True)


def test_signing_infos():
    result, _ = bostrom.slashing.signing_infos()
    assert result is not None


def test_signing_infos_with_pagination():
    result, _ = bostrom.slashing.signing_infos(pagopt)
    assert result is not None


def test_signing_info():
    result = bostrom.slashing.signing_info(
        "bostromvalcons1lcjwqqp8sk86laggdagvk2lez0v3helfztsarh"
    )
    assert result is not None


def test_parameters():
    result = bostrom.slashing.parameters()
    assert result.get("signed_blocks_window")
    assert result.get("min_signed_per_window")
    assert result.get("downtime_jail_duration")
    assert result.get("slash_fraction_double_sign")
    assert result.get("slash_fraction_downtime")
