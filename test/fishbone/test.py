import os
import sys

# module = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.insert(0, ".")
# sys.path.insert(1, module)
src = os.path.join(os.path.dirname(os.path.dirname(os.getcwd())), 'src')
sys.path.insert(2, src)
# print(src)
# print(module)


try:
    import io
    from netkiller.fishbone import Fishbone
    from netkiller.markdown import Markdown

except ImportError as err:
    print("Error: %s" % (err))
    exit()


def main():
    text = """
# 石川鱼骨图
- 产品目标
  - 竞品分析
  - 品牌形象
  - 产品生命周期
  - 发现了一个名
- 开发目标
  - 编码开发
  - 代码测试
- 运营目标
  - 区域投放
- 运营目标1
  - 区域投放1
  - 区域投放2
  - 区域投放3
  - 区域投放4
  - 区域投放5
- 运营目标1运营
  - 区域投放11
  - 区域投放21    
  - 区域投放31区域投放31
  - 区域投放41
  - 区域投放51
- 区域投放513
  - 竞品分析
  - 品牌形象
  - 产品生命周期
  - 发现了一个名
  - 区域投放3
  - 区域投放4
  - 区域投放5
- 运营目标1运营99
  - 区域投放11
  - 区域投放21
  - 区域投放31  
        """

    text2 = """
    
- 区域投放31区域投放31
  - 产品生命周期产品生命周期产品生命周期产品生命周期
  - 产品生命周期产品生命周期产品生命周期产品生命周期
  - 产品生命周期
- 产品生命周期
  - 发现了一个名
  - 区域投放3
  - 区域投放4生命周期产品
- 生命周期产品生命周生命周期产品生命周期产品
  - 生命周生命周期产品生命周期产品生命周
  - 区域投放5
- 运营目标1运营99
  - 区域投放11
  - 区域投放21
  - 区域投放31    
    """
    #     - 运营目标1运营99
    #     - 区域投放11
    #     - 区域投放21
    #     - 区域投放31
    #     - 区域投放513
    #     - 竞品分析
    #     - 品牌形象
    #
    #
    test3 = """
- 居家办公效率问题
  - 任务量暴涨导致延期
  - 办公室频繁被打断影响专注
  - 通勤时间占用导致加班成本增加
  - 协作工具操作不熟练
  - 缺少工作与生活的时间界限

- 居家办公体验问题
  - 缺少升降桌等办公设备
  - 缺乏零食水果等福利
  - 需要自行解决饮食问题
  - 缺少运动场景
  - 社交交流减少

- 居家办公试行方案执行问题
  - 试行时间周期较短
  - 到岗与居家天数分配可能不合理
  - 申请流程存在滞后性
  - 视频会议系统使用频率过高
  - 行政部门统计工作负荷增加    
    """
    text1 = """
- 如何提高移山效率
  - 工具选择单一
  - 缺乏现代化设备
  - 人力劳动强度大
  - 缺乏团队协作
  - 未考虑环境影响

- 移山工具优化方案
  - 传统工具效率低下
  - 未引入机械作业
  - 工具维护不足
  - 工具使用培训缺乏
  - 工具更新不及时  

    """
    text4 = """
- 工具选择低效
  - 缺乏现代化设备
  - 仅依赖传统工具
  - 未评估工具效率

- 人力成本过高
  - 过分依赖人工操作
  - 未考虑机械化替代方案
  - 劳动力分配不合理

- 工程进度缓慢
  - 工具效率低下
  - 缺乏科学施工规划
  - 未制定明确时间表

- 施工方法单一
  - 局限于传统挖掘方式
  - 未考虑爆破等现代技术
  - 缺乏多方法协同作业    
    """

    text5 = """
- 居家办公影响工作效率
  - 任务量暴涨导致延期
  - 办公室频繁被打断
  - 通勤时间占用导致加班费增加
- 居家办公造成生活作息紊乱
  - 缺乏场景切换导致时间管理混乱
  - 报复性熬夜现象严重
  - 没有固定上下班时间界限
- 居家办公设备条件不足
  - 缺乏专业办公桌椅
  - 长时间通话设备不适
  - 缺少办公室零食补给
- 居家办公影响身心健康
  - 缺乏运动空间和动力
  - 饮食规律被打破
  - 社交活动骤减
- 协作工具使用问题
  - 虚拟白板系统操作不熟练
  - 新工具需要适应期
  - 缺乏现场协作的即时性
- 成本控制问题
  - 加班费支出增加
  - 需要额外设备投入
  - 通勤补贴计算困难
- 工作生活界限模糊
  - 无法区分工作和休息空间
  - 工作时间内易受家庭事务干扰
  - 缺少同事监督机制
- 团队沟通效率下降
  - 视频会议替代现场会议效果欠佳
  - 非正式沟通渠道减少
  - 信息同步存在延迟
- 试行方案执行困难
  - 自主选择机制不明确
  - 申请流程复杂
  - 考勤管理难度增大
- 技术支持不足
  - 系统稳定性待验证
  - IT支持响应速度慢
  - 家庭网络环境差异大
"""
    # markdown = Markdown()
    # data = markdown.fishbone()
    # print(data)
    fishbone = Fishbone()

    fishbone.title("石川鱼骨图")
    fishbone.department("技术研发部")
    # fishbone.border(5)
    fishbone.legend(False)
    # fishbone.markdown(test3)
    # fishbone.save("test3.svg")
    #
    # fishbone.markdown(text2)
    # fishbone.save("test2.svg")
    #
    # fishbone.markdown(text)
    # fishbone.save("test1.svg")
    #
    # fishbone.markdown(text1)
    # fishbone.save("test1.svg")
    #
    # fishbone.markdown(text4)
    # fishbone.save("test4.svg")

    fishbone.markdown(text5)
    fishbone.save("test5.svg")
    # fishbone.debug()
    # print(fishbone.show())


if __name__ == "__main__":
    main()
