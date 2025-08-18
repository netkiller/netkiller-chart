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
    from netkiller.svg import Svg
    # from netkiller.svg.ScalableVectorGraphics import Svg
    from netkiller.svg.defs import Marker
    from netkiller.svg.elements import Circle, Path, Rectangle

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

    svg1 = Svg(800, 600)
    # svg.link("style.css")
    svg1.title("Netkiller SVG Library")
    svg1.desc("https://www.netkiller.cn")
    svg1.style("""
    circle {
           stroke: #006600;
           fill:   #00cc00;
    }    
    """)

    markerSquare = Marker(id="markerSquare", markerWidth="7", markerHeight="7", refX="4", refY="4", orient="auto")
    markerSquare.append(Rectangle(x="1", y="1", width="5", height="5", style="stroke: none; fill:#000000;"))

    markerCircle = Marker('markerCircle', markerWidth="8", markerHeight="8", refX="5", refY="5")
    markerCircle.append(Circle(5, 5, 3, style="stroke: none; fill:#000000;"))

    markerArrow = Marker('markerArrow', markerWidth="13", markerHeight="13", refX="2", refY="7", orient="auto")
    markerArrow.append(Path("M2,2 L2,13 L8,7 L2,2", style="fill: #000000;"))

    svg1.defs(markerCircle, markerSquare, markerArrow)
    svg1.append(Path("M100,10 L150,10 L150,60",
                     style="stroke: #6666ff; stroke-width: 1px; fill: none;marker-start: url(#markerCircle);marker-mid: url(#markerSquare);marker-end: url(#markerArrow);"))
    svg1.save('marker1.svg')


if __name__ == "__main__":
    main()
