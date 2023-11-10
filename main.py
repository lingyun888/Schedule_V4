# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication
from InputFlow import InputFlow
from scheduler.Scheduler import Scheduler
from Topology import Topology
from scheduler.Demo_copy import Demo


# from ResourceUsagePlot import ResourceUsagePlot


def main():

    # 读取flow参数                       OK
    input_flow = InputFlow()
    flow_dic = input_flow.run()

    # 构建拓扑(假设已从CUC得到拓扑信息)     OK
    topology = Topology(flow_dic)
    topology.load_links("links.txt")
    topology.create_reverse_links()

    # 得到每个flow的路径流向
    topology.routing()

    # 规划排程
    scheduler = Scheduler(topology.flow_dic, topology.links, topology.path_dic)

    # print(f"流字典 : ")
    # for key, value in topology.flow_dic.items():
    #     print(f"{key}: {value}")
    # print(f"链接字典 : ")
    # for key, value in topology.links.items():
    #     print(f"{key}: {value}")
    # print(f"路径字典 : ")
    # for key, value in topology.path_dic.items():
    #     print(f"{key}: {value}")

    scheduler.scheduling()

    # 窗口结果展示
    app = QApplication(sys.argv)
    view = Demo(topology.links)

    view.setWindowTitle('CNC调度窗口')

    view.show()
    view.update_graphics_from_dict(scheduler.time_table_maintainer.time_table)

    sys.exit(app.exec_())


if __name__ == '__main__':

    main()
