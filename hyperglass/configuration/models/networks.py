"""
Defines models for Networks config variables.

Imports config variables and overrides default class attributes.

Validates input for overridden parameters.
"""

# Third Party Imports
from pydantic import BaseSettings

# Project Imports
from hyperglass.configuration.models._utils import clean_name


class Network(BaseSettings):
    """Model for per-network/asn config in devices.yaml"""

    display_name: str


class Networks(BaseSettings):
    """Base model for networks class"""

    @classmethod
    def import_params(cls, input_params):
        """
        Imports passed dict from YAML config, removes unsupported
        characters from device names, dynamically sets attributes for
        the credentials class.
        """
        obj = Networks()
        networks = {}
        for (netname, params) in input_params.items():
            netname = clean_name(netname)
            setattr(Networks, netname, Network(**params))
            networks.update({netname: Network(**params).dict()})
        Networks.networks = networks
        return obj

    class Config:
        """Pydantic Config"""

        validate_all = True
        validate_assignment = True
