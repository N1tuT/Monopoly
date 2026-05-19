# segHandler.py

from library.tm1637 import TM1637  # type: ignore

def setup7Seg(clk, dio, brightness):
    return TM1637(clk, dio, brightness)