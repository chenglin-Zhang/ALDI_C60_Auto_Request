import datetime
import os
import unittest
from HTMLTestRunner import HTMLTestRunner
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

cur_path = os.path.dirname(os.path.realpath(__file__))


def add_case(caseName = "case", rule="test*.py"):
    case_path = os.path.join(cur_path, caseName)

    if not os.path.exists(case_path):
        os.mkdir(case_path)

    discover = unittest.defaultTestLoader.discover(case_path, pattern=rule, top_level_dir=None)

    return discover


def run_case(all_case, reportName = "report"):
    now = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

    report_path = os.path.join(cur_path, reportName)
    if not os.path.exists(report_path):
        os.mkdir(report_path)

    report_abs_file = os.path.join(report_path, now+".html")
    print("report_abs_file:----"+report_abs_file)

    fp = open(report_abs_file, 'wb')

    runner = HTMLTestRunner(stream=fp, title=u'自动化测试报告，测试结果如下：', description=u'用例执行情况')

    runner.run(all_case)
    fp.close()


def get_report_file(report_path):
    lists = os.listdir(report_path)
    lists.sort(key=lambda fn : os.path.getmtime(os.path.join(report_path, fn)))
    report_file = os.path.join(report_path, lists[-1])
    return report_file


def send_mail(from_user, password, to_user, report_file, server, port):
    with open(report_file, 'rb') as f:
        mail_body = f.read()

    msg = MIMEMultipart()
    body = MIMEText(mail_body, 'html', 'utf-8')
    msg["Subject"] = "接口测试报告"
    msg["From"] = from_user
    msg["To"] = to_user
    msg.attach(body)

    # 添加附件
    att = MIMEText(open(report_file, 'rb').read(), "base64", 'utf-8')
    att["Content-Type"] = "application/octet-stream"
    att["Content-Disposition"] = "attachment; filename= report.html"
    msg.attach(att)

    smtp = smtplib.SMTP()
    smtp.connect(server, port)
    smtp.login(from_user, password)
    smtp.sendmail(from_user, to_user.split(","), msg.as_string())
    smtp.quit()

    print("report_mail send success")


if __name__ == '__main__':
    all_case = add_case()
    run_case = run_case(all_case)

    report_path = os.path.join(cur_path, "report")
    report_file = get_report_file(report_path)

    from config import readConfig
    from_user = readConfig.from_user
    password = readConfig.password
    to_user = readConfig.to_user
    server =readConfig.server
    port = readConfig.port

    send_mail(from_user, password, to_user, report_file, server, port)