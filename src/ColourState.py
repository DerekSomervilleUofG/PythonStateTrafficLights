from abc import ABC, abstractmethod

class ColourState(ABC):

    traffic_light = None

    @abstractmethod
    def set_state(self):
        pass

    @abstractmethod
    def get_colour(self):
        pass