from src.ColourState import ColourState
import RedState

class AmberState(ColourState):

    def __init__(self, traffic_light):
        self.traffic_light = traffic_light

    def set_state(self):
        self.traffic_light.set_colour_state(RedState.RedState(self.traffic_light))

    def get_colour(self):
        return "AMBER"

