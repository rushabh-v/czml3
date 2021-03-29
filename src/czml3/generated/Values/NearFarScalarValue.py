# generated by datamodel-codegen:
#   filename:  Values/NearFarScalarValue.json
#   timestamp: 2021-03-29T05:46:25+00:00

from __future__ import annotations

from typing import List

from pydantic import BaseModel, Field


class NearFarScalar(BaseModel):
    """
    A near-far scalar value specified as four values `[NearDistance, NearValue, FarDistance, FarValue]`. If the array has four elements, the value is constant. If it has five or more elements, they are time-tagged samples arranged as `[Time, NearDistance, NearValue, FarDistance, FarValue, Time, NearDistance, NearValue, FarDistance, FarValue, ...]`, where Time is an ISO 8601 date and time string or seconds since epoch.
    """

    __root__: List = Field(
        ...,
        description='A near-far scalar value specified as four values `[NearDistance, NearValue, FarDistance, FarValue]`. If the array has four elements, the value is constant. If it has five or more elements, they are time-tagged samples arranged as `[Time, NearDistance, NearValue, FarDistance, FarValue, Time, NearDistance, NearValue, FarDistance, FarValue, ...]`, where Time is an ISO 8601 date and time string or seconds since epoch.',
        title='NearFarScalar',
    )
