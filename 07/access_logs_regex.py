# 1. Create a python program that reads apache log file - access_log and from that log file using regular expressions extracts and group following information:

# - IP address

# - accessed page path

# And based on that information:

#  - show top 5 IP addresses based on the count of connections

#   - show top 5 most vissited web content


import re


class Access_log_model:
    def __init__(self, request_ip, content):
        self.request_ip = request_ip
        self.content = content
    request_ip: str
    content: str


access_log_match_pattern = r"(.*) - - .*\"GET (.*)\?|(.*) - - .*\"GET (.*) HTTP"

access_logs_file = open("access_logs.txt", "r").read()

matches = re.finditer(access_log_match_pattern, access_logs_file, re.MULTILINE)

access_logs = []
for matchNum, match in enumerate(matches):

    groups = match.groups()
    if (groups[2]):
        log = Access_log_model(groups[2], groups[3])
        access_logs.append(log)
    else:
        log = Access_log_model(groups[0], groups[1])
        access_logs.append(log)


def print_top(array: list, top: int):
    if len(array) <= 0:
        return
    count_dict = dict()
    for elem in array:
        element: str = elem
        if element in count_dict:
            count_dict[elem] += 1
        else:
            count_dict[elem] = 1
    pairs = list(count_dict.items())

    tops = [pairs[0]]

    for pair in pairs[1:]:
        topsLen = len(tops)
        if topsLen < top:
            tops.append(pair)
            tops = list(reversed(sorted(tops, key=lambda tup: tup[1])))
        elif pair[1] > tops[topsLen-1][1]:

            tops.pop()
            tops.append(pair)

            tops = list(reversed(sorted(tops, key=lambda tup: tup[1])))
            # sorting the array from the second tuple

    for i in range(0, len(tops)):
        print("{} place: Value:\"{}\" Total times:{}".format(
            i+1, tops[i][0], tops[i][1]))


print("Top 5 IP addresses based on the count of connections")

ips = []

for log in access_logs:
    ips.append(log.request_ip)

print_top(ips, 5)

print("Top 5 most visited web content")

contents = []

for log in access_logs:
    contents.append(log.content)

print_top(contents, 5)
