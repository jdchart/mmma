import mmma
from mmma.analysis import AnalysisProcess

class DescriptionAnalysis(AnalysisProcess):
    def __init__(self, input) -> None:
        super().__init__(input)
        print("a description")