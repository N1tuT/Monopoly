# gameLogger.py
# Functions to write game logs to a file

from time import ticks_ms, ticks_diff

game_start_time = None

def startGameTimer():
    """
    Starts game timer
    """

    global game_start_time
    game_start_time = ticks_ms()

def stopGameTimer():
    """
    Starts game timer
    """

    global game_start_time
    game_start_time = None


def getGameTime():
    """
    Return how long the game has been running in seconds.
    """
    if game_start_time is None:
        return None
    
    elapsed_ms = ticks_diff(ticks_ms(), game_start_time)
    return elapsed_ms / 1000




def formatGameTime (secs):
    """
    Convert game time into HH:MM:SS:MS format
    """
    
    total_ms = int(secs * 1000)

    hours = total_ms // 3600000
    total_ms %= 3600000

    mins = total_ms // 60000
    total_ms %= 60000

    seconds = total_ms // 1000
    milliseconds = total_ms % 1000

    return "{:02}:{:02}:{:02}:{:03}".format(
        hours, mins, seconds, milliseconds
    )




def writeLog (msg):
    """
    Write a normal message to the game log file.
    """
    with open("game_log.txt", "a") as log_file:
        log_file.write(msg + "\n")


def writeErrorLog (msg):
    """
    Write a message to the game log file

    If the game timer has started, include the game time.
    If the game timer has not started, log it as a setup error.
    """

    game_time = getGameTime()

    if game_time is None:
        writeLog("SETUP ERROR: " + msg)
    else:
        writeLog(f"[{formatGameTime(game_time)}] ERROR: {msg}")

