from interfaces.Categorizer import Categorizer

FLAT_THRESHOLD = 10000


class TrivialRuleBasedCategorizer(Categorizer):

    LABELS = ["ASCENDING", "DESCENDING", "FLAT"]

    def get_supported_labels(self):
        return self.LABELS

    def _categorize(self, data):
        if len(data) < 2:
            return None

        first_value = int(data[0][1])
        last_value = int(data[-1][1])
        diff = last_value - first_value
        if abs(diff) < FLAT_THRESHOLD:
            return "FLAT"
        return "ASCENDING" if diff > 0 else "DESCENDING"
