class Metadata:
    def __init__(self) -> None:
        pass

def get_metadata_system(system_name : str):
    """Return a metadata object according to input."""

    if system_name == "dublin_core":
        return DublinCore()

class DublinCore(Metadata):
    def __init__(self, **kwargs) -> None:
        super().__init__()

        self.title = kwargs.get("title", None)
        self.subject = kwargs.get("subject", None)
        self.description = kwargs.get("description", None)
        self.type = kwargs.get("type", None)
        self.source = kwargs.get("source", None)
        self.creator = kwargs.get("creator", None)
        self.publisher = kwargs.get("publisher", None)
        self.contributor = kwargs.get("contributor", None)
        self.rights = kwargs.get("rights", None)
        self.audience = kwargs.get("audience", None)
        self.provenance = kwargs.get("provenance", None)
        self.rights_holder = kwargs.get("rights_holder", None)
        self.accural_method = kwargs.get("accural_method", None)
        self.accural_periodicity = kwargs.get("accural_periodicity", None)
        self.accural_policy = kwargs.get("accural_policy", None)
        self.date = kwargs.get("date", None)
        self.relation = kwargs.get("relation", None)
        self.coverage = kwargs.get("coverage", None)
        self.format = kwargs.get("format", None)
        self.instructional_method = kwargs.get("instructional_method", None)