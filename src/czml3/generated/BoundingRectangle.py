# generated by datamodel-codegen:
#   filename:  BoundingRectangle.json
#   timestamp: 2021-03-29T05:46:25+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field

from . import CustomProperty, LabelStyle


class BoundingRectangle(BaseModel):
    """
    A bounding rectangle specified by a corner, width and height.
    """

    boundingRectangle: Optional[CustomProperty.BoundingRectangleValue] = Field(
        None, description='The bounding rectangle specified as `[X, Y, Width, Height]`.'
    )
    reference: Optional[LabelStyle.ReferenceValue] = Field(
        None,
        description='The bounding rectangle specified as a reference to another property.',
    )
