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
        """ Create a serial generator that begins at start (number). """
        self.start = start - 1
        self.previous_value = start - 1

    def generate(self):
        """ Given the current count, return next sequential number. """
        self.previous_value += 1
        return self.previous_value

    def reset(self):
        """ Reset current count to original start number. """
        self.previous_value = self.start
