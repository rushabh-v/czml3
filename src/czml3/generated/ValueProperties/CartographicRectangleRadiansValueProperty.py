# generated by datamodel-codegen:
#   filename:  ValueProperties/CartographicRectangleRadiansValueProperty.json
#   timestamp: 2021-04-04T10:04:35+00:00

from __future__ import annotations

from typing import Any

import BaseCZMLObject
from pydantic import Field


class CartographicRectangleRadiansValueProperty(BaseCZMLObject):
    __root__: Any = Field(
        ...,
        description='The base schema for a property whose value may be written as a two-dimensional region specified as `[WestLongitude, SouthLatitude, EastLongitude, NorthLatitude]`, with values in radians.',
    )
