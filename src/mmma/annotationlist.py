import numpy as np
from .mmma_element import MMMAElement
from .annotation import Annotation

class AnnotationList(MMMAElement):
    def __init__(self) -> None:
        """Representation of a mmma AnnotationList."""

        # Initialize MMMAElement class with annotation mmma_type:
        super().__init__(mmma_type = "AnnotationList")

        # AnnotationList attributes:
        self.array = None
        self._array_empty = True

    def append_slice(self, annotation : Annotation) -> None:
        """Add a new annotation to the annotation list."""

        if self._array_empty:
            self.array = np.array([annotation])
            self._array_empty = False
        else:
            self.array = np.append(self.array, annotation)

    def clear(self) -> None:
        """Clear the array and reset the object."""

        self.array = None
        self._array_empty = True