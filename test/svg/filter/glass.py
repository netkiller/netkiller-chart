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
    from netkiller.svg.elements import Rectangle, Group, Text
    from netkiller.svg.filter import Filter, feOffset, feGaussianBlur, feComposite, feColorMatrix, feBlend


except ImportError as err:
    print("Error: %s" % (err))
    exit()


def main():
    svg = Svg(800, 600)
    # svg.link("style.css")
    svg.title("Netkiller Python 手札")
    svg.desc("https://www.netkiller.cn")
    filter = Filter(id="glass", filterUnits="userSpaceOnUse", color_interpolation_filters="sRGB")
    filter.append(feColorMatrix(inn="SourceAlpha", type="matrix", values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0",
                                result="hardAlpha"))

    filter.append(feOffset(dx="4", dy="4"))
    filter.append(feGaussianBlur(stdDeviation="2"))
    filter.append(feColorMatrix(type="matrix", values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.25 0"))
    filter.append(feBlend(mode="normal", inn="SourceGraphic", in2="effect1_dropShadow_130_286", result="shape"))

    # 内
    filter.append(feOffset(dx="4", dy="4"))
    filter.append(feGaussianBlur(stdDeviation="2"))
    filter.append(feComposite(in2="hardAlpha", operator="arithmetic", k2="-1", k3="1"))
    filter.append(feColorMatrix(type="matrix", values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.25 0"))
    filter.append(feBlend(mode="normal", in2="shape", result="effect2_innerShadow_130_286"))

    filterText = Filter(id="text", filterUnits="userSpaceOnUse", color_interpolation_filters="sRGB").append(
        feColorMatrix(inn="SourceAlpha", type="matrix", values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0",
                      result="hardAlpha")
    ).append(
        feOffset(dx="4", dy="4")
    ).append(
        feGaussianBlur(stdDeviation="2")
    ).append(
        feComposite(in2="hardAlpha", operator="out")
    ).append(
        feColorMatrix(type="matrix", values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.25 0")).append(
        feBlend(mode="normal", inn="SourceGraphic", in2="effect1_dropShadow_103_1497", result="shape")
    )

    svg.defs(filter, filterText)

    g = Group(filter="url(#glass)")
    g.append(Rectangle(x="1", y="1", width="600", height="60", stroke="none", fill="#D9D9D9"))
    g.append(Text("Netkiller Python 手札", 10, 40, font_size=30, stroke="none", fill="red", filter="url(#text)"))
    svg.append(g)
    svg.append(
        Rectangle(x="1", y="180", width="400", height="60", stroke="white", fill="#E23368", filter="url(#glass)"))
    svg.append(Rectangle(x="1",
                         y="90",
                         width="400",
                         height="70",
                         stroke="none",
                         fill="green",
                         filter="url(#glass)"))

    g = Group(filter="url(#glass)")
    g.append(Rectangle(x="10", y="250", width="600", height="30", stroke="none", fill="white"))
    g.append(
        Rectangle(x="15", y="255", width="400", height="20", stroke="none", fill="#E23368"))
    svg.append(g)

    svg.save('glass.svg')


if __name__ == "__main__":
    main()
