from tacpyle.midi import start_listening

def dump_callback_data(message, timestamp):
    signal, note, value = message
    print "Note: {note}   Value: {value}".format(note=note, value=value)


start_listening(callback_method=dump_callback_data)

