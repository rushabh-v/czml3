# generated by datamodel-codegen:
#   filename:  Values/SphericalValue.json
#   timestamp: 2021-04-04T10:04:35+00:00

from __future__ import annotations

from typing import List

import BaseCZMLObject
from pydantic import Field


class Spherical(BaseCZMLObject):
    """
    A spherical value `[Clock, Cone, Magnitude]`, with angles in radians and magnitude in meters. The clock angle is measured in the XY plane from the positive X axis toward the positive Y axis. The cone angle is the angle from the positive Z axis toward the negative Z axis. If the array has three elements, the value is constant. If it has four or more elements, they are time-tagged samples arranged as `[Time, Clock, Cone, Magnitude, Time, Clock, Cone, Magnitude, ...]`, where Time is an ISO 8601 date and time string or seconds since epoch.
    """

    __root__: List = Field(
        ...,
        description='A spherical value `[Clock, Cone, Magnitude]`, with angles in radians and magnitude in meters. The clock angle is measured in the XY plane from the positive X axis toward the positive Y axis. The cone angle is the angle from the positive Z axis toward the negative Z axis. If the array has three elements, the value is constant. If it has four or more elements, they are time-tagged samples arranged as `[Time, Clock, Cone, Magnitude, Time, Clock, Cone, Magnitude, ...]`, where Time is an ISO 8601 date and time string or seconds since epoch.',
        title='Spherical',
    )