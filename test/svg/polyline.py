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
    from netkiller.svg.elements import Polyline, Polygon

except ImportError as err:
    print("Error: %s" % (err))
    exit()


def main():
    svg = Svg(800, 600)
    # svg.link("style.css")
    svg.title("Test")
    svg.desc("https://www.netkiller.cn")
    svg.append(Polyline("20,100 40,60 70,80 100,20", fill="none", stroke="black"))
    svg.append(Polyline((60, 30), (30, 15), style="stroke:#006600; fill:#00cc00"))
    svg.append(Polyline("0,0  30,0  15,30", style="stroke:#006600;"))
    svg.append(Polygon("10,0  60,0  35,50", style="stroke: #ff0000;stroke-width: 5;fill: #ff6666;"))
    svg.append(Polygon("60,20 100,40 100,80 60,100 20,80 20,40",
                       style="stroke: #0000ff;stroke-width: 5;stroke-opacity: 0.5;fill: none;"))

    svg.append(Polygon("50,5   100,5  125,30  125,80 100,105 50,105  25,80  25, 30",
                       style="stroke:#660000; fill:#cc3333; stroke-width: 3;"))
    svg.append(Polygon("100,10 40,180 190,60 10,60 160,180",
                       style="fill:lime;stroke:purple;stroke-width:5;fill-rule:nonzero;"))

    svg.save('polyline.svg')


if __name__ == "__main__":
    main()
