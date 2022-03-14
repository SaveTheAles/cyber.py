from cyber_sdk.core.distribution.proposals import CommunityPoolSpendProposal
from cyber_sdk.core.gov.proposals import TextProposal
from cyber_sdk.core.params.proposals import ParameterChangeProposal

from .base import create_demux

parse_content = create_demux(
    [
        CommunityPoolSpendProposal,
        TextProposal,
        ParameterChangeProposal,
    ]
)
