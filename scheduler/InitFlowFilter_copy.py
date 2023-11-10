class InitFlowFilter:

    def __init__(self, flow_dic, flow_paths_dic, time_table_maintainer):
        self.flow_dic = flow_dic
        self.flow_paths_dic = flow_paths_dic
        self.time_table_maintainer = time_table_maintainer

    # 应该要将比较方法放在时间表(time_table)里面进行，会有比较高的可调整性。(但这边想说一次处理，先利用path_dic执行看看，之后有机会再做模组化调整)
    def init_flows_filter(self):

        # 先将时间放入各Flow的path中的first link，并计算path size
        for flow, path in self.flow_paths_dic.items():
            time_list = self.generate_time_slot(flow)
            self.time_table_maintainer.put_path_and_time_list_to_table(flow, path[0], time_list)

    # 加入时间
    def generate_time_slot(self, flow):
        time_list = {}
        start = self.flow_dic[flow]["StartTime"]
        period = self.flow_dic[flow]["Period"]
        times = self.flow_dic[flow]["Times"]
        size = self.flow_dic[flow]["Size"]
        current_time = start
        for _ in range(times):
            for times in range(size):
                time_list[current_time] = {"Flow": flow, "Packet": times}
                current_time += 1
            current_time += period - size
        return time_list
