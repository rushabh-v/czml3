# generated by datamodel-codegen:
#   filename:  Values/UnitCartesian3ListValue.json
#   timestamp: 2021-04-04T10:04:35+00:00

from __future__ import annotations

from typing import List

import BaseCZMLObject
from pydantic import Field


class UnitCartesian3List(BaseCZMLObject):
    """
    A list of three-dimensional unit magnitude Cartesian values, specified as `[X, Y, Z, X, Y, Z, ...]`.
    """

    __root__: List[float] = Field(
        ...,
        description='A list of three-dimensional unit magnitude Cartesian values, specified as `[X, Y, Z, X, Y, Z, ...]`.',
        title='UnitCartesian3List',
    )