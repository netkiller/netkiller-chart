
# import svgwrite
from svgwrite import cm, mm


def create_mind_map(filename):
    # 创建SVG画布（尺寸：800x600像素）
    dwg = svgwrite.Drawing(filename, size=(800, 600), profile='full')

    # 定义样式（颜色、字体等）
    styles = """
        .center-node { fill: #4a90e2; stroke: #333; stroke-width: 2; }
        .center-text { font-family: Arial; font-size: 16px; font-weight: bold; fill: white; text-anchor: middle; dominant-baseline: middle; }
        .level1-node { fill: #5cb85c; stroke: #333; stroke-width: 1.5; rx: 5; ry: 5; } /* 带圆角的矩形 */
        .level1-text { font-family: Arial; font-size: 14px; fill: white; text-anchor: middle; dominant-baseline: middle; }
        .level2-node { fill: #f0ad4e; stroke: #333; stroke-width: 1; rx: 3; ry: 3; }
        .level2-text { font-family: Arial; font-size: 12px; fill: #333; text-anchor: middle; dominant-baseline: middle; }
        .connection { stroke: #666; stroke-width: 1.5; fill: none; }
    """
    dwg.defs.add(dwg.style(styles))

    # 中心节点（坐标：400, 300，尺寸：100x60）
    center_x, center_y = 400, 300
    dwg.add(dwg.rect(
        (center_x - 50, center_y - 30),  # 左上角坐标
        (100, 60),  # 宽高
        class_='center-node'
    ))
    dwg.add(dwg.text('中心主题', (center_x, center_y), class_='center-text'))

    # 一级分支与子节点（3个方向：上、右、下）
    # 1. 上方分支
    level1_top_x, level1_top_y = 400, 180  # 一级节点坐标
    # 连接线（贝塞尔曲线：从中心到一级节点，控制点调整弧度）
    dwg.add(dwg.path(
        d=f'M {center_x} {center_y - 30} C {center_x} {center_y - 60}, {center_x} {level1_top_y + 30}, {level1_top_x} {level1_top_y + 30}',
        class_='connection'
    ))
    # 一级节点
    dwg.add(dwg.rect((level1_top_x - 80, level1_top_y - 20), (160, 40), class_='level1-node'))
    dwg.add(dwg.text('分支1', (level1_top_x, level1_top_y), class_='level1-text'))
    # 分支1的子节点（左、右）
    level2_top_left_x, level2_top_left_y = 300, 120
    level2_top_right_x, level2_top_right_y = 500, 120
    # 子节点连接线
    dwg.add(dwg.path(
        d=f'M {level1_top_x - 60} {level1_top_y} C {level1_top_x - 100} {level1_top_y}, {level2_top_left_x + 30} {level1_top_y - 30}, {level2_top_left_x + 30} {level2_top_left_y}',
        class_='connection'
    ))
    dwg.add(dwg.path(
        d=f'M {level1_top_x + 60} {level1_top_y} C {level1_top_x + 100} {level1_top_y}, {level2_top_right_x - 30} {level1_top_y - 30}, {level2_top_right_x - 30} {level2_top_left_y}',
        class_='connection'
    ))
    # 子节点
    dwg.add(dwg.rect((level2_top_left_x - 60, level2_top_left_y - 15), (120, 30), class_='level2-node'))
    dwg.add(dwg.text('子分支1-1', (level2_top_left_x, level2_top_left_y), class_='level2-text'))
    dwg.add(dwg.rect((level2_top_right_x - 60, level2_top_right_y - 15), (120, 30), class_='level2-node'))
    dwg.add(dwg.text('子分支1-2', (level2_top_right_x, level2_top_right_y), class_='level2-text'))

    # 2. 右侧分支
    level1_right_x, level1_right_y = 580, 300
    dwg.add(dwg.path(
        d=f'M {center_x + 30} {center_y} C {center_x + 60} {center_y}, {level1_right_x - 30} {center_y}, {level1_right_x - 30} {level1_right_y}',
        class_='connection'
    ))
    dwg.add(dwg.rect((level1_right_x - 80, level1_right_y - 20), (160, 40), class_='level1-node'))
    dwg.add(dwg.text('分支2', (level1_right_x, level1_right_y), class_='level1-text'))
    # 分支2的子节点（上、下）
    level2_right_top_x, level2_right_top_y = 580, 240
    level2_right_bottom_x, level2_right_bottom_y = 580, 360
    dwg.add(dwg.path(
        d=f'M {level1_right_x} {level1_right_y - 20} C {level1_right_x} {level1_right_y - 60}, {level1_right_x} {level2_right_top_y + 20}, {level2_right_top_x} {level2_right_top_y + 20}',
        class_='connection'
    ))
    dwg.add(dwg.path(
        d=f'M {level1_right_x} {level1_right_y + 20} C {level1_right_x} {level1_right_y + 60}, {level1_right_x} {level2_right_bottom_y - 20}, {level2_right_bottom_x} {level2_right_bottom_y - 20}',
        class_='connection'
    ))
    dwg.add(dwg.rect((level2_right_top_x - 60, level2_right_top_y - 15), (120, 30), class_='level2-node'))
    dwg.add(dwg.text('子分支2-1', (level2_right_top_x, level2_right_top_y), class_='level2-text'))
    dwg.add(dwg.rect((level2_right_bottom_x - 60, level2_right_bottom_y - 15), (120, 30), class_='level2-node'))
    dwg.add(dwg.text('子分支2-2', (level2_right_bottom_x, level2_right_bottom_y), class_='level2-text'))

    # 3. 下方分支
    level1_bottom_x, level1_bottom_y = 400, 420
    dwg.add(dwg.path(
        d=f'M {center_x} {center_y + 30} C {center_x} {center_y + 60}, {center_x} {level1_bottom_y - 30}, {level1_bottom_x} {level1_bottom_y - 30}',
        class_='connection'
    ))
    dwg.add(dwg.rect((level1_bottom_x - 80, level1_bottom_y - 20), (160, 40), class_='level1-node'))
    dwg.add(dwg.text('分支3', (level1_bottom_x, level1_bottom_y), class_='level1-text'))
    # 分支3的子节点（左、右）
    level2_bottom_left_x, level2_bottom_left_y = 300, 480
    level2_bottom_right_x, level2_bottom_right_y = 500, 480
    dwg.add(dwg.path(
        d=f'M {level1_bottom_x - 60} {level1_bottom_y} C {level1_bottom_x - 100} {level1_bottom_y}, {level2_bottom_left_x + 30} {level1_bottom_y + 30}, {level2_bottom_left_x + 30} {level2_bottom_left_y}',
        class_='connection'
    ))
    dwg.add(dwg.path(
        d=f'M {level1_bottom_x + 60} {level1_bottom_y} C {level1_bottom_x + 100} {level1_bottom_y}, {level2_bottom_right_x - 30} {level1_bottom_y + 30}, {level2_bottom_right_x - 30} {level2_bottom_left_y}',
        class_='connection'
    ))
    dwg.add(dwg.rect((level2_bottom_left_x - 60, level2_bottom_left_y - 15), (120, 30), class_='level2-node'))
    dwg.add(dwg.text('子分支3-1', (level2_bottom_left_x, level2_bottom_left_y), class_='level2-text'))
    dwg.add(dwg.rect((level2_bottom_right_x - 60, level2_bottom_right_y - 15), (120, 30), class_='level2-node'))
    dwg.add(dwg.text('子分支3-2', (level2_bottom_right_x, level2_bottom_right_y), class_='level2-text'))

    # 保存SVG文件
    dwg.save()


# 生成思维导图SVG
create_mind_map('mind_map.svg')