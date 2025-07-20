import svgwrite


def draw_bezier_connection(dwg, start, end, color="#666", width=2):
    """绘制贝塞尔曲线连接"""
    # 计算控制点
    control1 = (start[0] + 50, start[1])  # 第一个控制点
    control2 = (end[0] - 50, end[1])  # 第二个控制点

    # 创建贝塞尔曲线路径
    path = dwg.path(
        d=f"M {start[0]} {start[1]} C {control1[0]} {control1[1]}, "
          f"{control2[0]} {control2[1]}, {end[0]} {end[1]}",
        stroke=color,
        fill="none",
        stroke_width=width
    )

    # 添加箭头
    arrow = dwg.polygon(
        points=[
            (end[0], end[1]),
            (end[0] - 10, end[1] - 5),
            (end[0] - 10, end[1] + 5)
        ],
        fill=color
    )

    dwg.add(path)
    dwg.add(arrow)


# 使用示例
dwg = svgwrite.Drawing("connection.svg", size=("400px", "200px"))
draw_bezier_connection(dwg, (100, 50), (250, 100))
dwg.save()