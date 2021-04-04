# generated by datamodel-codegen:
#   filename:  LineThickness.json
#   timestamp: 2021-04-04T10:04:35+00:00

from __future__ import annotations

from typing import List, Optional, Union

import BaseCZMLObject
from pydantic import Field

from .DeletableProperty import DeletableProperty
from .InterpolatableProperty import InterpolatableProperty
from .Values import Cartesian2Value, ReferenceValue


class LineThickness1(InterpolatableProperty, DeletableProperty):
    """
    The thickness of grid lines along each axis, in pixels.
    """

    cartesian2: Optional[Cartesian2Value.Cartesian2] = Field(
        None,
        description='The thickness specified as a two-dimensional Cartesian value `[X, Y]`, in pixels.',
    )
    reference: Optional[ReferenceValue.Reference] = Field(
        None, description='The thickness specified as a reference to another property.'
    )


class LineThickness(BaseCZMLObject):
    """
    The thickness of grid lines along each axis, in pixels.
    """

    __root__: Union[List[LineThickness1], LineThickness1] = Field(
        ...,
        description='The thickness of grid lines along each axis, in pixels.',
        title='LineThickness',
    )