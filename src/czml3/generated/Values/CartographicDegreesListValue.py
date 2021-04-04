# generated by datamodel-codegen:
#   filename:  Values/CartographicDegreesListValue.json
#   timestamp: 2021-04-04T10:04:35+00:00

from __future__ import annotations

from typing import List

import BaseCZMLObject
from pydantic import Field


class CartographicDegreesList(BaseCZMLObject):
    """
    A list of geodetic, WGS84 positions specified as `[Longitude, Latitude, Height, Longitude, Latitude, Height, ...]`, where Longitude and Latitude are in degrees and Height is in meters.
    """

    __root__: List[float] = Field(
        ...,
        description='A list of geodetic, WGS84 positions specified as `[Longitude, Latitude, Height, Longitude, Latitude, Height, ...]`, where Longitude and Latitude are in degrees and Height is in meters.',
        title='CartographicDegreesList',
    )
