"""SVG tool code."""

class ScaleLinear:
    """Linear scale."""

    def __init__(self, domain, range_):
        """Linear scale constructor."""
        assert domain[0] < domain[1]
        assert range_[0] < range_[1]
        self.domain = domain
        self.range_ = range_

    def scale(self, value):
        """Scale from the domain to the range."""
        assert value >= self.domain[0] and value <= self.domain[1]
        fac = (value - self.domain[0]) / (self.domain[1] - self.domain[0])
        return self.range_[0] + fac * (self.range_[1] - self.range_[0])

    def axis_horizontal(self, tick_count=5, label=lambda tick_val: str(tick_val)):
        """Create a horizontal axis for the given scale."""
        width = self.domain[1] - self.domain[0]
        # Create the initial horizontal line
        axis = [
            '<path d="M%i,0 L%i,0" stroke="#000000"></path>\n'
            % (self.range_[0], self.range_[1]),
        ]
        # Create each tick
        for i in range(tick_count):
            tick_val = self.domain[0] + i * (width / float(tick_count))
            pos = self.scale(tick_val)
            axis.append('<path d="M{pos},0 L{pos},6" stroke="#000000"></path>'.format(pos=pos))
            # Add the labels
            axis.append(text(label(tick_val), x=pos - 4, y=20, style='font-size: 10pt'))
        return ''.join(axis)

class ScaleBand:
    """Band scale."""

    def __init__(self, domain, range_, padding=10):
        """Band scale constructor."""
        assert range_[0] < range_[1]
        self.domain = list(domain)
        self.domain.sort()
        self.range_ = range_
        self.padding = padding

    def scale(self, value):
        """Scale from the domain to the range."""
        assert value in self.domain
        i = self.domain.index(value)
        count = float(len(self.domain))
        width = (self.range_[1] - self.range_[0]) / count
        return self.range_[0] + i * width

    @property
    def bandwidth(self):
        """Return the bandwidth of the scale band."""
        count = float(len(self.domain))
        width = (self.range_[1] - self.range_[0]) / count
        return width - self.padding

    def axis_vertical(self, text_style=''):
        """Create a vertical axis."""
        axis = []
        for value in self.domain:
            self.scale(value)
            text_y = self.scale(value) + self.bandwidth / 2.5
            axis.append(text(value, x=0, y=text_y, style=text_style))
        return ''.join(axis)

class ScaleOrdinal:
    """Ordinal scale."""

    def __init__(self, domain, range_):
        """Ordinal scale constructor."""
        self.domain = list(domain)
        self.domain.sort()
        self.range_ = list(range_)
        self.range_.sort()

    def scale(self, value):
        """Scale from the domain to the range."""
        assert value in self.domain
        i = self.domain.index(value) % len(self.range_)
        return self.range_[i]

def svg(width, height, content=''):
    """Return an SVG document with the width, height and content."""
    return ''.join([
        '<svg xmlns="http://www.w3.org/2000/svg" width="%i" height="%i">\n'
        % (width, height),
        ''.join(content),
        '</svg>\n'
    ])

def rect(x, y, width, height, fill=None, content=''):
    """Return a new SVG rect element."""
    attrs = 'fill="%s"' % (fill,) if fill is not None else ''
    return ''.join([
        '<rect x="%i" y="%i" width="%i" height="%i" %s>\n'
        % (x, y, width, height, attrs),
        ''.join(content),
        '</rect>\n',
    ])

def g(transform=None, content=''):
    """SVG g element."""
    return ''.join([
        '<g transform="%s">\n' % (transform,),
        ''.join(content),
        '</g>\n',
    ])

def text(txt, x, y, style=''):
    """SVG text element."""
    return '<text x="%i" y="%i" style="%s">%s</text>\n' % (x, y, style, txt)

def path(d='', style=''):
    """SVG path element."""
    return '<path d="%s" style="%s" />' % (''.join(d), style)

def path_move_to(x, y):
    """SVG path line move to command."""
    return 'M%i,%i ' % (x, y)

def path_line_to(x, y):
    """SVG path line to command."""
    return 'L%i,%i ' % (x, y)

def translate(x, y):
    """Return a translate() transform."""
    return 'translate(%f %f)' % (x, y)
