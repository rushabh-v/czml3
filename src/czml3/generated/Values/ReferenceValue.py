# generated by datamodel-codegen:
#   filename:  Values/ReferenceValue.json
#   timestamp: 2021-04-04T10:04:35+00:00

from __future__ import annotations

import BaseCZMLObject
from pydantic import Field


class Reference(BaseCZMLObject):
    __root__: str = Field(
        ...,
        description='Represents a reference to another property. References can be used to specify that two properties on different objects are in fact, the same property.',
    )