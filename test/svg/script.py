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
    svg = Svg(viewBox="0 0 10 10",
              height="120px",
              width="120px")
    # svg.link("style.css")
    svg.title("Svg 图形库")
    svg.desc("https://www.netkiller.cn")
    svg.append(Circle(cx="5", cy="5", r="4"))

    svg.script("""
    function getColor() {
      const R = Math.round(Math.random() * 255)
        .toString(16)
        .padStart(2, "0");

      const G = Math.round(Math.random() * 255)
        .toString(16)
        .padStart(2, "0");

      const B = Math.round(Math.random() * 255)
        .toString(16)
        .padStart(2, "0");

      return `#${R}${G}${B}`;
    }

    document.querySelector("circle").addEventListener("click", (e) => {
      e.target.style.fill = getColor();
    });
    """)

    svg.save('script.svg')


if __name__ == "__main__":
    main()
