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
    svg = Svg(800, 600)
    # svg.link("style.css")
    svg.title("Test")
    svg.desc("https://www.netkiller.cn")
    svg.append(Ellipse(60, 30, 30, 15, style="stroke:#006600; fill:#00cc00"))
    svg.append(Ellipse(60, 80, 50, 30, style="stroke: #ff0000;stroke-width: 5;fill: none;"))

    svg.append(Ellipse(130, 160, 50, 30, style="stroke: #ff0000;stroke-width: 5;stroke-dasharray: 10 5;fill: none;"))
    svg.append(Ellipse(60, 160, 50, 30, style="stroke: #ff0000;stroke-width: 5;fill: #ff6666;"))

    svg.append(Ellipse(60, 250, 50, 30, style="stroke: #0000ff;stroke-width: 5;stroke-opacity: 0.5;fill: none;"))
    svg.append(Ellipse(160, 250, 50, 30, style="stroke: none; fill: #0000ff;fill-opacity: 0.5;"))

    svg.save('ellipse.svg')


if __name__ == "__main__":
    main()
