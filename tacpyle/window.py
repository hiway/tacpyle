import os
import subprocess
from tacpyle.osahelper import osascript_multiline_compress


def get_screen_resolution():
    """
    returns (example): [1280, 800]
    """
    command = """osascript -e 'tell application "Finder" to get bounds of window of desktop'"""
    output = subprocess.check_output(command, shell=True)
    output = output.strip().split(',')
    output = [int(x.strip()) for x in output]
    return output[2:]


def set_window_size(window_name, width, height):
    """
    set_window_size("iTerm", 800, 600)
    """
    script = """tell application "System Events" to tell process "%s"
    tell window 1
        set size to {%s, %s}
    end tell
end tell""" % (window_name, width, height)
    os.system(osascript_multiline_compress(script))


def set_window_position(window_name, x, y):
    """
    set_window_position('iTerm', 100, 100)
    """
    script = """tell application "System Events" to tell process "%s"
    tell window 1
        set position to {%s, %s}
    end tell
end tell""" % (window_name, x, y)
    os.system(osascript_multiline_compress(script))


