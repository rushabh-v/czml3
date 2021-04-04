# generated by datamodel-codegen:
#   filename:  Point.json
#   timestamp: 2021-04-04T10:04:35+00:00

from __future__ import annotations

from typing import Optional

import BaseCZMLObject
from pydantic import Field

from . import (
    Boolean,
    Color,
    DistanceDisplayCondition,
    Double,
    HeightReference,
    NearFarScalar,
)


class Point(BaseCZMLObject):
    """
    A point, or viewport-aligned circle.
    """

    show: Optional[Boolean] = Field(
        True, description='Whether or not the point is shown.'
    )
    pixelSize: Optional[Double] = Field(
        1.0, description='The size of the point, in pixels.'
    )
    heightReference: Optional[HeightReference] = Field(
        'NONE',
        description='The height reference of the point, which indicates if the position is relative to terrain or not.',
    )
    color: Optional[Color] = Field('white', description='The color of the point.')
    outlineColor: Optional[Color] = Field(
        'black', description='The color of the outline of the point.'
    )
    outlineWidth: Optional[Double] = Field(
        0.0, description='The width of the outline of the point.'
    )
    scaleByDistance: Optional[NearFarScalar] = Field(
        None,
        description="How the point's scale should change based on the point's distance from the camera. This scalar value will be multiplied by `pixelSize`.",
    )
    translucencyByDistance: Optional[NearFarScalar] = Field(
        None,
        description="How the point's translucency should change based on the point's distance from the camera. This scalar value should range from 0 to 1.",
    )
    distanceDisplayCondition: Optional[DistanceDisplayCondition] = Field(
        None,
        description='The display condition specifying the distance from the camera at which this point will be displayed.',
    )
    disableDepthTestDistance: Optional[Double] = Field(
        0.0,
        description='The distance from the camera at which to disable the depth test. This can be used to prevent clipping against terrain, for example. When set to zero, the depth test is always applied. When set to Infinity, the depth test is never applied.',
    )
