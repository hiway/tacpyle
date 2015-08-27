import os

# http://apple.stackexchange.com/questions/36943/how-do-i-automate-a-key-press-in-applescript

templ_keystroke = """osascript -e 'tell application "System Events" to keystroke "{key}"{modifiers}'"""
templ_keycode = """osascript -e 'tell application "System Events" to key code {key}{modifiers}'"""


def build_osascript_command(key, key_code=False, command=False, option=False, shift=False, control=False):
    modifiers = []
    if command is True:
        modifiers.append('command down')
    if option is True:
        modifiers.append('option down')
    if shift is True:
        modifiers.append('shift down')
    if control is True:
        modifiers.append('control down')

    if modifiers:
        modifiers = ' using {%s}' % (', '.join(modifiers))

    if key_code is True:
        return templ_keycode.format(key=key, modifiers=modifiers)
    return templ_keystroke.format(key=key, modifiers=modifiers)


def send_keystroke(key, key_code=False, command=False, option=False, shift=False, control=False):
    cmd = build_osascript_command(key, key_code, command, option, shift, control)
    os.system(cmd)
