# generated by datamodel-codegen:
#   filename:  Values/UnitSphericalListValue.json
#   timestamp: 2021-03-29T05:46:25+00:00

from __future__ import annotations

from typing import List

from pydantic import BaseModel, Field


class UnitSphericalList(BaseModel):
    """
    A list of unit spherical values specified as `[Clock, Cone, Clock, Cone, ...]` angles.
    """

    __root__: List[float] = Field(
        ...,
        description='A list of unit spherical values specified as `[Clock, Cone, Clock, Cone, ...]` angles.',
        title='UnitSphericalList',
    )
