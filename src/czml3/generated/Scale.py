# generated by datamodel-codegen:
#   filename:  Scale.json
#   timestamp: 2021-03-29T05:46:25+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field

from . import LabelStyle, Position


class Scale(BaseModel):
    """
    A scaling factor which can optionally vary over time.
    """

    cartesian: Optional[Position.Cartesian3Value] = Field(
        None,
        description='The scale specified as a three-dimensional Cartesian value `[X, Y, Z]`.',
    )
    reference: Optional[LabelStyle.ReferenceValue] = Field(
        None, description='The scale specified as a reference to another property.'
    )
