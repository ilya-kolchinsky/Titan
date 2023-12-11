from interfaces.Analyzer import Analyzer


class RegexAnalyzer(Analyzer):

    def analyze(self, data):

        list_of_strings, label_map = self.__preprocess_data(data)

        # use an external library to mine the best fitting regex
        regex_list = None  # TODO: find an external library that returns a list of regular expressions

        # for now, just choosing the best regex (the one with the max fitness)
        best_regex = max(regex_list, key=lambda x: x[0])[1]

        # have to come up with a better way of improving the regex readability
        # for long_label, short_label in label_map.items():
        #     best_regex = best_regex.replace(short_label, '(' + long_label + ')')
        return best_regex

    @staticmethod
    def __preprocess_data(data):
        # For now, we assume that no two labels start with the same letter. We will need to find a workaround soon.
        label_map = {}
        list_of_strings = []
        for sequence in data:
            long_labels = set(sequence)
            for label in long_labels:
                if label not in label_map:
                    short_label = label[0]
                    label_map[label] = short_label
            shortened_sequence = [label_map[label] for label in sequence]
            list_of_strings.append(''.join(shortened_sequence))

        return list_of_strings, label_map
