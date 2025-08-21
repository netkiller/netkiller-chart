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
    from netkiller.svg.elements import Circle
    from netkiller.svg.filter import Filter, feGaussianBlur


except ImportError as err:
    print("Error: %s" % (err))
    exit()


def main():
    svg = Svg(800, 600)
    # svg.link("style.css")
    svg.title("Test")
    svg.desc("https://www.netkiller.cn")
    filter = Filter(id="blurMe")
    filter.append(feGaussianBlur(inn="SourceGraphic", stdDeviation="5"))
    svg.defs(filter)

    svg.append(Circle(cx="170", cy="60", r="50", fill="green", filter="url(#blurMe)"))

    svg.save('filter.svg')


if __name__ == "__main__":
    main()
