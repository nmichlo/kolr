# Nathan Michlo


class Color(object):

    def __init__(self, color):
        self._rgb = None
        self._hex = None

        # Convert color to correct type
        t = type(color)
        if t == Color:
            self._rgb = color._rgb
        elif t == tuple:
            assert len(color) == 3
            self._rgb = color
        elif t == str:
            assert len(color) == 7 and color[0] == '#'
            self._hex = color
        else:
            raise TypeError(f'Unsupported Type: {t}')

    def __hash__(self):
        return self.rgb.__hash__()

    def __eq__(self, other):
        if type(other) == Color:
            return self.rgb == other.rgb
        return False

    def __str__(self):
        return self.hex

    def __repr__(self):
        return str(self)

    @property
    def hex(self):
        if self._hex is None:
            self._hex = Color.rgb_to_hex(self._rgb)
        return self._hex

    @property
    def rgb(self):
        if self._rgb is None:
            self._rgb = Color.hex_to_rgb(self._hex)
        return self._rgb

    @staticmethod
    def hex_to_rgb(hex):
        hex = hex.lstrip('#')
        assert len(hex) == 6
        return tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))

    @staticmethod
    def rgb_to_hex(rgb):
        assert len(rgb) == 3 and all(0 <= v <= 255 for v in rgb)
        return '#%02x%02x%02x' % rgb