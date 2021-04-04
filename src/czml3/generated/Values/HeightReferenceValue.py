# generated by datamodel-codegen:
#   filename:  Values/HeightReferenceValue.json
#   timestamp: 2021-04-04T10:04:35+00:00

from __future__ import annotations

import BaseCZMLObject
from pydantic import Field


class HeightReference(BaseCZMLObject):
    __root__: str = Field(
        ...,
        description="The height reference of an object, which indicates if the object's position is relative to terrain or not.",
    )
