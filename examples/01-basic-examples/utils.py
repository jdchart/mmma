import os

def test_media(media_type : str = "video") -> list:
    """Get some test media files."""
    base_folder = os.path.join(os.getcwd(), "test-corpora", f"{media_type}s")
    return collect_files(base_folder)

def collect_files(path, accepted_formats = [], recursive = True):
    """Collect all of the files of a given type in a directory."""
    finalList = []
    for root, dirs, files in os.walk(path):
        for file in files:
            extension = os.path.splitext(file)[1][1:]
            if extension in accepted_formats or len(accepted_formats) == 0:
                finalList.append(os.path.join(root, file))
    return finalList

def create_output_folder():
    if os.path.isdir(os.path.join(os.getcwd(), "output")) == False:
        os.makedirs(os.path.join(os.getcwd(), "output"))
    return os.path.join(os.getcwd(), "output")