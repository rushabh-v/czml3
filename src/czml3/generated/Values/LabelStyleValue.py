# generated by datamodel-codegen:
#   filename:  Values/LabelStyleValue.json
#   timestamp: 2021-03-29T05:46:25+00:00

from __future__ import annotations

from pydantic import BaseModel, Field


class LabelStyle(BaseModel):
    __root__: str = Field(..., description='The style of a label.')
