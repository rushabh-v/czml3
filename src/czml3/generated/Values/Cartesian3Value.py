# generated by datamodel-codegen:
#   filename:  Values/Cartesian3Value.json
#   timestamp: 2021-03-29T05:46:25+00:00

from __future__ import annotations

from typing import List

from pydantic import BaseModel, Field


class Cartesian3(BaseModel):
    """
    A three-dimensional Cartesian value specified as `[X, Y, Z]`. If the array has three elements, the value is constant. If it has four or more elements, they are time-tagged samples arranged as `[Time, X, Y, Z, Time, X, Y, Z, ...]`, where Time is an ISO 8601 date and time string or seconds since epoch.
    """

    __root__: List = Field(
        ...,
        description='A three-dimensional Cartesian value specified as `[X, Y, Z]`. If the array has three elements, the value is constant. If it has four or more elements, they are time-tagged samples arranged as `[Time, X, Y, Z, Time, X, Y, Z, ...]`, where Time is an ISO 8601 date and time string or seconds since epoch.',
        title='Cartesian3',
    )
