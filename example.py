from tacpyle.app import tacpyle_app, callback

@callback(note=71, range=100)
def fader(value):
    print value

@callback(note=72, range=10)
def say_hello(value):
    messages = [
        'hi',
        'hello',
        'well, hello there',
        'hello again',
        'i see you are still here',
        'yes?',
        'no',
        'stop',
        'go away',
        'shoo!',    
        'outta here!',
    ]
    print messages[value]

tacpyle_app()
