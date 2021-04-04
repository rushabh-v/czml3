# generated by datamodel-codegen:
#   filename:  ShadowMode.json
#   timestamp: 2021-04-04T10:04:35+00:00

from __future__ import annotations

from typing import List, Optional, Union

import BaseCZMLObject
from pydantic import Field

from .DeletableProperty import DeletableProperty
from .Values import ReferenceValue, ShadowModeValue


class ShadowMode1(DeletableProperty):
    """
    Whether or not an object casts or receives shadows from each light source when shadows are enabled.
    """

    shadowMode: Optional[ShadowModeValue.ShadowMode] = Field(
        None, description='The shadow mode.'
    )
    reference: Optional[ReferenceValue.Reference] = Field(
        None,
        description='The shadow mode specified as a reference to another property.',
    )


class ShadowMode(BaseCZMLObject):
    """
    Whether or not an object casts or receives shadows from each light source when shadows are enabled.
    """

    __root__: Union[List[ShadowMode1], ShadowMode1] = Field(
        ...,
        description='Whether or not an object casts or receives shadows from each light source when shadows are enabled.',
        title='ShadowMode',
    )