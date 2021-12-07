from src.ColourState import ColourState
import GreenState

class RedState(ColourState):

    def __init__(self, traffic_light):
        self.traffic_light = traffic_light

    def set_state(self):
        self.traffic_light.set_colour_state(GreenState.GreenState(self.traffic_light))

    def get_colour(self):
        return "RED"