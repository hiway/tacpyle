from tacpyle.app import tacpyle_app, callback

@callback(note=71, range=100)
def fader(value):
    print value

tacpyle_app()
