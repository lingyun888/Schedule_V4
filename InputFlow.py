import json


class InputFlow:

    def __init__(self):
        pass

    def run(self):
        with open('flow_data.json', 'r') as json_file:
            flow_dic = json.load(json_file)
            # print("\n\n", pd.DataFrame(flow_dic))
            return flow_dic
