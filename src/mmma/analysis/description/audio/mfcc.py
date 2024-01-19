from ...utils import flucoma_subprocess

from ..description_analysis import DescriptionAnalysis

class MFCCAnalysis(DescriptionAnalysis):
    def __init__(self, input) -> None:
        super().__init__(input)
        print("MFCC anal")

    def process(self):
        return flucoma_subprocess("mfcc", self.input, ["features"], {})