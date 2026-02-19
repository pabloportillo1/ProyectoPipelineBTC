class BaseFilter:
    def process(self, transaction):
        raise NotImplementedError("Each filter must implement the process method.")