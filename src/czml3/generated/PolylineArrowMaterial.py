# generated by datamodel-codegen:
#   filename:  PolylineArrowMaterial.json
#   timestamp: 2021-04-04T10:04:35+00:00

from __future__ import annotations

from typing import List, Optional, Union

import BaseCZMLObject
from pydantic import Field

from . import Color


class PolylineArrowMaterial1(BaseCZMLObject):
    """
    A material that fills the surface of a line with an arrow.
    """

    color: Optional[Color] = Field('white', description='The color of the surface.')


class PolylineArrowMaterial(BaseCZMLObject):
    """
    A material that fills the surface of a line with an arrow.
    """

    __root__: Union[List[PolylineArrowMaterial1], PolylineArrowMaterial1] = Field(
        ...,
        description='A material that fills the surface of a line with an arrow.',
        title='PolylineArrowMaterial',
    )