class Region:
    def __init__(self, **kwargs) -> None:
        """
        A region of a Corpus.
        
        There is no inherent unit for the attributes of the `Region()` class - for example `start` can be in ms, in frames or in date.
        Similarly, `x`, `y`, `width` or `height` could be in pixels, cm or km, `path` could be a list of pixel coordinates, or a list of real world coordinates.
        Each region has a set of attributes that you can set, and a `time_unit` and `space_unit` attribute that sets the unit.
        """

        # Attributes are set via __dict__ because we update the setattr method.
        self.__dict__["target"] = kwargs.get("target", None)

        self.__dict__["time_unit"] = kwargs.get("time_unit", "ms")
        self.__dict__["space_unit"] = kwargs.get("space_unit", "px")

        self.__dict__["start"] = kwargs.get("start", None)
        self.__dict__["end"] = kwargs.get("end", None)
        self.__dict__["x"] = kwargs.get("x", None)
        self.__dict__["y"] = kwargs.get("y", None)
        self.__dict__["z"] = kwargs.get("z", None)
        self.__dict__["width"] = kwargs.get("width", None)
        self.__dict__["height"] = kwargs.get("height", None)
        self.__dict__["depth"] = kwargs.get("depth", None)
        self.__dict__["path"] = kwargs.get("path", None)
        self.__dict__["props"] = kwargs.get("props", None)

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
    
    def __setattr__(self, attr, val) -> None:
        """Update the setter method so that it may trigger recalculation of corpus dimensions."""
        
        super().__setattr__(attr, val)
        if self.target != None:
            if self.target.mmma_type == "Corpus":
                if self.target.handler != None:
                    self.target.handler.decode()