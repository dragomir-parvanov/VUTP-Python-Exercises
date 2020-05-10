# 2. From the apache error_log file extract error messages and show report
# - clacify the type of error
# - when the error had happend
# - which user IP addresses has been affected

import re
from enum import Enum


class Log_type(Enum):
    INFO = 1
    ERROR = 2


class Error_user_log_model:
    def __init__(self, date, type: str, ip, reason):
        if type == "info":
            self.type = Log_type.INFO
        elif type == "error":
            self.type = Log_type.ERROR
        self.date = date
        self.ip = ip
        self.reason = reason
    type: Log_type
    date: str
    ip: str
    reason: str


error_logs_regex_pattern = r"\[(.*)\] \[(.*)\] \[client (.*)\] (.*)"

error_logs_file = open("error_logs.txt", "r").read()

matches = re.finditer(error_logs_regex_pattern, error_logs_file, re.MULTILINE)

logs = []
for matchNum, match in enumerate(matches):
    groups = match.groups()
    log = Error_user_log_model(groups[0], groups[1], groups[2], groups[3])
    logs.append(log)

problems_dict = dict([])
for log in logs:
    if log.reason in problems_dict:

        problems_dict[log.reason].append(log.ip)
    else:
        problems_dict[log.reason] = [log.ip]


for problem in problems_dict.items():
    print("Problem:\"{}\"\naffected ips:{}".format(
        problem[0], ", ".join(set(problem[1]))))
