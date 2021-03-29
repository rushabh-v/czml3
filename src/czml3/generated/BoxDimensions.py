# generated by datamodel-codegen:
#   filename:  BoxDimensions.json
#   timestamp: 2021-03-29T05:46:25+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field

from . import LabelStyle, Position


class BoxDimensions(BaseModel):
    """
    The width, depth, and height of a box.
    """

    cartesian: Optional[Position.Cartesian3Value] = Field(
        None,
        description='The dimensions specified as a three-dimensional Cartesian value `[X, Y, Z]`, with X representing width, Y representing depth, and Z representing height, in world coordinates in meters.',
    )
    reference: Optional[LabelStyle.ReferenceValue] = Field(
        None, description='The dimensions specified as a reference to another property.'
    )
