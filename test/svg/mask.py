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
    from netkiller.svg.defs import Mask
    from netkiller.svg.elements import Text, Path, Rectangle

except ImportError as err:
    print("Error: %s" % (err))
    exit()


def main():
    svg = Svg(800, 600, viewBox="0 0 200 80", version="1.1")
    # svg.link("style.css")
    svg.title("Netkiller SVG Library")
    svg.desc("https://www.netkiller.cn")
    # mask = Mask(id="mask1", x="0", y="0", width="100", height="100")
    # mask.append(Rectangle(x="0", y="0", width="100", height="100", style="stroke:none; fill: #ffffff"))
    # svg.defs(mask)
    # svg.append(
    #     Rectangle(x="1", y="1", width="200", height="200", style="stroke: none; fill: #0000ff; mask: url(#mask1)"))

    mask = Mask(id="myMask", maskUnits="userSpaceOnUse",
                x="0", y="0", width="200", height="80")
    mask.append(Rectangle(x="0", y="0", width="100", height="80", fill="white"))
    svg.defs(mask)
    svg.defs(
        Text(id="Text", x="100", y="48", text="Black &amp; White", font_size="26", font_weight="bold",
             text_anchor="middle"))
    svg.append(
        Rectangle(x="100", y="10", width="95", height="60"))
    svg.use(id="Text", fill="white")
    svg.use(id="Text", fill="black", mask="url(#myMask)")
    svg.save('mask.svg')


if __name__ == "__main__":
    main()
