import svgwrite


def create_bezier_example(filename="bezier_curves.svg"):
    """创建贝塞尔曲线SVG示例"""
    # 创建SVG文档，设置视图框
    dwg = svgwrite.Drawing(filename, size=('600px', '400px'), viewBox='0 0 600 400')

    # 添加标题
    dwg.add(dwg.text('贝塞尔曲线示例', insert=(300, 30), text_anchor='middle',
                     font_size='20px', font_family='Arial'))

    # 1. 绘制二次贝塞尔曲线 (Q)
    quadratic_path = dwg.path(d='M 100,100', fill='none', stroke='blue', stroke_width=2)
    quadratic_path.push('Q 200,50 300,100')  # 控制点 (200,50), 终点 (300,100)
    dwg.add(quadratic_path)

    # 添加控制点标记和标签
    dwg.add(dwg.circle(center=(200, 50), r=5, fill='red'))
    dwg.add(dwg.text('控制点', insert=(210, 45), font_size='12px', font_family='Arial'))
    dwg.add(dwg.text('二次贝塞尔曲线', insert=(200, 120), text_anchor='middle', font_size='14px', font_family='Arial'))

    # 2. 绘制三次贝塞尔曲线 (C)
    cubic_path = dwg.path(d='M 100,200', fill='none', stroke='green', stroke_width=2)
    cubic_path.push('C 150,150 250,250 300,200')  # 控制点1 (150,150), 控制点2 (250,250), 终点 (300,200)
    dwg.add(cubic_path)

    # 添加控制点标记和标签
    dwg.add(dwg.circle(center=(150, 150), r=5, fill='red'))
    dwg.add(dwg.circle(center=(250, 250), r=5, fill='red'))
    dwg.add(dwg.text('控制点1', insert=(160, 145), font_size='12px', font_family='Arial'))
    dwg.add(dwg.text('控制点2', insert=(260, 245), font_size='12px', font_family='Arial'))
    dwg.add(dwg.text('三次贝塞尔曲线', insert=(200, 230), text_anchor='middle', font_size='14px', font_family='Arial'))

    # 3. 绘制平滑三次贝塞尔曲线 (S)
    smooth_cubic_path = dwg.path(d='M 100,300 C 150,250 175,350 225,300', fill='none', stroke='purple', stroke_width=2)
    smooth_cubic_path.push('S 275,250 300,300')  # 自动计算反射控制点, 控制点2 (275,250), 终点 (300,300)
    dwg.add(smooth_cubic_path)

    # 添加控制点标记和标签
    dwg.add(dwg.circle(center=(275, 250), r=5, fill='red'))
    dwg.add(dwg.text('控制点2', insert=(285, 245), font_size='12px', font_family='Arial'))
    dwg.add(
        dwg.text('平滑三次贝塞尔曲线', insert=(200, 330), text_anchor='middle', font_size='14px', font_family='Arial'))

    # 保存SVG文件
    dwg.save()
    print(f"SVG文件已保存为: {filename}")


if __name__ == "__main__":
    create_bezier_example()
