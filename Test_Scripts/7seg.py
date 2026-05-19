from tm1637 import TM1637
import time

display = TM1637(clk=16, dio=17, brightness=7)

display.show("1234")
time.sleep(1)

display.show("PLAY")
time.sleep(1)

display.number(42)
time.sleep(1)

display.clear()