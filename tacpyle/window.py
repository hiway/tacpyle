import subprocess

def get_screen_resolution():
    """
    returns (example): [1280, 800]
    """
    command = """osascript -e 'tell application "Finder" to get bounds of window of desktop'"""
    output = subprocess.check_output(command, shell=True)
    output = output.strip().split(',')
    output = [int(x.strip()) for x in output]
    return output[2:]
