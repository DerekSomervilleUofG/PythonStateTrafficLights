import time
import RedState

class TrafficLight:
    colour_state = None

    def get_colour_state(self):
        return self.colour_state

    def set_colour_state(self, colour_state):
        self.colour_state = colour_state
        print(colour_state.get_colour())

    def change_light(self):
        self.colour_state.set_state()

    def change_lights(self, number_of_times):
        for counter in range(number_of_times):
            self.change_light()
            time.sleep(.5)

def main():
    traffic_light = TrafficLight()
    traffic_light.set_colour_state(RedState.RedState(traffic_light))
    traffic_light.change_lights(10)

if __name__ == "__main__":
    main()