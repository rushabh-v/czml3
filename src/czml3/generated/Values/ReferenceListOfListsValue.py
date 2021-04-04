# generated by datamodel-codegen:
#   filename:  Values/ReferenceListOfListsValue.json
#   timestamp: 2021-04-04T10:04:35+00:00

from __future__ import annotations

from typing import List

import BaseCZMLObject
from pydantic import Field


class ReferenceListOfLists(BaseCZMLObject):
    """
    A list of lists of references to other properties.
    """

    __root__: List[List] = Field(
        ...,
        description='A list of lists of references to other properties.',
        title='ReferenceListOfLists',
    )
