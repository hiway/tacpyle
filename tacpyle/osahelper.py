def osascript_multiline_compress(script):
    script = ["-e '{line}'".format(line=line) for line in script.split('\n')]
    return 'osascript ' + ' '.join(script)

