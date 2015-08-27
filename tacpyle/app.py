from .midi import start_listening
from functools import wraps

# note > [(method, range), ]
_callbacks = {}

def _call_method(method_data, value):
    # todo implement ranging
    range = method_data['range']
    multiplier = float(range)/ 127.0
    ranged_value = int(value * multiplier)
    if not method_data['last_callback_value'] == ranged_value:
        method_data['method'](ranged_value)
        method_data['last_callback_value'] = ranged_value


def _midi_callback(message, time_stamp, *args, **kwargs):
    signal, note, value = message
    if _callbacks.get(note):
        [_call_method(method_data, value) for method_data in _callbacks[note]]
    # print message, time_stamp, args, kwargs


def tags(tag_name):
    def tags_decorator(func):
        def func_wrapper(name):
            return "<{0}>{1}</{0}>".format(tag_name, func(name))

        return func_wrapper

    return tags_decorator

def callback(note, range):
    def _wrapper(method):
        return register_callback(method, note, range)
    return _wrapper


def register_callback(method, note, range=127):
    note_config = _callbacks.get(note)

    if not note_config:
        _callbacks[note] = []

    _callbacks[note].append(dict(method=method, range=range, last_callback_value=0))



def tacpyle_app():
    start_listening(callback_method=_midi_callback)