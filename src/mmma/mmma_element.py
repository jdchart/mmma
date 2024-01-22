import pickle
import os
import uuid

class MMMAElement:
    def __init__(self, **kwargs) -> None:
        """
        Basic mmma element (base class for Corpus, Annotation and AnnotationList).

        attributes
        ----------
        - uuid : uuid.uuid4(). a unique ID is automatically attributed to the object on creation with uuid.uuid4().
        - mmma_type : str. The type of MMMAElement ("corpus", "annotation", "annotationlist"). Set on creation with the 'mmma_type' kwarg.
        """
        
        self.uuid = uuid.uuid4()
        self.mmma_type = kwargs.get('mmma_type', None)

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