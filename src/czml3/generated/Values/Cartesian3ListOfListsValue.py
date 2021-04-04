# generated by datamodel-codegen:
#   filename:  Values/Cartesian3ListOfListsValue.json
#   timestamp: 2021-04-04T10:04:35+00:00

from __future__ import annotations

from typing import List

import BaseCZMLObject
from pydantic import Field


class Cartesian3ListOfLists(BaseCZMLObject):
    """
    A list of lists of three-dimensional Cartesian values specified as `[X, Y, Z, X, Y, Z, ...]`.
    """

    __root__: List[List] = Field(
        ...,
        description='A list of lists of three-dimensional Cartesian values specified as `[X, Y, Z, X, Y, Z, ...]`.',
        title='Cartesian3ListOfLists',
    )
