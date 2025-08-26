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
    from netkiller import Data
    from netkiller.workload import Workload

except ImportError as err:
    print("Error: %s" % (err))
    exit()


def main():
    text = """id,name,start,finish,resource,progress,parent,predecessor,milestone
1,任务组,2023-03-01,2023-03-10,tom,1,0,0,FALSE
2,UI设计,2023-03-03,2023-03-04,neo,0,1,0,FALSE
3,测试环境部署,2023-03-05,2023-03-07,jerry,0,1,2,FALSE
4,后台开发,2023-03-08,2023-03-10,neo,0,1,3,FALSE
5,生产环境部署,2023-03-08,2023-03-10,jerry,2,1,3,FALSE
6,提示词优化,2023-03-15,2023-03-20,neo,2,0,0,FALSE
7,Android适配,2023-03-02,2023-03-03,jam,0,1,0,TRUE
8,安卓接口开发,2023-03-10,2023-03-13,jam,4,0,0,TRUE
9,主任务,2023-03-10,2023-03-19,陈景峰,0,0,0,FALSE
10,子任务1,2023-03-01,2023-03-04,test,0,9,5,FALSE
11,子任务2,2023-03-07,2023-03-09,test,0,9,10,FALSE
12,子任务3,2023-03-16,2023-03-17,test,0,9,11,FALSE
13,任务3,2023-03-15,2023-03-19,test,0,0,0,FALSE
"""
    try:
        with io.StringIO(text) as csv:
            workload = Workload()
            data = workload.csv2workload(csv)
            print(data)
            workload.title("工作负载图")
            workload.department("技术研发部")
            workload.setWorkweeks(6, 1)
            # workload.workload()
            workload.save("workload1.svg")


    except KeyboardInterrupt as e:
        print(e)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
