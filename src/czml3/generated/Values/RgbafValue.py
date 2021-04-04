# generated by datamodel-codegen:
#   filename:  Values/RgbafValue.json
#   timestamp: 2021-04-04T10:04:35+00:00

from __future__ import annotations

from typing import List

import BaseCZMLObject
from pydantic import Field


class Rgbaf(BaseCZMLObject):
    """
    A color specified as an array of color components `[Red, Green, Blue, Alpha]` where each component is in the range 0.0-1.0. If the array has four elements, the color is constant. If it has five or more elements, they are time-tagged samples arranged as `[Time, Red, Green, Blue, Alpha, Time, Red, Green, Blue, Alpha, ...]`, where Time is an ISO 8601 date and time string or seconds since epoch.
    """

    __root__: List = Field(
        ...,
        description='A color specified as an array of color components `[Red, Green, Blue, Alpha]` where each component is in the range 0.0-1.0. If the array has four elements, the color is constant. If it has five or more elements, they are time-tagged samples arranged as `[Time, Red, Green, Blue, Alpha, Time, Red, Green, Blue, Alpha, ...]`, where Time is an ISO 8601 date and time string or seconds since epoch.',
        title='Rgbaf',
    )
