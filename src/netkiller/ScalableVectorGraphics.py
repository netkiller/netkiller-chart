class Svg:
    # https://developer.mozilla.org/zh-CN/docs/Web/SVG/Tutorials/SVG_from_scratch/SVG_and_CSS
    def __init__(self, width, height, **kwargs):
        self.width = width
        self.height = height
        self.elements = []
        self.attribute = []
        for key, value in kwargs.items():
            self.attribute.append(f'{key}="{value}"')

    def __attribute(self, kwargs) -> str:
        attrs = []
        for key, value in kwargs.items():
            if key in ['klass', 'clazz']:
                key = 'class'
            attrs.append(f'{key}="{value}"')
        return " ".join(attrs)

    def link(self, href):
        self.elements.append(f'<link rel="stylesheet" href="{href}" type="text/css" />')

    def title(self, text: str):
        self.elements.append(f"<title>{text}</title>")

    def desc(self, text: str):
        self.elements.append(f"<desc>{text}</desc>")

    def defs(self):
        pass

    def symbol(self, id: str, element):
        self.elements.append(f'<symbol id="{id}">{element.__str__()}</symbol>')

    def use(self, x: int, y: int, id: str, **kwargs):
        self.elements.append(f'<use xlink:href="#{id}" x="{x}" y="{y}" {self.__attribute(kwargs)}/>')

    def group(self, element, **kwargs):
        self.elements.append(f'<g {self.__attribute(kwargs)}>{element.__str__()}</g>')

    def append(self, text):
        if type(text) == str:
            self.elements.append(text)
        else:
            self.elements.append(text.__str__())

    def render(self):
        self.elements.insert(0,
                             f'<svg width="{self.width}px"   height="{self.height}px" {" ".join(self.attribute)} xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">')
        self.elements.append("</svg>")
        return "\n".join(self.elements)

    def __str__(self):
        return self.render()

    def save(self, filename):
        with open(filename, 'w') as file:
            file.write(self.render())

    def main(self):
        self.save('test.svg')


class Element:
    def __init__(self):
        pass

    def attribute(self, kwargs):
        attrs = []
        for key, value in kwargs.items():
            if key in ['klass', 'clazz']:
                key = 'class'
            attrs.append(f'{key}="{value}"')
        return " ".join(attrs)


class Title:
    def __init__(self, value):
        self.title = value

    def __str__(self):
        return f"<title>{self.title}</title>"


class Text(Element):
    def __init__(self, x: int, y: int, text: str, **kwargs):
        super().__init__()
        self.x = x
        self.y = y
        self.text = text
        self.attrs = super().attribute(kwargs)

    def __str__(self):
        return f'<text x="{self.x}" y="{self.y}" {self.attrs}>{self.text}</text>'


class Circle(Element):
    def __init__(self, cx: int, cy: int, r: int, stroke: str = None, fill: str = None, **kwargs):
        self.cx = cx
        self.cy = cy
        self.r = r
        if stroke:
            kwargs['stroke'] = stroke
            # self.stroke = stroke
        if fill:
            kwargs['fill'] = fill
            # self.fill = fill
        self.attrs = super().attribute(kwargs)

    def __str__(self):
        # return f'<circle cx="{self.cx}" cy="{self.cy}" r="{self.r}" stroke="{self.stroke}" fill="{self.fill}" {self.attrs} />'
        return f'<circle cx="{self.cx}" cy="{self.cy}" r="{self.r}" {self.attrs} />'


class Rectangle(Element):
    def __init__(self, x: int, y: int, width: int, height: int, stroke: str = None, fill: str = None, **kwargs):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        if stroke:
            kwargs['stroke'] = stroke
        if fill:
            kwargs['fill'] = fill
        self.attrs = super().attribute(kwargs)

    def __str__(self):
        # return f'<circle cx="{self.cx}" cy="{self.cy}" r="{self.r}" stroke="{self.stroke}" fill="{self.fill}" {self.attrs} />'
        return f'<rect x="{self.x}" y="{self.y}" width="{self.width}" height="{self.height}" {self.attrs} />'


class Path(Element):
    def __init__(self, d: str = None, stroke: str = None, fill: str = None, **kwargs):
        self.d = d
        if stroke:
            kwargs['stroke'] = stroke
        if fill:
            kwargs['fill'] = fill
        self.attrs = super().attribute(kwargs)
        self.drawn = []

    def D(self):
        # https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/d
        self.d = None
        return self

    def M(self, x, y):
        self.drawn.append(f'M {x},{y}')
        return self

    def m(self, dx, dy):
        self.drawn.append(f'M {dx},{dy}')
        return self

    def L(self, x, y):
        self.drawn.append(f'L {x},{y}')
        return self

    def l(self, dx, dy):
        self.drawn.append(f'l {dx},{dy}')
        return self

    def H(self, x: int):
        self.drawn.append(f'H {x}')
        return self

    def H(self, dx: int):
        self.drawn.append(f'H {dx}')
        return self

    def V(self, y: int):
        self.drawn.append(f'H {y}')
        return self

    def v(self, dy: int):
        self.drawn.append(f'H {dy}')
        return self

    def C(self, x1, y1, x2, y2, x, y):
        self.drawn.append(f'C {x1},{y1},{x2},{y2},{x},{y}')
        return self

    def c(self, dx1, dy1, dx2, dy2, dx, dy):
        self.drawn.append(f'c {dx1},{dy1},{dx2},{dy2},{dx},{dy}')
        return self

    def S(self, x2, y2, x, y):
        self.drawn.append(f'S {x2},{y2},{x},{y}')
        return self

    def s(self, dx2, dy2, dx, dy):
        self.drawn.append(f's {dx2},{dy2},{dx},{dy}')
        return self

    def Q(self, x1, y1, x, y):
        self.drawn.append(f'Q {x1},{y1},{x},{y}')
        return self

    def q(self, dx1, dy1, dx, dy):
        self.drawn.append(f'q {dx1},{dy1},{dx},{dy}')
        return self

    def T(self, x, y):
        self.drawn.append(f'T {x},{y}')
        return self

    def t(self, dx, dy):
        self.drawn.append(f't {dx},{dy}')
        return self

    def A(self, rx, ry, angle, large_arc_flag, sweep_flag, x, y):
        self.drawn.append(f'A {rx}, {ry}, {angle}, {large_arc_flag}, {sweep_flag}, {x}, {y}')
        return self

    def a(self, rx, ry, angle, large_arc_flag, sweep_flag, dx, dy):
        self.drawn.append(f'A {rx}, {ry}, {angle}, {large_arc_flag}, {sweep_flag}, {dx}, {dy}')
        return self

    def Z(self):
        self.drawn.append(f'Z')
        return self

    def z(self):
        self.drawn.append(f'z')
        return self

    def __str__(self):
        if not self.d:
            self.d = " ".join(self.drawn)
        return f'<path d="{self.d}" {self.attrs} />'


svg = Svg(600, 600)
# svg.link("style.css")
svg.title("Test")
svg.desc("https://www.netkiller.cn")
# svg.append(Title("Hello world"))
svg.symbol("shape1", Circle(25, 25, 25, "gery"))
svg.append(Text(100, 200, "Hello world", klass="test"))
svg.append(Circle(100, 200, 100, "red", fill="none"))
svg.append(Rectangle(100, 200, 100, 100, "blue", fill="green"))
svg.append(Rectangle(200, 200, 100, 100, style="stroke:#009900; fill: #00cc00"))
svg.use(10, 10, "shape1")
svg.use(100, 50, "shape1", style="stroke: #00ff00; fill: none;")
svg.group(Text(10, 100, "Hello world", klass="test"))
svg.append(Path('M100,100 L150,100 L150,150 Z'))
svg.append(Path().D().M(10, 10).L(10, 15).L(20, 26).H(11).V(30).Z())
svg.main()
