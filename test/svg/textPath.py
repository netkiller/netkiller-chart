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
    from netkiller.svg.elements import Text, Path, TextPath

except ImportError as err:
    print("Error: %s" % (err))
    exit()


def main():
    svg = Svg(viewBox="0 0 100 100")
    svg.title("Svg 图形库")
    svg.desc("https://www.netkiller.cn")
    svg.defs(Path(id="MyPath",
                  fill="none",
                  stroke="red",
                  d="M10,90 Q90,90 90,45 Q90,10 50,10 Q10,10 10,40 Q10,70 45,70 Q70,70 75,50"))
    text = Text()
    svg.append(text.append(TextPath(href="MyPath", text="Quick brown fox jumps over the lazy dog.")))
    svg.save('textpath.svg')


if __name__ == "__main__":
    main()
