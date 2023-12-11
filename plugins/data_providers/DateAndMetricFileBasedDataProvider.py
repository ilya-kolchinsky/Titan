import csv
from datetime import datetime, timedelta

from plugins.data_providers.FileBasedDataProvider import FileBasedDataProvider

DATE_FORMAT = '%m/%d/%Y  %H:%M:%S.%f'
METRIC_INDEX = 1  # Memory\Cache bytes
TIMEDELTA_BETWEEN_SAMPLES = timedelta(hours=1)


class DateAndMetricFileBasedDataProvider(FileBasedDataProvider):
    def _read_data(self):
        data_samples = []
        current_data_sample = []
        current_sample_start = None

        with open(self._file_path, newline='') as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                timestamp_str = row[0]
                try:
                    timestamp = datetime.strptime(timestamp_str, DATE_FORMAT)
                except ValueError:
                    # first line
                    continue
                if '' in row or ' ' in row:
                    # could happen due to imperfect data collection procedure
                    continue
                if current_sample_start is None:
                    current_sample_start = timestamp
                elif timestamp - current_sample_start >= TIMEDELTA_BETWEEN_SAMPLES:
                    data_samples.append(current_data_sample)
                    current_data_sample = []
                    current_sample_start = timestamp
                new_data_point = (timestamp, row[METRIC_INDEX])
                current_data_sample.append(new_data_point)
            data_samples.append(current_data_sample)

        return data_samples
