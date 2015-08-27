# tacpyle

Use MIDI touchpad/keyboard to manage windows and control applications inside MacOSX

Example: 

```
from tacpyle.app import tacpyle_app, callback

@callback(note=71, range=100)
def fader(value):
    print value

tacpyle_app()
```

## Explanation

`from tacpyle.app import tacpyle_app, callback`

`tacpyle_app` is needed to start the MIDI listener, after you have set up the callbacks, remember to call it at the end using `tacpyle_app()`.
`callback` is a decorator that we'll use in the next line

`@callback(note=71, range=100)`

`note` can be discovered by running `python monitor.py` and fiddling with the MIDI controller.
`range` lets you choose the upper limit for the fader range. Default is 0-127, but if you need discrete steps such as 1-10, setting range=10 will automatically convert from 0-127 to 0-10 and call back only when the value actually changes (even if in 0-127 range it is changing gradually)

`def fader(value):`

You can name this function whatever you want, it needs to accept one  argument - `value`, this value is within the range specified in the decorator.

