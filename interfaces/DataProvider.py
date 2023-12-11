class DataProvider(object):

    def get_data_sample(self):
        raise NotImplementedError()

    def __iter__(self):
        return self.get_data_sample()
