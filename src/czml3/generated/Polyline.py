# generated by datamodel-codegen:
#   filename:  Polyline.json
#   timestamp: 2021-04-04T10:04:35+00:00

from __future__ import annotations

from typing import Optional

import BaseCZMLObject
from pydantic import Field

from . import (
    ArcType,
    Boolean,
    ClassificationType,
    DistanceDisplayCondition,
    Double,
    Integer,
    PolylineMaterial,
    PositionList,
    ShadowMode,
)


class Polyline(BaseCZMLObject):
    """
    A polyline, which is a line in the scene composed of multiple segments.
    """

    show: Optional[Boolean] = Field(
        True, description='Whether or not the polyline is shown.'
    )
    positions: Optional[PositionList] = Field(
        None,
        description='The array of positions defining the polyline as a line strip.',
    )
    arcType: Optional[ArcType] = Field(
        'GEODESIC',
        description='The type of arc that should connect the positions of the polyline.',
    )
    width: Optional[Double] = Field(1.0, description='The width of the polyline.')
    granularity: Optional[Double] = Field(
        'π / 180.0', description='The sampling distance, in radians.'
    )
    material: Optional[PolylineMaterial] = Field(
        'solid white', description='The material to use to draw the polyline.'
    )
    followSurface: Optional[Boolean] = Field(
        True,
        description='Whether or not the positions are connected as great arcs (the default) or as straight lines. This property has been superseded by `arcType`, which should be used instead.',
    )
    shadows: Optional[ShadowMode] = Field(
        'DISABLED', description='Whether or not the polyline casts or receives shadows.'
    )
    depthFailMaterial: Optional[PolylineMaterial] = Field(
        None,
        description='The material to use to draw the polyline when it is below the terrain.',
    )
    distanceDisplayCondition: Optional[DistanceDisplayCondition] = Field(
        None,
        description='The display condition specifying at what distance from the camera this polyline will be displayed.',
    )
    clampToGround: Optional[Boolean] = Field(
        False,
        description='Whether or not the polyline should be clamped to the ground.',
    )
    classificationType: Optional[ClassificationType] = Field(
        'BOTH',
        description='Whether a classification affects terrain, 3D Tiles, or both.',
    )
    zIndex: Optional[Integer] = Field(
        '0',
        description='The z-index of the polyline, used for ordering ground geometry. Only has an effect if the polyline is constant, and `clampToGround` is true.',
    )
