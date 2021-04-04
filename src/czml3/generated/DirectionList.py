# generated by datamodel-codegen:
#   filename:  DirectionList.json
#   timestamp: 2021-04-04T10:04:35+00:00

from __future__ import annotations

from typing import List, Optional, Union

import BaseCZMLObject
from pydantic import Field

from .DeletableProperty import DeletableProperty
from .Values import (
    Cartesian3ListValue,
    SphericalListValue,
    UnitCartesian3ListValue,
    UnitSphericalListValue,
)


class DirectionList1(DeletableProperty):
    """
    A list of directions.
    """

    spherical: Optional[SphericalListValue.SphericalList] = Field(
        None,
        description='The list of directions specified as spherical values `[Clock, Cone, Magnitude, Clock, Cone, Magnitude, ...]`, with angles in radians and magnitude in meters. The clock angle is measured in the XY plane from the positive X axis toward the positive Y axis. The cone angle is the angle from the positive Z axis toward the negative Z axis.',
    )
    unitSpherical: Optional[UnitSphericalListValue.UnitSphericalList] = Field(
        None,
        description='The list of directions specified as unit spherical values `[Clock, Cone, Clock, Cone, ...]`, in radians. The clock angle is measured in the XY plane from the positive X axis toward the positive Y axis. The cone angle is the angle from the positive Z axis toward the negative Z axis.',
    )
    cartesian: Optional[Cartesian3ListValue.Cartesian3List] = Field(
        None,
        description='The list of directions specified as three-dimensional Cartesian values `[X, Y, Z, X, Y, Z, ...]`, in world coordinates in meters.',
    )
    unitCartesian: Optional[UnitCartesian3ListValue.UnitCartesian3List] = Field(
        None,
        description='The list of directions specified as three-dimensional unit magnitude Cartesian values, `[X, Y, Z, X, Y, Z, ...]`, in world coordinates in meters.',
    )


class DirectionList(BaseCZMLObject):
    """
    A list of directions.
    """

    __root__: Union[List[DirectionList1], DirectionList1] = Field(
        ..., description='A list of directions.', title='DirectionList'
    )
