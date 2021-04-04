# generated by datamodel-codegen:
#   filename:  Model.json
#   timestamp: 2021-04-04T10:04:35+00:00

from __future__ import annotations

from typing import Optional

import BaseCZMLObject
from pydantic import Field

from . import (
    Articulations,
    Boolean,
    Color,
    ColorBlendMode,
    DistanceDisplayCondition,
    Double,
    HeightReference,
    NodeTransformations,
    ShadowMode,
    Uri,
)


class Model(BaseCZMLObject):
    """
    A 3D model.
    """

    show: Optional[Boolean] = Field(
        True, description='Whether or not the model is shown.'
    )
    gltf: Optional[Uri] = Field(
        None,
        description='The URI of a <a href="https://github.com/KhronosGroup/glTF">glTF</a> model. For broadest client compatibility, the URI should be accessible via Cross-Origin Resource Sharing (CORS). The URI may also be a <a href="https://developer.mozilla.org/en/data_URIs">data URI</a>.',
    )
    scale: Optional[Double] = Field(1.0, description='The scale of the model.')
    minimumPixelSize: Optional[Double] = Field(
        0.0,
        description='The approximate minimum pixel size of the model regardless of zoom.',
    )
    maximumScale: Optional[Double] = Field(
        None,
        description='The maximum scale size of the model. This is used as an upper limit for `minimumPixelSize`.',
    )
    incrementallyLoadTextures: Optional[Boolean] = Field(
        True,
        description='Whether or not the model can be rendered before all textures have loaded.',
    )
    runAnimations: Optional[Boolean] = Field(
        True,
        description='Whether or not to run all animations defined in the glTF model.',
    )
    shadows: Optional[ShadowMode] = Field(
        'ENABLED', description='Whether or not the model casts or receives shadows.'
    )
    heightReference: Optional[HeightReference] = Field(
        'NONE',
        description='The height reference of the model, which indicates if the position is relative to terrain or not.',
    )
    silhouetteColor: Optional[Color] = Field(
        'red', description='The color of the silhouette drawn around the model.'
    )
    silhouetteSize: Optional[Double] = Field(
        0.0,
        description='The size, in pixels, of the silhouette drawn around the model.',
    )
    color: Optional[Color] = Field(
        'white', description="The color to blend with the model's rendered color."
    )
    colorBlendMode: Optional[ColorBlendMode] = Field(
        'HIGHLIGHT',
        description="The mode to use for blending between `color` and the model's color.",
    )
    colorBlendAmount: Optional[Double] = Field(
        0.5,
        description="The color strength when `colorBlendMode` is `MIX`. A value of 0.0 results in the model's rendered color while a value of 1.0 results in a solid color, with any value in-between resulting in a mix of the two.",
    )
    distanceDisplayCondition: Optional[DistanceDisplayCondition] = Field(
        None,
        description='The display condition specifying at what distance from the camera this model will be displayed.',
    )
    nodeTransformations: Optional[NodeTransformations] = None
    articulations: Optional[Articulations] = None
