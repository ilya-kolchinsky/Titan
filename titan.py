import pickle

from plugins.analyzers.FrequentLabelAnalyzer import FrequentLabelAnalyzer
from plugins.categorizers.TrivialRuleBasedCategorizer import TrivialRuleBasedCategorizer
from plugins.slicers.ConstantIntervalSlicer import ConstantIntervalSlicer

DEFAULT_GRAPH_SLICER = ConstantIntervalSlicer()
DEFAULT_CATEGORIZER = TrivialRuleBasedCategorizer()
DEFAULT_ANALYZERS = [FrequentLabelAnalyzer()]


#  TITAN - daTa mIning for sysTem performANce
class Titan(object):

    def __init__(self, data_provider, slicer=None, categorizer=None, analyzers=None):
        self.__data_provider = data_provider

        self.__slicer = slicer if slicer is not None else DEFAULT_GRAPH_SLICER
        self.__categorizer = categorizer if categorizer is not None else DEFAULT_CATEGORIZER
        self.__analyzers = analyzers if analyzers is not None else DEFAULT_ANALYZERS

    def analyze(self, output_path, prior_analysis_result=None):
        # TODO: support incremental analysis by using prior_analysis_result parameter
        sliced_data_samples = self.__slicer.slice(self.__data_provider)
        categorized_data = [self.__categorizer.categorize(sliced_data_sample)
                            for sliced_data_sample in sliced_data_samples]

        with open(output_path, 'wb') as output_file:
            for analyzer in self.__analyzers:
                pickle.dump(analyzer.analyze(categorized_data), output_file)
