# generated by datamodel-codegen:
#   filename:  Box.json
#   timestamp: 2021-03-29T05:46:25+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field

from . import Cylinder, LabelStyle, Position


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


class Box(BaseModel):
    """
    A box, which is a closed rectangular cuboid.
    """

    show: Optional[Cylinder.Boolean] = Field(
        True, description='Whether or not the box is shown.'
    )
    dimensions: Optional[BoxDimensions] = Field(
        None, description='The dimensions of the box.'
    )
    heightReference: Optional[Cylinder.HeightReference] = Field(
        'NONE',
        description='The height reference of the box, which indicates if the position is relative to terrain or not.',
    )
    fill: Optional[Cylinder.Boolean] = Field(
        True, description='Whether or not the box is filled.'
    )
    material: Optional[Cylinder.Material] = Field(
        'solid white', description='The material to display on the surface of the box.'
    )
    outline: Optional[Cylinder.Boolean] = Field(
        False, description='Whether or not the box is outlined.'
    )
    outlineColor: Optional[Cylinder.Color] = Field(
        'black', description='The color of the box outline.'
    )
    outlineWidth: Optional[Cylinder.Double] = Field(
        1.0, description='The width of the box outline.'
    )
    shadows: Optional[Cylinder.ShadowMode] = Field(
        'DISABLED', description='Whether or not the box casts or receives shadows.'
    )
    distanceDisplayCondition: Optional[Cylinder.DistanceDisplayCondition] = Field(
        None,
        description='The display condition specifying the distance from the camera at which this box will be displayed.',
    )
