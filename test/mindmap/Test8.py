import svgwrite


def create_simple_connection(filename="simple_connection.svg"):
    """创建简化的节点连接示例SVG"""
    # 创建SVG文档
    dwg = svgwrite.Drawing(filename, size=('400px', '300px'), viewBox='0 0 400 300')

    # 节点A (位置较高)
    node_a = (100, 100)  # 节点A的中心位置
    dwg.add(dwg.circle(center=node_a, r=20, fill='#4CAF50'))  # 绿色圆形
    dwg.add(dwg.text('A', insert=(node_a[0], node_a[1] + 5),
                     text_anchor='middle', font_size='14px', font_family='Arial'))

    # 节点B (位置较低)
    node_b = (300, 200)  # 节点B的中心位置
    dwg.add(dwg.circle(center=node_b, r=20, fill='#2196F3'))  # 蓝色圆形
    dwg.add(dwg.text('B', insert=(node_b[0], node_b[1] + 5),
                     text_anchor='middle', font_size='14px', font_family='Arial'))

    # 计算贝塞尔曲线的控制点
    # 控制点1: 从节点A向右偏移
    control1 = (node_a[0] + 60, node_a[1])
    # 控制点2: 从节点B向左偏移并稍微向上
    control2 = (node_b[0] - 60, node_b[1] - 30)

    # 绘制贝塞尔曲线连接两个节点
    path = dwg.path(d=f'M {node_a[0] + 20}, {node_a[1]}',  # 从节点A的右侧开始
                    fill='none', stroke='#FF5722', stroke_width=3)
    path.push(f'L {node_a[0] + 100}, {node_a[1]}')
    path.push(f'C {control1[0]}, {control1[1]}, {control2[0]}, {control2[1]}, {node_b[0] - 20}, {node_b[1]}')
    path.push(f'L {node_b[0] + 100}, {node_b[1]}')
    dwg.add(path)

    # 保存SVG文件
    dwg.save()
    print(f"SVG文件已保存为: {filename}")


if __name__ == "__main__":
    create_simple_connection()
