import numpy as np
from .mmma_element import MMMAElement

class Annotation(MMMAElement):
    def __init__(self, **kwargs) -> None:
        """
        Representation of a mmma Annotation.

        attributes
        ----------
        - target : Corpus. The Corpus that the annotation targets.
        - region : Region. The region of the Corpus that the annotation covers.
        - props : dict. By default empty, can be populated with any number of user-given properties.
        - annotation_list : 
        """

        # Initialize MMMAElement class with annotation mmma_type:
        super().__init__(mmma_type = "Annotation")

        # Annotation attributes:
        self.target = kwargs.get("target", None)
        self.region = kwargs.get("region", None)
        self.props = kwargs.get("props", {})