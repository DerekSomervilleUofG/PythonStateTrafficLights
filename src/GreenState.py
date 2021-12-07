from src.ColourState import ColourState
import AmberState

class GreenState(ColourState):

    def __init__(self, traffic_light):
        self.traffic_light = traffic_light

    def set_state(self):
        self.traffic_light.set_colour_state(AmberState.AmberState(self.traffic_light))

    def get_colour(self):
        return "GREEN"