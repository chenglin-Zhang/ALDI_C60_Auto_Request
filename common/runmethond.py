import json
import requests


class RunMethod(object):

    def get_main(self, url, data, header=None):
        res = None
        if header:
            res = requests.get(url=url, params=data, headers=header, verify=False)
        else:
            res = requests.get(url=url, params=data)
        return res.json()

    def post_main(self, url, data, header=None):
        res = None
        print(header)
        if header:
            res = requests.post(url=url, json=data, headers=header, verify=False)
        else:
            res = requests.post(url=url, json=data)
        return res.json()

    def run_main(self, method, url, data=None, header=None):
        '''
        调用请求方式的主方法
        :param method:
        :param url:
        :param data:
        :param header:
        :return:    sort_keys =True:是告诉编码器按照字典排序(a到z)输出。如果是字典类型的python对象，就把关键字按照字典排序。
                    indent:参数根据数据格式缩进显示，读起来更加清晰。
                    ensure_ascii=True：默认输出ASCLL码，如果把这个该成False,就可以输出中文。
        '''
        res = None
        if method == "get":
            res = self.get_main(url, data, header)
        elif method == "post":
            res = self.post_main(url, data, header)
        return json.dumps(res, indent=2, sort_keys=True, ensure_ascii=False)


if __name__ == '__main__':
    url = "http://10.1.23.245:9221/tpdotnet/pos/webapi/process-barcode"
    data = {
        "clientname":"Android-ZL",
        "clientId":"webapi",
        "Workflow":"process-barcode",
        "lOperatorID":"8888",
        "szSignOnName":"8888",
        "szEmplName": "IT Support",
        "InputString":"10000001",
        "Ta":"TRANS_B2507E36-11D9-4DA3-AEB6-8AD846D471D2"
    }
    header = {'Content-Type': 'application/json'}

    run = RunMethod()
    res = run.run_main(method="post", url=url, data=data, header=header)
    print(res)
