class GraphSlicer(object):

    def slice(self, data_provider):
        return [self._slice(data_to_slice) for data_to_slice in data_provider]

    def _slice(self, data):
        raise NotImplementedError()
