from time import sleep
import rtmidi_python as rtmidi

def start_listening(callback_method, port=0, sleep_time=0.2):
    midi_in = rtmidi.MidiIn()
    midi_in.callback = callback_method
    midi_in.open_port(port)

    while True:
        sleep(sleep_time)
        