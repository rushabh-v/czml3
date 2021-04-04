# generated by datamodel-codegen:
#   filename:  Tileset.json
#   timestamp: 2021-04-04T10:04:35+00:00

from __future__ import annotations

from typing import Optional

import BaseCZMLObject
from pydantic import Field

from . import Boolean, Double, Uri


class Tileset(BaseCZMLObject):
    """
    A 3D Tiles tileset.
    """

    show: Optional[Boolean] = Field(
        True, description='Whether or not the tileset is shown.'
    )
    uri: Optional[Uri] = Field(
        None,
        description='The URI of a 3D tiles tileset. For broadest client compatibility, the URI should be accessible via Cross-Origin Resource Sharing (CORS).',
    )
    maximumScreenSpaceError: Optional[Double] = Field(
        None,
        description='The maximum screen space error used to drive level of detail refinement.',
    )
