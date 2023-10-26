from .mmma_element import MMMAElement

class Corpus(MMMAElement):
    def __init__(self) -> None:
        super().__init__()
        self.type = "Corpus"