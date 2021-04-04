# generated by datamodel-codegen:
#   filename:  Values/VerticalOriginValue.json
#   timestamp: 2021-04-04T10:04:35+00:00

from __future__ import annotations

import BaseCZMLObject
from pydantic import Field


class VerticalOrigin(BaseCZMLObject):
    __root__: str = Field(
        ...,
        description="The vertical location of an origin relative to an object's position.",
    )
