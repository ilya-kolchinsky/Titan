from interfaces.GraphSlicer import GraphSlicer

CONSTANT_INTERVAL = 300  # 5-minute intervals


class ConstantIntervalSlicer(GraphSlicer):
    def _slice(self, data):
        num_slices = int(len(data) / CONSTANT_INTERVAL)
        return [data[i * CONSTANT_INTERVAL:(i + 1) * CONSTANT_INTERVAL] for i in range(num_slices)]
