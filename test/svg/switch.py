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
    from netkiller.svg.elements import Text, Line, Circle, Switch

except ImportError as err:
    print("Error: %s" % (err))
    exit()


def main():
    svg = Svg(viewBox="0 -20 100 50")
    svg.title("Svg 图形库")
    svg.desc("https://www.netkiller.cn")
    switch = Switch(Text("@"))
    switch.append(Text("مرحبا", systemLanguage="ar")).append(Text("Hallo!", systemLanguage="de,nl")).append(
        Text("Howdy!", systemLanguage="en-us")).append(Text("Wotcha! ", systemLanguage="en-gb")).append(
        Text("G'day!", systemLanguage="en-au")).append(Text("Hello!", systemLanguage="en")).append(
        Text("Hola!", systemLanguage="es")).append(Text("Bonjour!", systemLanguage="fr")).append(
        Text("こんにちは", systemLanguage="ja")).append(Text("zПривет! ", systemLanguage="ru")).append(
        Text("你好！ ", systemLanguage="zh"))
    svg.append(switch)
    svg.save('switch.svg')


if __name__ == "__main__":
    main()
