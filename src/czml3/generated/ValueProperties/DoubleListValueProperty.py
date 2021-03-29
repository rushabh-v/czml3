# generated by datamodel-codegen:
#   filename:  ValueProperties/DoubleListValueProperty.json
#   timestamp: 2021-03-29T05:46:25+00:00

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field


class DoubleListValueProperty(BaseModel):
    __root__: Any = Field(
        ...,
        description='The base schema for a property whose value may be written as a list of floating-point numbers.',
    )
