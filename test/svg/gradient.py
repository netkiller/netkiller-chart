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
    from netkiller.svg.gradient import linearGradient, radialGradient, stop
except ImportError as err:
    print("Error: %s" % (err))
    exit()


def main():
    svg = Svg(viewBox="0 0 40 40",
              height="120px",
              width="120px")

    svg.title("Svg 图形库")
    svg.desc("https://www.netkiller.cn")

    linear = linearGradient(id="linearGradient", gradientTransform="rotate(90)")
    linear.append(stop(offset="5%", stop_color="gold"))
    linear.append(stop(offset="95%", stop_color="red"))

    radial = radialGradient(id="radialGradient")
    radial.append(stop(offset="10%", stop_color="gold"))
    radial.append(stop(offset="95%", stop_color="red"))

    svg.defs(linear, radial)
    svg.comment("using my linear gradient")
    svg.append(Circle(cx="5", cy="5", r="4", fill="url('#linearGradient')"))
    svg.comment("using my radial gradient")
    svg.append(Circle(cx="5", cy="20", r="4", fill="url('#radialGradient')"))

    svg.save('gradient.svg')


if __name__ == "__main__":
    main()
