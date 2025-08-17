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
    from netkiller.svg.defs import Marker
    from netkiller.svg.elements import Circle, Path

except ImportError as err:
    print("Error: %s" % (err))
    exit()


def main():
    svg = Svg(800, 600)
    # svg.link("style.css")
    svg.title("Netkiller SVG Library")
    svg.desc("https://www.netkiller.cn")
    markerCircle = Marker('markerCircle', markerWidth="8", markerHeight="8", refX="5", refY="5")
    markerCircle.append(Circle(5, 5, 3, style="stroke: none; fill:#000000;"))
    markerArrow = Marker('markerArrow', markerWidth="13", markerHeight="13", refX="2", refY="6", orient="auto")
    markerArrow.append(Path("M2,2 L2,11 L10,6 L2,2", style="fill: #000000;"))

    svg.defs(markerCircle, markerArrow)
    svg.append(Path("M100,10 L150,10 L150,60",
                    style="stroke: #6666ff; stroke-width: 1px; fill: none;marker-start: url(#markerCircle);marker-end: url(#markerArrow);"))
    svg.save('marker.svg')


if __name__ == "__main__":
    main()
