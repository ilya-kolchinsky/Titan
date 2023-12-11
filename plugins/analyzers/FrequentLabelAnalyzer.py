from interfaces.Analyzer import Analyzer


class FrequentLabelAnalyzer(Analyzer):
    def analyze(self, data):

        # flatten the data in all samples into one large sample
        flattened_data = [label for sample in data for label in sample]

        label_counters = {}
        most_frequent_label = None
        most_frequent_label_occurrences = 0

        for label in flattened_data:
            if label in label_counters:
                label_counters[label] += 1
            else:
                label_counters[label] = 1

            if label_counters[label] > most_frequent_label_occurrences:
                most_frequent_label = label
                most_frequent_label_occurrences = label_counters[label]

        return most_frequent_label
