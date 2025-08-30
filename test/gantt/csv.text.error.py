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
    from netkiller import Data
    from netkiller.gantt import Gantt

except ImportError as err:
    print("Error: %s" % (err))
    exit()


def main():
    text = """id,name,start,finish,resource,progress,parent,predecessor,milestone
185,居家办公申请流程,2025-08-23,2025-08-24,行政部门,0,0,0,FALSE
186,行政统计工作,2025-08-25,2025-08-26,行政部门,0,0,0,FALSE
194,虚拟白板系统部署,2025-08-23,2025-08-24,IT部门,0,185,0,FALSE
195,居家办公申请流程设计,2025-08-24,2025-08-25,行政部门,0,0,0,FALSE
196,考勤制度调整,2025-08-25,2025-08-26,人力资源,0,0,0,FALSE
197,每日视频会议安排,2025-08-26,2025-08-26,行政部门,0,0,0,FALSE
198,工作进度同步机制,2025-08-26,2025-08-27,各部门主管,0,0,0,FALSE
199,员工健康提醒机制,2025-08-28,2025-08-29,行政部门,0,0,0,FALSE
203,每日视频会议安排,2025-08-23,2025-08-23,行政部门,0,185,0,FALSE
204,居家办公申请流程制定,2025-08-23,2025-08-24,行政部门,0,0,0,FALSE
205,行政部门统计工作,2025-08-24,2025-08-25,行政部门,0,0,0,FALSE
206,员工身心健康关注,2025-08-25,2025-08-26,HR部门,0,0,199,FALSE
207,社交互动活动安排,2025-08-26,2025-08-27,HR部门,0,0,0,FALSE
211,效率保障措施,2025-08-23,2025-08-24,发言人2,0,208,0,FALSE
212,行政部门统计,2025-08-24,2025-08-25,行政部门,0,208,0,FALSE
213,饮食与运动提醒,2025-08-25,2025-08-26,发言人1,0,208,0,FALSE
214,社交活动安排,2025-08-26,2025-08-27,发言人3,0,208,0,FALSE
215,虚拟白板系统维护,2025-08-27,2025-08-28,IT部门,0,208,0,FALSE
216,视频会议系统优化,2025-08-28,2025-08-29,IT部门,0,208,0,FALSE
232,安排每日视频会议            ,2025-08-23,2025-08-30,行政部门,0,0,0,FALSE
236,虚拟白板系统维护,2025-08-23,2025-08-23,IT部门,0,234,0,FALSE
238,行政部门统计数据,2025-08-23,2025-08-23,行政部门,0,234,0,FALSE
240,设计虚拟白板系统使用指南,2025-08-23,2025-08-24,IT部,0,0,0,FALSE
242,制定居家办公考勤管理办法,2025-08-23,2025-08-24,HR部,0,0,0,FALSE
244,准备居家办公设备清单,2025-08-24,2025-08-25,IT部,0,0,0,FALSE
245,编制居家办公健康指南,2025-08-25,2025-08-26,发言人3,0,0,0,FALSE
246,规划社交活动安排,2025-08-26,2025-08-27,发言人1,0,0,0,FALSE"""

    text1 = "id,name,start,finish,resource,progress,parent,predecessor,milestone"

    csv = Data()
    data = csv.csvtext(text1)
    print(data)
    try:

        gantt = Gantt(data)
        # gantt.hideTable()
        gantt.author("Neo Chen")
        gantt.setWorkweeks(6, 1)
        gantt.title("甘特图测试")
        # gantt.legend(False)
        # gantt.blank(True)
        gantt.department("技术研发部")
        gantt.save("csv.error.svg")
    except KeyboardInterrupt as e:
        print(e)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
