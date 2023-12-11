from interfaces.DataProvider import DataProvider


class FileBasedDataProvider(DataProvider):

    def __init__(self, file_path=None):
        self._file_path = None
        self.__data_samples = None
        if file_path is not None:
            self.set_file_path(file_path)

    def set_file_path(self, file_path):
        self._file_path = file_path
        self.__data_samples = self._read_data()

    def get_data_sample(self):
        if self.__data_samples is None:
            return None
        for sample in self.__data_samples:
            yield sample

    def _read_data(self):
        raise NotImplementedError()
