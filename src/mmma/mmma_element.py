import pickle
import os
import uuid
from .metadata import get_metadata_system

class MMMAElement:
    def __init__(self, **kwargs) -> None:
        """
        Basic mmma element (base class for Corpus, Annotation and AnnotationList).

        attributes
        ----------
        - uuid : uuid.uuid4(). a unique ID is automatically attributed to the object on creation with uuid.uuid4().
        - mmma_type : str. The type of MMMAElement ("corpus", "annotation", "annotationlist"). Set on creation with the 'mmma_type' kwarg.
        - metadata : Metadata. A Metadata object used to describe the element (by default dublin_core).
        """
        
        self.uuid = uuid.uuid4()
        self.mmma_type = kwargs.get('mmma_type', None)
        self.metadata = get_metadata_system(kwargs.get('metadata_system', "dublin_core"))

    def write(self, path : str) -> None:
        """
        Write the mmma element to disk.
        
        Path must have a ".pkl" extension.
        """

        if os.path.splitext((path))[1] == ".pkl":
            with open(path, 'wb') as write_file:
                pickle.dump(self, write_file, pickle.HIGHEST_PROTOCOL)
        else:
            print(f"Unable to write to path \"{path}\". Must have the \".pkl\" extension.")
    
    def to_dict(self):
        """Represent the mmma element as a dict."""
        ret = {"uuid" : self.uuid}
        if self.mmma_type != None:
            ret["mmma_type"] = self.mmma_type
        ret["metadata"] = self.metadata.to_dict()
        return ret

    def set_metadata(self, attribute_name : str, value):
        """Set the attribute of the element's metadata object."""

        setattr(self.metadata, attribute_name, value)
    
def read(path : str) -> None:
    """
    Read an mmma element from disk.
    
    Path must have a ".pkl" extension.
    """

    if os.path.splitext(path)[1] == ".pkl":
        if os.path.isfile(path):
            with open(path, 'rb') as read_file:
                read = pickle.load(read_file)
                return read
        else:
            print(f"Unable to read from path \"{path}\". The file doesn't exist.")
    else:
        print(f"Unable to read from path \"{path}\". Must have the \".pkl\" extension.")