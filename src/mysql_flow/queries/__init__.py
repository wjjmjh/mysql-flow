# credits: Stephen Ka-Wah Ma
def wrap(val):
    if isinstance(val, str):
        return '"{}"'.format(val)
    return "{}".format(val)
