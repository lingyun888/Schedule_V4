# flow_packet = {1:F1_0, 2:F1_1,....}
class TimeTable:

    def __init__(self):
        self.time_table = {}
        self.fail_flows = []

    def put_path_and_time_list_to_table(self, flow, path, time_list):
        temp_dict = {}

        for time, flow_packet_dict in time_list.items():
            temp_dict[time] = {}
            # 若此时间尚未被建立
            if self.time_table.get(time) is None:
                temp_dict[time][(path["Ingress"], path["Egress"])] = flow_packet_dict
            # 时间已建立，path尚未建立：无冲突Path问题，直接放置flow_packet
            elif self.time_table.get(time) is not None:
                if self.time_table[time].get((path["Ingress"], path["Egress"])) is None:
                    temp_dict[time][(path["Ingress"], path["Egress"])] = flow_packet_dict
                # 时间已建立path也建立完毕，将会有link_time_collision，先预设排序较后面的flow name优先级较低，需先去除
                else:
                    temp_dict = {}
                    self.fail_flows.append(flow)
                    break

        if temp_dict:
            for time in temp_dict.keys():
                if time in self.time_table:
                    self.time_table[time].update(temp_dict[time])
                else:
                    self.time_table[time] = temp_dict[time]

    def put_large_data_to_table(self):
        pass
