# generated by datamodel-codegen:
#   filename:  Polygon.json
#   timestamp: 2021-04-04T10:04:35+00:00

from __future__ import annotations

from typing import Optional

import BaseCZMLObject
from pydantic import Field

from . import (
    ArcType,
    Boolean,
    ClassificationType,
    Color,
    DistanceDisplayCondition,
    Double,
    HeightReference,
    Integer,
    Material,
    PositionList,
    PositionListOfLists,
    ShadowMode,
)


class Polygon(BaseCZMLObject):
    """
    A polygon, which is a closed figure on the surface of the Earth.
    """

    show: Optional[Boolean] = Field(
        True, description='Whether or not the polygon is shown.'
    )
    positions: Optional[PositionList] = Field(
        None, description='The array of positions defining a simple polygon.'
    )
    holes: Optional[PositionListOfLists] = Field(
        None,
        description='The array of arrays of positions defining holes in the polygon.',
    )
    arcType: Optional[ArcType] = Field(
        'GEODESIC',
        description='The type of arc that should connect the positions of the polygon.',
    )
    height: Optional[Double] = Field(
        0.0, description='The height of the polygon when `perPositionHeight` is false.'
    )
    heightReference: Optional[HeightReference] = Field(
        'NONE',
        description='The height reference of the polygon, which indicates if `height` is relative to terrain or not.',
    )
    extrudedHeight: Optional[Double] = Field(
        None, description='The extruded height of the polygon.'
    )
    extrudedHeightReference: Optional[HeightReference] = Field(
        'NONE',
        description='The extruded height reference of the polygon, which indicates if `extrudedHeight` is relative to terrain or not.',
    )
    stRotation: Optional[Double] = Field(
        0.0,
        description='The rotation of any applied texture. A positive rotation is counter-clockwise.',
    )
    granularity: Optional[Double] = Field(
        'π / 180.0', description='The sampling distance, in radians.'
    )
    fill: Optional[Boolean] = Field(
        True, description='Whether or not the polygon is filled.'
    )
    material: Optional[Material] = Field(
        'solid white', description='The material to use to fill the polygon.'
    )
    outline: Optional[Boolean] = Field(
        False, description='Whether or not the polygon is outlined.'
    )
    outlineColor: Optional[Color] = Field(
        'black', description='The color of the polygon outline.'
    )
    outlineWidth: Optional[Double] = Field(
        1.0, description='The width of the polygon outline.'
    )
    perPositionHeight: Optional[Boolean] = Field(
        False,
        description='Whether to use the height of each position to define the polygon or to use `height` as a constant height above the surface.',
    )
    closeTop: Optional[Boolean] = Field(
        True, description='Whether to close the top of the polygon.'
    )
    closeBottom: Optional[Boolean] = Field(
        True, description='Whether to close the bottom of the polygon.'
    )
    shadows: Optional[ShadowMode] = Field(
        'DISABLED', description='Whether or not the polygon casts or receives shadows.'
    )
    distanceDisplayCondition: Optional[DistanceDisplayCondition] = Field(
        None,
        description='The display condition specifying the distance from the camera at which this polygon will be displayed.',
    )
    classificationType: Optional[ClassificationType] = Field(
        'BOTH',
        description='Whether a classification affects terrain, 3D Tiles, or both.',
    )
    zIndex: Optional[Integer] = Field(
        '0',
        description='The z-index of the polygon, used for ordering ground geometry. Only has an effect if the polygon is constant, and `height` and `extrudedHeight` are not specified.',
    )
