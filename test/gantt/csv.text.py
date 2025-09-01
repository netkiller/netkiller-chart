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
    from netkiller.gantt import Gantt

except ImportError as err:
    print("Error: %s" % (err))
    exit()


def main():
    text = """id,name,start,finish,resource,progress,parent,predecessor,milestone
1,任务组,2023-03-01,2023-03-10,admin,1,0,0,FALSE
2,aaa,2023-03-03,2023-03-04,test,0,1,0,FALSE
3,bbb,2023-03-05,2023-03-07,,0,1,2,FALSE
4,ccc,2023-03-08,2023-03-10,test,0,1,3,FALSE
5,ddd,2023-03-08,2023-03-10,,2,1,3,FALSE
6,aaa,2023-03-11,2023-03-20,test,2,0,0,FALSE
7,aaabbb,2023-03-02,2023-03-03,closed,0,1,0,TRUE
8,eeeee,2023-03-10,2023-03-13,,4,0,0,TRUE
9,主任务主任务主任务,2023-03-10,2023-03-19,,0,0,0,FALSE
10,子任务1,2023-03-10,2023-03-11,test,0,9,5,FALSE
11,子任务2,2023-03-12,2023-03-14,test,0,9,10,FALSE
12,子任务3,2023-03-15,2023-03-19,test,0,9,11,FALSE
13,任务3,2023-03-15,2023-03-19,test,0,0,0,FALSE"""

    csv = Data()
    data = csv.csvtext(text)

    print(data)
    try:

        gantt = Gantt(data)
        # gantt.hideTable()
        gantt.author("Neo Chen")
        # gantt.setWorkweeks(6, 1)
        gantt.title("甘特图测试")
        # gantt.legend(False)
        # gantt.blank(True)
        gantt.department("技术研发部")
        gantt.save("csv.svg")
    except KeyboardInterrupt as e:
        print(e)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
