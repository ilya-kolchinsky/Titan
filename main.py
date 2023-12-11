from titan import Titan
from plugins.data_providers.DateAndMetricFileBasedDataProvider import DateAndMetricFileBasedDataProvider

INPUT_PATH = r""
OUTPUT_PATH = r""

DATA_PROVIDER = DateAndMetricFileBasedDataProvider(INPUT_PATH)


def main():
    Titan(DATA_PROVIDER).analyze(OUTPUT_PATH)


if __name__ == '__main__':
    main()
