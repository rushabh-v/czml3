# generated by datamodel-codegen:
#   filename:  InterpolatableProperty.json
#   timestamp: 2021-04-04T10:04:35+00:00

from __future__ import annotations

from datetime import datetime
from typing import Optional

import BaseCZMLObject
from pydantic import Field


class InterpolatableProperty(BaseCZMLObject):
    """
    The base schema for a property whose value may be determined by interpolating over provided time-tagged samples.
    """

    epoch: Optional[datetime] = Field(
        None,
        description='The epoch to use for times specified as seconds since an epoch.',
    )
    interpolationAlgorithm: Optional[str] = Field(
        'LINEAR',
        description='The interpolation algorithm to use when interpolating. Valid values are "LINEAR", "LAGRANGE", and "HERMITE".',
    )
    interpolationDegree: Optional[float] = Field(
        1, description='The degree of interpolation to use when interpolating.'
    )
    forwardExtrapolationType: Optional[str] = Field(
        'NONE',
        description='The type of extrapolation to perform when a value is requested at a time after any available samples. Valid values are "NONE", "HOLD", and "EXTRAPOLATE".',
    )
    forwardExtrapolationDuration: Optional[float] = Field(
        0.0,
        description='The amount of time to extrapolate forward before the property becomes undefined. A value of 0 will extrapolate forever.',
    )
    backwardExtrapolationType: Optional[str] = Field(
        'NONE',
        description='The type of extrapolation to perform when a value is requested at a time before any available samples. Valid values are "NONE", "HOLD", and "EXTRAPOLATE".',
    )
    backwardExtrapolationDuration: Optional[float] = Field(
        0.0,
        description='The amount of time to extrapolate backward before the property becomes undefined. A value of 0 will extrapolate forever.',
    )