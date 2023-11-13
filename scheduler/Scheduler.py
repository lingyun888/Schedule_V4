import math
import copy
from scheduler.InitFlowFilter_copy import InitFlowFilter
from scheduler.ScheduleMiddle_copy import ScheduleMiddle
from scheduler.Timetable import TimeTable


class Scheduler:
    def __init__(self, flow_dic, flow_links, flow_paths_dic):
        self.flow_dic = flow_dic
        self.flow_links = flow_links
        self.flow_paths_dic = flow_paths_dic
        self.fail_flows = []
        self.time_table_maintainer = TimeTable()

    def scheduling(self):
        print("\n\n------------------------------")
        print(f"(Scheduler.py)\n")
        # 将有相同first_Link的flows依据path从小排到大，发生冲突时path较小的可优先被挑选
        init_flows = InitFlowFilter(self.flow_dic, self.flow_paths_dic, self.time_table_maintainer)
        init_flows.init_flows_filter()
        self.fail_flows = self.time_table_maintainer.fail_flows
        print(f"fail flows = {self.fail_flows}\n")

        # 打印时间表
        for time, path in self.time_table_maintainer.time_table.items():
            print(f"↓↓↓↓{time}↓↓↓↓")
            for links, packets in path.items():
                print(f"link = {links}, packets = {packets}")
        print(f"{self.time_table_maintainer.time_table}")

        schedule_middle = ScheduleMiddle(self.flow_dic, self.flow_paths_dic, self.time_table_maintainer)
        schedule_middle.schedule_middle()

        print(f"path_dic = ")
        for flow, paths in self.flow_paths_dic.items():
            print(f"{flow}=")
            for path in paths:
                print(path)
        print("-------------------------------")
        return self.flow_paths_dic
