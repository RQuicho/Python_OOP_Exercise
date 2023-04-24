"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start):
        "Gives a starting number for a new serial number."
        self.start = start

    def __repr__(self):
        "Shows representation."
        return f"<Serial Generator start={self.start}>"

    def generate(self):
        "Generates next number."
        self.start += 1
        return self.start

    def reset(self):
        self.start = None

