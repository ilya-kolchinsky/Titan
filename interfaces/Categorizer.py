class Categorizer(object):

    def categorize(self, data_slices):
        return [self._categorize(data_slice) for data_slice in data_slices]

    def _categorize(self, data):
        raise NotImplementedError()

    def get_supported_labels(self):
        raise NotImplementedError()
