class PipeLine:
    def __init__(self, filters):
        self.filters = filters

    def run(self, transaction):
        for filter in self.filters:
            transaction = filter.process(transaction)

        return transaction