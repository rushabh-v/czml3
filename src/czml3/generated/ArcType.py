# generated by datamodel-codegen:
#   filename:  ArcType.json
#   timestamp: 2021-04-04T10:04:35+00:00

from __future__ import annotations

from typing import List, Optional, Union

import BaseCZMLObject
from pydantic import Field

from .DeletableProperty import DeletableProperty
from .Values import ArcTypeValue, ReferenceValue


class ArcType1(DeletableProperty):
    """
    The type of an arc.
    """

    arcType: Optional[ArcTypeValue.ArcType] = Field(None, description='The arc type.')
    reference: Optional[ReferenceValue.Reference] = Field(
        None, description='The arc type specified as a reference to another property.'
    )


class ArcType(BaseCZMLObject):
    """
    The type of an arc.
    """

    __root__: Union[List[ArcType1], ArcType1] = Field(
        ..., description='The type of an arc.', title='ArcType'
    )