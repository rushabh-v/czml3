# generated by datamodel-codegen:
#   filename:  ValueProperties/IntegerValueProperty.json
#   timestamp: 2021-04-04T10:04:35+00:00

from __future__ import annotations

from typing import Any

import BaseCZMLObject
from pydantic import Field


class IntegerValueProperty(BaseCZMLObject):
    __root__: Any = Field(
        ...,
        description='The base schema for a property whose value may be written as an integer.',
    )
