# generated by datamodel-codegen:
#   filename:  Values/StripeOrientationValue.json
#   timestamp: 2021-04-04T10:04:35+00:00

from __future__ import annotations

import BaseCZMLObject
from pydantic import Field


class StripeOrientation(BaseCZMLObject):
    __root__: str = Field(
        ..., description='The orientation of stripes in the stripe material.'
    )