# generated by datamodel-codegen:
#   filename:  Extensions/AGI/SensorVolumePortionToDisplayValue.json
#   timestamp: 2021-04-04T10:04:35+00:00

from __future__ import annotations

import BaseCZMLObject
from pydantic import Field


class SensorVolumePortionToDisplay(BaseCZMLObject):
    __root__: str = Field(..., description='What part of a sensor should be displayed.')