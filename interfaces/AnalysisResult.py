class AnalysisResult(object):

    def get_result_data(self):
        raise NotImplementedError()

    def get_hidden_data(self):
        raise NotImplementedError()

    def __str__(self):
        # for serialization
        raise NotImplementedError()

    def from_str(self):
        # for serialization
        raise NotImplementedError()
