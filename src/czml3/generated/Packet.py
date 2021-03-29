# generated by datamodel-codegen:
#   filename:  Packet.json
#   timestamp: 2021-03-29T05:46:25+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field

from . import Document, Label


class Packet(BaseModel):
    """
    Describes the graphical properties of a single object in a scene, such as a single aircraft.
    """

    id: Optional[str] = Field(
        None,
        description='The ID of the object described by this packet. IDs do not need to be GUIDs, but they do need to uniquely identify a single object within a CZML source and any other CZML sources loaded into the same scope. If this property is not specified, the client will automatically generate a unique one. However, this prevents later packets from referring to this object in order to add more data to it.',
    )
    delete: Optional[bool] = Field(
        None,
        description='Whether the client should delete all existing data for this object, identified by ID. If true, all other properties in this packet will be ignored.',
    )
    name: Optional[str] = Field(
        None,
        description='The name of the object. It does not have to be unique and is intended for user consumption.',
    )
    parent: Optional[str] = Field(
        None, description='The ID of the parent object, if any.'
    )
    description: Optional[Label.String] = Field(
        None, description='An HTML description of the object.'
    )
    clock: Optional[Document.Clock] = Field(
        None,
        description='The clock settings for the entire data set. Only valid on the document object.',
    )
    version: Optional[str] = Field(
        None,
        description='The CZML version being written. Only valid on the document object.',
    )
    availability: Optional[Document.TimeIntervalCollectionValue] = Field(
        '0000-00-00T00:00:00Z/9999-12-31T24:00:00Z',
        description='The set of time intervals over which data for an object is available. The property can be a single string specifying a single interval, or an array of strings representing intervals. A later CZML packet can update this availability if it changes or is found to be incorrect. For example, an SGP4 propagator may initially report availability for all time, but then later the propagator throws an exception and the availability can be adjusted to end at that time. If this optional property is not present, the object is assumed to be available for all time. Availability is scoped to a particular CZML stream, so two different streams can list different availability for a single object. Within a single stream, the last availability stated for an object is the one in effect and any availabilities in previous packets are ignored. If an object is not available at a time, the client will not draw that object.',
    )
    properties: Optional[Document.CustomProperties] = Field(
        None, description='A set of custom properties for this object.'
    )
    position: Optional[Document.Position] = Field(
        None,
        description='The position of the object in the world. The position has no direct visual representation, but it is used to locate billboards, labels, and other graphical items attached to the object.',
    )
    orientation: Optional[Document.Orientation] = Field(
        None,
        description='The orientation of the object in the world. The orientation has no direct visual representation, but it is used to orient models, cones, pyramids, and other graphical items attached to the object.',
    )
    viewFrom: Optional[Document.ViewFrom] = Field(
        None,
        description="A suggested camera location when viewing this object. The property is specified as a Cartesian position in the East (x), North (y), Up (z) reference frame relative to the object's position.",
    )
    billboard: Optional[Document.Billboard] = Field(
        None,
        description='A billboard, or viewport-aligned image, sometimes called a marker. The billboard is positioned in the scene by the `position` property.',
    )
    box: Optional[Document.Box] = Field(
        None,
        description='A box, which is a closed rectangular cuboid. The box is positioned and oriented using the `position` and `orientation` properties.',
    )
    corridor: Optional[Document.Corridor] = Field(
        None,
        description='A corridor, which is a shape defined by a centerline and width.',
    )
    cylinder: Optional[Document.Cylinder] = Field(
        None,
        description='A cylinder, truncated cone, or cone defined by a length, top radius, and bottom radius. The cylinder is positioned and oriented using the `position` and `orientation` properties.',
    )
    ellipse: Optional[Document.Ellipse] = Field(
        None,
        description='An ellipse, which is a closed curve on the surface of the Earth. The ellipse is positioned using the `position` property.',
    )
    ellipsoid: Optional[Document.Ellipsoid] = Field(
        None,
        description='An ellipsoid, which is a closed quadric surface that is a three-dimensional analogue of an ellipse. The ellipsoid is positioned and oriented using the `position` and `orientation` properties.',
    )
    label: Optional[Document.Label] = Field(
        None,
        description='A string of text. The label is positioned in the scene by the `position` property.',
    )
    model: Optional[Document.Model] = Field(
        None,
        description='A 3D model. The model is positioned and oriented using the `position` and `orientation` properties.',
    )
    path: Optional[Document.Path] = Field(
        None,
        description='A path, which is a polyline defined by the motion of an object over time. The possible vertices of the path are specified by the `position` property.',
    )
    point: Optional[Document.Point] = Field(
        None,
        description='A point, or viewport-aligned circle. The point is positioned in the scene by the `position` property.',
    )
    polygon: Optional[Document.Polygon] = Field(
        None,
        description='A polygon, which is a closed figure on the surface of the Earth.',
    )
    polyline: Optional[Document.Polyline] = Field(
        None,
        description='A polyline, which is a line in the scene composed of multiple segments.',
    )
    polylineVolume: Optional[Document.PolylineVolume] = Field(
        None,
        description='A polyline with a volume, defined as a 2D shape extruded along a polyline.',
    )
    rectangle: Optional[Document.Rectangle] = Field(
        None,
        description='A cartographic rectangle, which conforms to the curvature of the globe and can be placed along the surface or at altitude.',
    )
    tileset: Optional[Document.Tileset] = Field(None, description='A 3D Tiles tileset.')
    wall: Optional[Document.Wall] = Field(
        None,
        description='A two-dimensional wall which conforms to the curvature of the globe and can be placed along the surface or at altitude.',
    )
    agi_conicSensor: Optional[Document.ConicSensor] = Field(
        None,
        description='A conical sensor volume taking into account occlusion of an ellipsoid, i.e., the globe. The sensor is positioned and oriented using the `position` and `orientation` properties.',
    )
    agi_customPatternSensor: Optional[Document.CustomPatternSensor] = Field(
        None,
        description='A custom sensor volume taking into account occlusion of an ellipsoid, i.e., the globe. The sensor is positioned and oriented using the `position` and `orientation` properties.',
    )
    agi_rectangularSensor: Optional[Document.RectangularSensor] = Field(
        None,
        description='A rectangular pyramid sensor volume taking into account occlusion of an ellipsoid, i.e., the globe. The sensor is positioned and oriented using the `position` and `orientation` properties.',
    )
    agi_fan: Optional[Document.Fan] = Field(
        None,
        description='Defines a fan, which starts at a point or apex and extends in a specified list of directions from the apex. Each pair of directions forms a face of the fan extending to the specified radius. The fan is positioned and oriented using the `position` and `orientation` properties.',
    )
    agi_vector: Optional[Document.Vector] = Field(
        None,
        description='Defines a graphical vector that originates at the `position` property and extends in the provided direction for the provided length. The vector is positioned using the `position` property.',
    )
