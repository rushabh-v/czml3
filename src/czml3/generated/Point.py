# generated by datamodel-codegen:
#   filename:  Point.json
#   timestamp: 2021-03-29T05:46:25+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field

from . import Cylinder, LabelStyle, NearFarScalar


class NearFarScalar(BaseModel):
    """
    A numeric value which will be linearly interpolated between two values based on an object's distance from the camera, in eye coordinates. The computed value will interpolate between the near value and the far value while the camera distance falls between the near distance and the far distance, and will be clamped to the near or far value while the distance is less than the near distance or greater than the far distance, respectively.
    """

    nearFarScalar: Optional[NearFarScalar.NearFarScalarValue] = Field(
        None,
        description='The value specified as four values `[NearDistance, NearValue, FarDistance, FarValue]`, with distances in eye coordinates in meters.',
    )
    reference: Optional[LabelStyle.ReferenceValue] = Field(
        None, description='The value specified as a reference to another property.'
    )


class Point(BaseModel):
    """
    A point, or viewport-aligned circle.
    """

    show: Optional[Cylinder.Boolean] = Field(
        True, description='Whether or not the point is shown.'
    )
    pixelSize: Optional[Cylinder.Double] = Field(
        1.0, description='The size of the point, in pixels.'
    )
    heightReference: Optional[Cylinder.HeightReference] = Field(
        'NONE',
        description='The height reference of the point, which indicates if the position is relative to terrain or not.',
    )
    color: Optional[Cylinder.Color] = Field(
        'white', description='The color of the point.'
    )
    outlineColor: Optional[Cylinder.Color] = Field(
        'black', description='The color of the outline of the point.'
    )
    outlineWidth: Optional[Cylinder.Double] = Field(
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
    distanceDisplayCondition: Optional[Cylinder.DistanceDisplayCondition] = Field(
        None,
        description='The display condition specifying the distance from the camera at which this point will be displayed.',
    )
    disableDepthTestDistance: Optional[Cylinder.Double] = Field(
        0.0,
        description='The distance from the camera at which to disable the depth test. This can be used to prevent clipping against terrain, for example. When set to zero, the depth test is always applied. When set to Infinity, the depth test is never applied.',
    )
