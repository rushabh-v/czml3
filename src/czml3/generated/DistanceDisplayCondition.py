# generated by datamodel-codegen:
#   filename:  DistanceDisplayCondition.json
#   timestamp: 2021-04-04T10:04:35+00:00

from __future__ import annotations

from typing import List, Optional, Union

import BaseCZMLObject
from pydantic import Field

from .DeletableProperty import DeletableProperty
from .InterpolatableProperty import InterpolatableProperty
from .Values import DistanceDisplayConditionValue, ReferenceValue


class DistanceDisplayCondition1(InterpolatableProperty, DeletableProperty):
    """
    Indicates the visibility of an object based on the distance to the camera.
    """

    distanceDisplayCondition: Optional[
        DistanceDisplayConditionValue.DistanceDisplayCondition
    ] = Field(
        None,
        description='The value specified as two values `[NearDistance, FarDistance]`, with distances in meters.',
    )
    reference: Optional[ReferenceValue.Reference] = Field(
        None, description='The value specified as a reference to another property.'
    )


class DistanceDisplayCondition(BaseCZMLObject):
    """
    Indicates the visibility of an object based on the distance to the camera.
    """

    __root__: Union[List[DistanceDisplayCondition1], DistanceDisplayCondition1] = Field(
        ...,
        description='Indicates the visibility of an object based on the distance to the camera.',
        title='DistanceDisplayCondition',
    )