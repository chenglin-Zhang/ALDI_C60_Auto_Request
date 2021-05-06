
class Global_Val(object):
    id = 0
    request_name = "1"
    url = "2"
    run = "3"
    run_way = "4"
    headers = "5"
    case_depend = "6"
    date_depend = "7"
    field_depend = "8"
    data = "9"
    expect = "10"
    result = "11"

    def get_id(slef):
        return slef.id

    def get_request_name(self):
        return self.request_name

    def get_url(self):
        return self.url

    def get_run(self):
        return self.run

    def get_run_way(self):
        return self.run_way

    def get_headers(self):
        return self.headers

    def get_case_depend(self):
        return self.case_depend

    def get_data_depend(self):
        return self.date_depend

    def get_field_depend(self):
        return self.field_depend

    def get_data(self):
        return self.data

    def get_expect(self):
        return self.expect

    def get_result(self):
        return self.result