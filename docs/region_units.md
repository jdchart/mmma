# Region units
There is no inherent unit for the attributes of the `Region()` class - for example `start` can be in ms, in frames or in date.
Similarly, `x`, `y`, `width` or `height` could be in pixels, cm or km, `path` could be a list of pixel coordinates, or a list of real world coordinates.
Therefore, when you set one of these values, you must give the unit following a set of standards.
When setting a region's delimitations, you must provide a dict like follows: `{"value" : 0, "unit" : "ms"}`.

## Region attributes
- `start`: the beginning of a span of time.
- `end`: the end of a span of time.
- `x`: the x coordinate of the top left of a rectangular space, or the x coordinate of a point.
- `y`: the y coordinate of the top left of a rectangular space, or the y coordinate of a point.
- `width`: the width of a space.
- `height`: the height of a space.
- `path`: a list of point coordinates that would draw non-rectangular limits of the region.
- `props` : ad hoc region definitions.

## Region units
- `"time"` : unspecified time unit. Expected type: float. Attributes: `start`, `end`.
- `"ms"` : milliseconds. Expected type: float. Attributes: `start`, `end`.
- `"frames"` : frames. Expected type: int. Attributes: `start`, `end`.
- `"date"` : date. Expected type: datetime.datetime. Attributes: `start`, `end`.
- `"space"` : unspecified space unit. Expected type: float. Attributes: `x`, `y`, `width`, `height`, `path`.
- `"px"` : pixels. Expected type: int. Attributes: `x`, `y`, `width`, `height`, `path`.
- `"cm"` : pixels. Expected type: float. Attributes: `x`, `y`, `width`, `height`.
- `"co"` : coordinates. Expected type: float. Attributes: `x`, `y`, `width`, `height`, `path`.