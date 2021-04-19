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

    def __init__(self, start=0):
        """Constructor...
        start is int
        it is the actual iterator
        This will jsut save the starting point in start"""
        self.start = start
        self.it = start

    def generate(self) -> int:
        """
        Takes nothing and returns an int
        assigns a return value
        iterates it
        """
        result = self.it
        self.it += 1
        return result

    def reset(self) -> None:
        """
        Takes nothing, just resets it to start value
        """
        self.it = self.start

    def __repr__(self):
        return f'SerialGenerator("start={self.start}")'


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    serial = SerialGenerator()
    # print(serial.generate())
    # serial.reset()
    # print(serial.generate())
    print(serial.__repr__())
