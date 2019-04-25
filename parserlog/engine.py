#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
from collections import Counter


def parse(file):
    pattern_id = re.compile(r'([A-Z0-9]{11})(?=:)')
    pattern_from = re.compile(r'(?<=from=<)[a-zA-Z0-9._%+-]+@([a-zA-Z0-9.-]+)(\.[a-zA-Z]{2,4})(?=>)')
    tmp_store = dict()
    count_ok = Counter()
    count_fail = Counter()
    with open(file, 'r') as file_log:
        for line in file_log:
            id_field = pattern_id.search(line)
            from_field = pattern_from.search(line)
            if id_field and from_field:
                # add key:value to temp dict
                tmp_store[id_field.group()] = str.lower(from_field.group())
            elif 'status=' in line and tmp_store.get(id_field.group()):
                # check status in line
                if 'sent' in line:
                    try:
                        count_ok[tmp_store[id_field.group()]] += 1
                    except KeyError:
                        count_ok[tmp_store[id_field.group()]] = 0
                else:
                    try:
                        count_fail[tmp_store[id_field.group()]] += 1
                    except KeyError:
                        count_fail[tmp_store[id_field.group()]] = 0
            elif 'removed' in line and tmp_store.get(id_field.group()):
                del tmp_store[id_field.group()]
            id_field = None
            from_field = None
        count_total = count_ok + count_fail
    # call write function or return value
    return count_total, count_ok, count_fail


def write_in_file(total, ok, fail, file='./result'):
    with open(file, 'w') as result_file:
        for item in total.most_common():
            result_file.write(
                'E-MAIL: %s; TOTAL: %s; OK: %s; FAIL: %s\n' % (item[0], item[1], ok[item[0]], fail[item[0]]))

