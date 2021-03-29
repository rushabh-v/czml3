# generated by datamodel-codegen:
#   filename:  EyeOffset.json
#   timestamp: 2021-03-29T05:46:25+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field

from . import LabelStyle, Position


class EyeOffset(BaseModel):
    """
    An offset in eye coordinates which can optionally vary over time. Eye coordinates are a left-handed coordinate system where the X-axis points toward the viewer's right, the Y-axis poitns up, and the Z-axis points into the screen.
    """

    cartesian: Optional[Position.Cartesian3Value] = Field(
        None,
        description='The eye offset specified as a three-dimensional Cartesian value `[X, Y, Z]`, in eye coordinates in meters. If the array has three elements, the eye offset is constant. If it has four or more elements, they are time-tagged samples arranged as `[Time, X, Y, Z, Time, X, Y, Z, ...]`, where Time is an ISO 8601 date and time string or seconds since epoch.',
    )
    reference: Optional[LabelStyle.ReferenceValue] = Field(
        None, description='The eye offset specified as a reference to another property.'
    )
