import numpy as np
from .mmma_element import MMMAElement
from .annotation import Annotation

class AnnotationList(MMMAElement):
    def __init__(self) -> None:
        """Representation of a mmma AnnotationList."""

        # Initialize MMMAElement class with annotation mmma_type:
        super().__init__(mmma_type = "AnnotationList")

        # AnnotationList attributes:
        self._array = None
        self._array_empty = True

    def append_annotation(self, annotation : Annotation) -> None:
        """Add a new annotation to the annotation list."""

        if self._array_empty:
            self._array = np.array([annotation])
            self._array_empty = False
        else:
            self._array = np.append(self._array, annotation)

    def clear(self) -> None:
        """Clear the array and reset the object."""

        self._array = None
        self._array_empty = True

    def to_dict(self) -> dict:
        """Represpent the contents of the annotation list as a dict."""
        if self._array_empty == False:
            ret = {"annotations" : []}
            for annotation in self._array:
                ret["annotations"].append(annotation.to_dict())
            return ret
        else:
            return {}