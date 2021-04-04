# generated by datamodel-codegen:
#   filename:  AlignedAxis.json
#   timestamp: 2021-04-04T10:04:35+00:00

from __future__ import annotations

from typing import List, Optional, Union

import BaseCZMLObject
from pydantic import Field

from .DeletableProperty import DeletableProperty
from .InterpolatableProperty import InterpolatableProperty
from .Values import (
    ReferenceValue,
    UnitCartesian3Value,
    UnitSphericalValue,
    VelocityReferenceValue,
)


class AlignedAxis1(InterpolatableProperty, DeletableProperty):
    """
    An aligned axis represented by a unit vector which can optionally vary over time.
    """

    unitCartesian: Optional[UnitCartesian3Value.UnitCartesian3] = Field(
        None,
        description='The axis specified as a three-dimensional unit magnitude Cartesian value `[X, Y, Z]`, in world coordinates.',
    )
    unitSpherical: Optional[UnitSphericalValue.UnitSpherical] = Field(
        None,
        description='The axis specified as a unit spherical value `[Clock, Cone]`, in radians. The clock angle is measured in the XY plane from the positive X axis toward the positive Y axis. The cone angle is the angle from the positive Z axis toward the negative Z axis.',
    )
    reference: Optional[ReferenceValue.Reference] = Field(
        None, description='The axis specified as a reference to another property.'
    )
    velocityReference: Optional[VelocityReferenceValue.VelocityReference] = Field(
        None,
        description='The axis specified as the normalized velocity vector of a position property. The reference must be to a `position` property.',
    )


class AlignedAxis(BaseCZMLObject):
    """
    An aligned axis represented by a unit vector which can optionally vary over time.
    """

    __root__: Union[List[AlignedAxis1], AlignedAxis1] = Field(
        ...,
        description='An aligned axis represented by a unit vector which can optionally vary over time.',
        title='AlignedAxis',
    )