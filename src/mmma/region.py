class Region:
    def __init__(self, **kwargs) -> None:
        """
        A region of a Corpus.
        
        There is no inherent unit for these attributes - for example start can be in ms, in frames or in date.
        Similarly, x, y, width or height could be in pixels, cm or km, path could be a list of pixel coordinates, or a list of real world coordinates.
        Therefore, when you set one of these values, you must give the unit following a set of standards (please consult the docs for these).
        """

        self.start = kwargs.get("start", None)
        self.end = kwargs.get("end", None)
        self.x = kwargs.get("x", None)
        self.y = kwargs.get("y", None)
        self.width = kwargs.get("width", None)
        self.height = kwargs.get("height", None)
        self.path = kwargs.get("path", None)
        self.props = kwargs.get("props", None)