# 这边方法采用最笨的排法，也就是依照flow编号排下去，编号前面的优先度较高
class ScheduleMiddle:

    def __init__(self, flow_dic, flow_paths_dic, time_table_maintainer):
        self.flow_dic = flow_dic
        self.flow_paths_dic = flow_paths_dic
        self.time_table = time_table_maintainer.time_table  # dict

    def schedule_middle(self):
        reschedule = {}
        for time in range(0, 101):

            if self.time_table.get(time) != None:
                # 依据当前时间所佔据在link上的Packets，取得他下一条是哪条link，并排程他近期可以占用的时间
                for link1, packet in self.time_table[time].items():
                    next_link = ()
                    # 取得下一条link
                    for link2 in self.flow_paths_dic[packet["Flow"]]:
                        if link2["Ingress"] == link1[1]:
                            next_link = (link2["Ingress"], link2["Egress"])
                            break
                    # 如果还没到结束路径(开始排他可以next_link最快可以占用的时间)
                    if next_link:
                        # 如果time+1沒有被建立
                        if self.time_table.get(time + 1) == None:
                            # 建立link并将封包丢到time_slot里面
                            self.time_table[time + 1] = {}
                            self.time_table[time + 1].update({next_link: packet})
                        else:
                            # 如果time+1已被建立但是里面没有该link(亦即无冲突)
                            if self.time_table[time + 1].get(next_link) == None:
                                self.time_table[time + 1][next_link] = packet
                            # 如果time+1已被建立，且里面有该Link存在(发生冲突)
                            else:
                                if reschedule.get(time + 1) == None:
                                    reschedule[time + 1] = {}
                                reschedule[time + 1].update({next_link: packet})
        if reschedule:
            print(f"\n\n重新排程：{reschedule}\n")
            self.rescheduling(reschedule)

    def rescheduling(self, reschedule):
        remaining_schedule = {}
        for time, link_dic in reschedule.items():
            for link, packet in link_dic.items():
                set_up = True
                while set_up:
                    if self.time_table.get(time) == None:
                        self.time_table[time] = {}
                        self.time_table[time][link] = packet

                        set_up = False
                    else:
                        if self.time_table[time].get(link) == None:
                            self.time_table[time][link] = packet

                            set_up = False
                        else:
                            time += 1

                for link2 in self.flow_paths_dic[packet["Flow"]]:
                    next_link = ()
                    if link2["Ingress"] == link[1]:
                        next_link = (link2["Ingress"], link2["Egress"])
                        break
                if next_link:
                    if remaining_schedule.get(time + 1) == None:
                        remaining_schedule[time + 1] = {next_link: packet}
                    else:
                        remaining_schedule[time + 1].update({next_link: packet})

        if remaining_schedule:
            self.rescheduling(remaining_schedule)
        print(f"剩余的：schedule = {remaining_schedule}")
