import os
import sys

# module = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
module = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, module + '/src')
print(module)

from netkiller.gantt import Gantt


def main():
    data = {
        "1": {
            "id": 1,
            "name": "开发需求排期",
            "start": "2023-02-22",
            "finish": "2023-03-03",
            "subitem": {
                "11": {
                    "id": 11,
                    "name": "用户登录开发",
                    "start": "2023-02-22",
                    "finish": "2023-02-24",
                    "progress": 4,
                    "resource": "陈景峰"
                },
                "12": {
                    "id": 12,
                    "name": "权限角色开发",
                    "start": "2023-02-27",
                    "finish": "2023-03-03",
                    "resource": "Neo",
                    "progress": 5,
                    "predecessor": 11
                },
                "2": {
                    "id": "2",
                    "name": "测试任务排期",
                    "start": "2023-03-01",
                    "finish": "2023-03-15",
                    "subitem": {
                        "21": {
                            "id": 21,
                            "name": "用户登陆测试",
                            "start": "2023-03-01",
                            "finish": "2023-03-08",
                            "resource": "陈景峰",
                            "progress": 4
                        },
                        "22": {
                            "id": 22,
                            "name": "权限角色测试",
                            "start": "2023-03-09",
                            "finish": "2023-03-15",
                            "resource": "netkiller",
                            "progress": 0,
                            "predecessor": 21
                        }
                    }
                }
            }
        },
        "3": {
            "id": 3,
            "name": "任务组测试",
            "start": "2023-02-24",
            "finish": "2023-03-10",
            "resource": "陈景峰",
            "progress": 3,
            "subitem": {
                "4": {
                    "id": 4,
                    "name": "Java",
                    "start": "2023-02-24",
                    "finish": "2023-02-27",
                    "resource": "司空摘星",
                    "progress": 2
                },
                "5": {
                    "id": 5,
                    "name": "PHP",
                    "start": "2023-02-27",
                    "finish": "2023-03-17",
                    "resource": "阿不都沙拉木",
                    "progress": 5,
                    "predecessor": 4,
                    "subitem": {
                        "83": {
                            "id": 83,
                            "name": "V7.0",
                            "start": "2023-02-28",
                            "finish": "2023-03-03",
                            "predecessor": 82,
                            "subitem": {
                                "83": {
                                    "id": 83,
                                    "name": "V8.0",
                                    "start": "2023-03-06",
                                    "finish": "2023-03-10",
                                    "predecessor": 82,
                                    "subitem": {
                                        "83": {
                                            "id": 83,
                                            "name": "V8.5",
                                            "start": "2023-03-13",
                                            "finish": "2023-03-16",
                                            "predecessor": 82
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                "6": {
                    "id": "6",
                    "name": "Go",
                    "start": "2023-02-23",
                    "finish": "2023-03-08",
                    "milestone": False
                },
                "7": {
                    "id": 7,
                    "name": "Python",
                    "start": "2023-03-09",
                    "finish": "2023-03-10",
                    "milestone": True
                },
                "8": {
                    "id": 8,
                    "name": "Swift",
                    "start": "2023-02-27",
                    "finish": "2023-03-17",
                    "subitem": {
                        "81": {
                            "id": 81,
                            "name": "LLVM",
                            "start": "2023-02-27",
                            "finish": "2023-03-03",
                            "predecessor": 0
                        },
                        "82": {
                            "id": 82,
                            "name": "Clang",
                            "start": "2023-03-06",
                            "finish": "2023-03-10",
                            "predecessor": 81
                        },
                        "83": {
                            "id": 83,
                            "name": "Rust",
                            "start": "2023-03-13",
                            "finish": "2023-03-17",
                            "predecessor": 82
                        }
                    }
                }
            }
        }
    }
    try:

        gantt = Gantt()
        # gantt.hideTable()
        gantt.load(data)
        gantt.author("Neo Chen")
        # gantt.setWorkweeks(workweeks, options.oddeven)
        gantt.ganttChart("Test")
        gantt.save("test.svg")
        # gantt.export(file)

        # gantt.main()
    except KeyboardInterrupt as e:
        print(e)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
