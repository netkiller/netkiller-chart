import svgwrite


def draw_ellipses(filename="ellipses.svg"):
    # 创建SVG绘图对象，尺寸为600x400
    dwg = svgwrite.Drawing(filename, size=(600, 400), profile='tiny')

    # 1. 基本椭圆：中心点(150, 100)，水平半径100，垂直半径50
    # 参数说明：
    # center: (cx, cy) 椭圆中心点坐标
    # r: (rx, ry) 水平半径和垂直半径
    basic_ellipse = dwg.ellipse(center=(150, 100), r=(100, 50),
                                fill="lightblue",  # 填充色
                                stroke="blue",  # 边框色
                                stroke_width=2)  # 边框宽度
    dwg.add(basic_ellipse)
    dwg.add(dwg.text("基本椭圆", insert=(150, 100), text_anchor="middle", dominant_baseline="middle"))

    # 2. 正圆（rx=ry时为圆形）
    circle = dwg.ellipse(center=(400, 100), r=(80, 80),  # rx=ry=80，即圆形
                         fill="lightgreen",
                         stroke="green",
                         stroke_width=2)
    dwg.add(circle)
    dwg.add(dwg.text("正圆 (rx=ry)", insert=(400, 100), text_anchor="middle", dominant_baseline="middle"))

    # 3. 无填充、虚线边框的椭圆
    dashed_ellipse = dwg.ellipse(center=(150, 250), r=(120, 60),
                                 fill="none",  # 无填充
                                 stroke="red",
                                 stroke_width=3,
                                 stroke_dasharray="5,5")  # 虚线样式（5像素实线，5像素空白）
    dwg.add(dashed_ellipse)
    dwg.add(dwg.text("虚线边框", insert=(150, 250), text_anchor="middle", dominant_baseline="middle"))

    # 4. 旋转椭圆（通过transform属性旋转）
    rotated_ellipse = dwg.ellipse(center=(400, 250), r=(100, 50),
                                  fill="pink",
                                  stroke="purple",
                                  stroke_width=2,
                                  transform="rotate(45, 400, 250)")  # 旋转45度，中心点不变
    dwg.add(rotated_ellipse)
    dwg.add(dwg.text("旋转45°", insert=(400, 250), text_anchor="middle", dominant_baseline="middle"))

    # 保存SVG文件
    dwg.save()
    print(f"椭圆示例已保存为: {filename}")


# 调用函数生成SVG
draw_ellipses()