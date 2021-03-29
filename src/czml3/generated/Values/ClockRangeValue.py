# generated by datamodel-codegen:
#   filename:  Values/ClockRangeValue.json
#   timestamp: 2021-03-29T05:46:25+00:00

from __future__ import annotations

from pydantic import BaseModel, Field


class ClockRange(BaseModel):
    __root__: str = Field(
        ...,
        description='The behavior of a clock when its current time reaches its start or end time.',
    )
