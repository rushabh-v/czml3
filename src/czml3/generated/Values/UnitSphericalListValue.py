# generated by datamodel-codegen:
#   filename:  Values/UnitSphericalListValue.json
#   timestamp: 2021-04-04T10:04:35+00:00

from __future__ import annotations

from typing import List

import BaseCZMLObject
from pydantic import Field


class UnitSphericalList(BaseCZMLObject):
    """
    A list of unit spherical values specified as `[Clock, Cone, Clock, Cone, ...]` angles.
    """

    __root__: List[float] = Field(
        ...,
        description='A list of unit spherical values specified as `[Clock, Cone, Clock, Cone, ...]` angles.',
        title='UnitSphericalList',
    )