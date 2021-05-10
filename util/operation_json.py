import json
import os


class OperationJson:
    """操作json文件"""

    def __init__(self, file_path=None):
        if file_path == None:
            base_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
            file_path = os.path.join(base_path, "dataconfig\data.json")
            self.file_path = file_path
        else:
            self.file_path = file_path
        self.data = self.read_data()

    def read_data(self):
        """
        读取json文件
        :param
        :return:
        """
        with open(self.file_path, encoding="utf8") as fp:
            data = json.load(fp)
            fp.close()
            return data

    def get_data(self, id):
        """根据关键字获取对应数据"""
        return self.data[id]

    # 写入json
    def write_token(self, data):
        with open("../dataconfig/token.json", 'w') as fp:
            fp.write(json.dumps(data))
            fp.close()

    def write_data(self, case_id, res):
        data = self.read_data()
        data[case_id] = res
        with open(self.file_path, 'w+', encoding="utf8") as fp:
            fp.write(json.dumps(data,ensure_ascii=False))
            fp.close()


if __name__ == '__main__':
    # file_path = "../dataconfig/data.json"
    opejson = OperationJson()
    # print(opejson.get_data('filtrate'))

    res = {
      "msg": "ok",
      "result": [
        {
          "author": "元稹",
          "detailid": 2,
          "name": "行宫"
        }]}

    opejson.write_data("case2", res)