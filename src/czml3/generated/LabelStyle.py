# generated by datamodel-codegen:
#   filename:  LabelStyle.json
#   timestamp: 2021-03-29T05:46:25+00:00

from __future__ import annotations

from typing import Any, Optional

from pydantic import BaseModel, Field


class DeletableProperty(BaseModel):
    """
    The base schema for a property whose value may be deleted.
    """

    delete: Optional[bool] = Field(
        None,
        description='Whether the client should delete existing samples or interval data for this property. Data will be deleted for the containing interval, or if there is no containing interval, then all data. If true, all other properties in this property will be ignored.',
    )


class LabelStyleValueProperty(BaseModel):
    __root__: Any = Field(
        ...,
        description='The base schema for a property whose value may be written as a label style.',
    )


class ReferenceValueProperty(BaseModel):
    __root__: Any = Field(
        ...,
        description='The base schema for a property whose value may be written as a reference to another property.',
    )


class LabelStyleValue(BaseModel):
    __root__: str = Field(..., description='The style of a label.')


class ReferenceValue(BaseModel):
    __root__: str = Field(
        ...,
        description='Represents a reference to another property. References can be used to specify that two properties on different objects are in fact, the same property.',
    )


class LabelStyle(BaseModel):
    """
    The style of a label.
    """

    labelStyle: Optional[LabelStyleValue] = Field(None, description='The label style.')
    reference: Optional[ReferenceValue] = Field(
        None,
        description='The label style specified as a reference to another property.',
    )
