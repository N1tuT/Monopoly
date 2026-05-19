from machine import Pin
import time


class TM1637:
    SEGMENTS = {
        "0": 0x3F,
        "1": 0x06,
        "2": 0x5B,
        "3": 0x4F,
        "4": 0x66,
        "5": 0x6D,
        "6": 0x7D,
        "7": 0x07,
        "8": 0x7F,
        "9": 0x6F,

        "A": 0x77,
        "B": 0x7C,
        "C": 0x39,
        "D": 0x5E,
        "E": 0x79,
        "F": 0x71,
        "G": 0x3D,
        "H": 0x76,
        "I": 0x06,  # same as 1
        "J": 0x1E,
        "K": 0x76,  # approximation, same as H
        "L": 0x38,
        "M": 0x37,  # approximation
        "N": 0x54,  # looks like n
        "O": 0x3F,  # same as 0
        "P": 0x73,
        "Q": 0x67,  # approximation
        "R": 0x50,  # looks like r
        "S": 0x6D,  # same as 5
        "T": 0x78,  # looks like t
        "U": 0x3E,
        "V": 0x3E,  # same as U
        "W": 0x2A,  # weak approximation
        "X": 0x76,  # approximation, same as H
        "Y": 0x6E,
        "Z": 0x5B,  # same as 2
        
        "-": 0x40,
        " ": 0x00,
    }

    def __init__(self, clk, dio, brightness=7):
        self.clk = Pin(clk, Pin.OUT)
        self.dio = Pin(dio, Pin.OUT)
        self.brightness = brightness & 0x07
        self.clk.value(1)
        self.dio.value(1)

    def start(self):
        self.dio.value(1)
        self.clk.value(1)
        self.dio.value(0)
        self.clk.value(0)

    def stop(self):
        self.clk.value(0)
        self.dio.value(0)
        self.clk.value(1)
        self.dio.value(1)

    def write_byte(self, data):
        for i in range(8):
            self.clk.value(0)
            self.dio.value((data >> i) & 1)
            self.clk.value(1)

        # ACK bit
        self.clk.value(0)
        self.dio.init(Pin.IN)
        self.clk.value(1)
        self.clk.value(0)
        self.dio.init(Pin.OUT)

    def command(self, cmd):
        self.start()
        self.write_byte(cmd)
        self.stop()

    def write_segments(self, segments):
        self.command(0x40)  # automatic address increment

        self.start()
        self.write_byte(0xC0)  # start at first digit

        for segment in segments:
            self.write_byte(segment)

        self.stop()

        self.command(0x88 | self.brightness)

    def encode_char(self, char):
        char = str(char).upper()
        return self.SEGMENTS.get(char, 0x00)

    def show(self, text, colon=False):
        text = str(text)

        # Make text exactly 4 characters long
        if len(text) > 4:
            text = text[:4]

        while len(text) < 4:
            text = text + " "

        segments = []

        for char in text:
            segments.append(self.encode_char(char))

        if colon:
            segments[1] |= 0x80

        self.write_segments(segments)

    def number(self, num, colon=False):
        text = str(num)

        if len(text) > 4:
            text = text[-4:]

        # Right-align number manually
        while len(text) < 4:
            text = " " + text

        self.show(text, colon=colon)

    def clear(self):
        self.write_segments([0x00, 0x00, 0x00, 0x00])

    def set_brightness(self, brightness):
        self.brightness = brightness & 0x07
        self.command(0x88 | self.brightness)
