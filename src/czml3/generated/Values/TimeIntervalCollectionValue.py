# generated by datamodel-codegen:
#   filename:  Values/TimeIntervalCollectionValue.json
#   timestamp: 2021-04-04T10:04:35+00:00

from __future__ import annotations

from typing import Any, List, Union

import BaseCZMLObject
from pydantic import Field


class TimeIntervalCollection(BaseCZMLObject):
    __root__: Union[List[Any], str] = Field(
        ...,
        description='A collection of time intervals, specified in ISO8601 interval format.',
    )
