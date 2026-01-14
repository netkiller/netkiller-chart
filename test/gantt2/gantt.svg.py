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
    from netkiller.data import Data
    from netkiller.gantt2 import Gantt

except ImportError as err:
    print("Error: %s" % (err))
    exit()


def main():
    text = """id,name,start,finish,resource,progress,parent,predecessor,milestone
1,魔簧1.4.8开发计划,2025-12-24,2025-12-31,,1,0,0,FALSE
2,增加负载均衡,2025-12-24,2025-12-26,陈景峰,0,1,0,FALSE
3,安卓包裁剪,2025-12-24,2025-12-26,詹子聪,0,1,0,FALSE
4,SIM卡切换,2025-12-29,2025-12-31,詹子聪,0,1,0,FALSE
5,识别会议主题,2025-12-29,2025-12-31,陈景峰,2,1,0,FALSE
6,观点生成频率调整,2025-12-29,2025-12-31,詹子聪,2,1,0,FALSE
7,会议监控,2025-12-29,2025-12-31,陈景峰,0,1,0,FALSE
8,设备留言,2025-12-29,2025-12-30,陈景峰,0,1,2,FALSE
9,🎉1.4.8升级,2025-12-31,2025-12-31,,0,0,0,TRUE
10,魔簧1.4.8开发计划,2026-01-04,2026-01-09,,0,0,0,FALSE
11,垂直行业提示词功能,2026-01-04,2026-01-09,陈景峰,0,9,0,FALSE
12,集成PPT,2026-01-04,2026-01-09,陈景峰,0,9,10,FALSE
13,待定任务,2026-01-04,2026-01-09,詹子聪,0,9,11,FALSE
14,🎉1.4.8升级,2026-01-09,2026-01-09,test,0,0,0,TRUE
"""

    csv = Data()
    data = csv.csvtext(text)

    print(data)
    # try:

    gantt = Gantt(data)
    # gantt.showTable = False
    # gantt.showHeader = False
    gantt.title("魔簧智脑开发计划")
    # gantt.table(True)
    # gantt.author("Neo Chen")
    # # gantt.setWorkweeks(6, 1)

    # gantt.legend(False)
    # # gantt.blank(True)
    gantt.department("一体机/云平台/后台/小程序")
    # print(gantt.show())
    gantt.save("gantt.svg")
    # print(gantt.header())
    # print(gantt.body())

    # except KeyboardInterrupt as e:
    #     print(e)
    # except Exception as e:
    #     print(e)


if __name__ == "__main__":
    main()
