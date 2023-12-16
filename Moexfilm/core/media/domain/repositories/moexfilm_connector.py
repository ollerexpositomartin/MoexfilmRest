from abc import ABC, abstractmethod


class MoexfilmConnector(ABC):

    @abstractmethod
    def execute(self, query: str, params=None):
        pass

    @abstractmethod
    def end(self):
        pass
