from common.runmethond import RunMethod
from data.get_data import GetData
from util.common_util import CommonUtil
# from data.dependent_data import DependentData
# from util.send_email import SendEmail
# from util.operation_header import OperationHeader
from util.operation_json import OperationJson


class RunTest:

    def __init__(self):
        self.run_method = RunMethod()
        self.data = GetData()
        self.com_util = CommonUtil()
        # self.send_email = SendEmail()

    def go_on_run(self):
        """程序执行"""
        pass_count = []
        fail_count = []
        res = None
        # 获取用例数
        rows_count = self.data.get_case_lines()
        # 第一行索引为0
        for i in range(1, rows_count):
            is_run = self.data.get_is_run(i)
            if is_run:
                url = self.data.get_request_url(i)
                method = self.data.get_request_method(i)
                request_data = self.data.get_request_data(i)
                expect = self.data.get_expcet_data(i)
                print(expect)
                header = self.data.is_header(i)

                res = self.run_method.run_main(method, url, request_data)
                print(res)

                if expect != None:
                    if self.com_util.is_contain(expect, res):
                        pass_count.append(i)
                    else:
                        fail_count.append(i)
                else:
                    print(f"用例ID：case-{i}，预期结果不能为空")

        print(f"通过用例数：{len(pass_count)}")
        print(f"失败用例数：{len(fail_count)}")


if __name__ == '__main__':
    run = RunTest()
    run.go_on_run()