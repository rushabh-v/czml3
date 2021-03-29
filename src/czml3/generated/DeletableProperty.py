# generated by datamodel-codegen:
#   filename:  DeletableProperty.json
#   timestamp: 2021-03-29T05:46:25+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class DeletableProperty(BaseModel):
    """
    The base schema for a property whose value may be deleted.
    """

    delete: Optional[bool] = Field(
        None,
        description='Whether the client should delete existing samples or interval data for this property. Data will be deleted for the containing interval, or if there is no containing interval, then all data. If true, all other properties in this property will be ignored.',
    )
