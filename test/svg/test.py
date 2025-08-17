import os
import sys

# module = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ".")
# sys.path.insert(1, module)
src = os.path.join(os.path.dirname(os.path.dirname(os.getcwd())), 'src')
sys.path.insert(1, src)
# print(src)
# print(module)

try:
    from netkiller.svg.ScalableVectorGraphics import Svg
    from netkiller.svg.elements import Text, Line, Circle, Rectangle, Image, Path, Ellipse

except ImportError as err:
    print("Error: %s" % (err))
    exit()


def main():
    # print('-' * 20)
    svg = Svg(600, 600)
    # svg.link("style.css")
    svg.title("Test")
    svg.desc("https://www.netkiller.cn")
    # svg.append(Title("Hello world"))
    svg.symbol("shape1", Circle(25, 25, 25, "gery"))
    svg.append(Text(100, 200, "Hello world", klass="test"))
    svg.append(Line(100, 5, 100, 300, stroke="#006600"))
    svg.append(Circle(100, 200, 100, "red", fill="none"))
    svg.append(Rectangle(100, 200, 100, 100, "blue", fill="green"))
    svg.append(Rectangle(200, 200, 100, 100, style="stroke:#009900; fill: #00cc00"))
    svg.append(Image(300, 300, 100, 100, href="https://www.netkiller.cn/graphics/by-nc-sa.png"))
    svg.use(10, 10, "shape1")
    svg.use(100, 50, "shape1", style="stroke: #00ff00; fill: none;")
    svg.group(Text(10, 100, "Hello world", klass="test"))
    svg.append(Path('M100,100 L150,100 L150,150 Z'))
    svg.append(Path().D().M(10, 10).L(10, 15).L(20, 26).H(11).V(30).Z())
    svg.append(Line(100, 200, 300, 300, stroke="#006600"))
    svg.append(Ellipse(30, 30, 30, 15, style="stroke:#006600; fill:#00cc00"))

    svg.save('test.svg')


if __name__ == "__main__":
    # print('-' * 20)
    main()
