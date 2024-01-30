class Region:
    def __init__(self, **kwargs) -> None:
        """
        A region of a Corpus.
        
        There is no inherent unit for these attributes - for example start can be in ms, in frames or in date.
        Similarly, x, y, width or height could be in pixels, cm or km, path could be a list of pixel coordinates, or a list of real world coordinates.
        Therefore, when you set one of these values, you must give the unit following a set of standards (please consult the docs for these).
        """

        self.time_unit = kwargs.get("time_unit", "ms")
        self.space_unit = kwargs.get("space_unit", "px")

        self.start = kwargs.get("start", None)
        self.end = kwargs.get("end", None)
        self.x = kwargs.get("x", None)
        self.y = kwargs.get("y", None)
        self.z = kwargs.get("z", None)
        self.width = kwargs.get("width", None)
        self.height = kwargs.get("height", None)
        self.depth = kwargs.get("depth", None)
        self.path = kwargs.get("path", None)
        self.props = kwargs.get("props", None)

    def to_dict(self) -> dict:
        """Represent the dict as a dict."""
        ret = {}
        for attr in self.__dict__:
            if attr in ["start", "end", "props"] and attr not in ["time_unit", "space_unit"]:
                if getattr(self, attr) != None:
                    ret[attr] = getattr(self, attr)
                    ret["time_unit"] = self.time_unit
            if attr in ["x", "y", "props", "width", "height", "path", "z", "depth"] and attr not in ["time_unit", "space_unit"]:
                if getattr(self, attr) != None:
                    ret[attr] = getattr(self, attr)
                    ret["space_unit"] = self.space_unit
        return ret