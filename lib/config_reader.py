import os
import yaml
import ast


class ConfigReader(object):
    def __init__(self):
        config = self.read_yml('config')
        res = ast.literal_eval(str(config["prisma_cloud"]))
        self.rl_user = res['username']
        self.rl_pass = res['password']
        self.rl_cust = res['customer_name']
        self.rl_api_base = res['api_base']
        self.rl_timerange_unit = "hour" if res['timerange_unit']==None else res['timerange_unit']
        self.rl_timerange_amount = 5 if res['timerange_amount']==None else res['timerange_amount']
        self.rl_filter_resource_type = ast.literal_eval(str(res['filter_resource_type']))

    @classmethod
    def read_yml(self, f):
        yml_path = os.path.join(os.path.dirname(__file__), "../config/%s.yml" % f)
        with open(yml_path,'r') as stream:
            return yaml.safe_load(stream)
