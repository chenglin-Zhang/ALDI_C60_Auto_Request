from util.operation_json import OperationJson
import json

class OperationDepend(object):

    def __init__(self):
        self.operation_json = OperationJson()
        pass


    def get_recursively(self, search_dict, field):
        '''
        迭代获取dict符合key的所有值
        :param search_dict: 查询的字典
        :param field: 查询的key
        :return: 列表
        '''
        fields_found = []
        for key, value in search_dict.items():
            if key == field:
                fields_found.append(value)
            elif isinstance(value, dict):
                results = self.get_recursively(value, field)
                for result in results:
                    fields_found.append(result)
            elif isinstance(value, list):
                for item in value:
                    if isinstance(item, dict):
                        more_results = self.get_recursively(item, field)
                        for another_result in more_results:
                            fields_found.append(another_result)
        return fields_found

    def get_depend_data(self, case_case, depend_key, depend_field, request_data):
        '''
        获取依赖数据，并给依赖数据赋值
        :param case_case: 依赖的case
        :param depend_key: 依赖case的字段
        :param depend_field: 需要替换的请求体
        :param request_data: 请求的参数
        :return:
        '''
        depend_key_list = depend_key.split()
        depend_field_list = depend_field.split()

        data = self.operation_json.get_data(case_case)
        data = eval(data)
        for (depend_key, depend_field) in zip(depend_key_list, depend_field_list):
            res = self.get_recursively(data, depend_key)
            request_data[depend_field] = res[0]
        return request_data
