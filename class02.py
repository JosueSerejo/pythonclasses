class Lamp:
    def __init__(self, color, power, state='off'):
        self.state = state
        self.color = color
        self.power = power

    def turn_on(self):
        self.state = 'on'

    def turn_off(self):
        self.state = 'off'

    def print_state(self):
        print(f'The lamp is: {self.state}')

    def set_color(self, new_color):
        self.color = new_color

    def set_power(self, new_power):
        self.power = new_power

    def __str__(self):
        return f"Lamp({self.power}W, {self.color}, {self.state})"


def main():


 lamp1 = Lamp(color="yellow", power=60)
 lamp1.turn_on()
 print(lamp1)

 lamp1.set_color("blue")
 lamp1.set_power(100)
 lamp1.turn_off()
 print(lamp1)


if __name__ == '__main__': 
    main()
