class Lamp:
    def __init__ (self, state = 'off'):
        self.state = state

    def turn_on(self):
        self.state = 'on'

    def turn_off(self):
        self.state = 'off'

    def print_state(self):
        print(f'The lamp is: {self.state}')



lamp1 = Lamp()
lamp1.turn_on()
lamp1.print_state()
