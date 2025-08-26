import os
import sys

# module = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ".")
# sys.path.insert(1, module)
src = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.getcwd()))), 'src')
sys.path.insert(1, src)
# print(src)
# print(module)

try:
    from netkiller.svg.ScalableVectorGraphics import Svg
    from netkiller.svg.elements import Text, Group
    from netkiller.svg.filter import Filter, feOffset, feGaussianBlur, feColorMatrix, feComposite


except ImportError as err:
    print("Error: %s" % (err))
    exit()


def main():
    svg = Svg(800, 600)
    # svg.link("style.css")
    svg.title("Netkiller Python 手札")
    svg.desc("https://www.netkiller.cn")
    filter = Filter(id="text1")
    filter.append(feGaussianBlur(inn="SourceGraphic", stdDeviation="2", result="blur"))
    filter.append(
        feColorMatrix(inn="blur", mode="matrix", values="1 0 0 0 0  0 1 0 0 0  0 0 1 0 0  0 0 0 19 -9", result="text1"))
    filter.append(feComposite(inn="SourceGraphic", in2="text1", operator="atop"))

    svg.defs(filter)
    g = Group(filter="url(#text1)")
    g.append(Text("Hello world", 100, 200, font_size=40, stroke="none", fill="red"))
    svg.append(g)

    svg.save('text.svg')


if __name__ == "__main__":
    main()
